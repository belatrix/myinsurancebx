import base64
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from web3.exceptions import CannotHandleRequest
from raven.contrib.django.raven_compat.models import client
from rest_framework.schemas import ManualSchema
import coreschema
import coreapi

from managers import ContractManager
from utils import Utils
from local_settings import TEMPORARY_OTS_PREFIX, PERMANENT_OTS_PREFIX, CONTRACTS


class Stamp(APIView):
    """
    [POST]
    Permite realizar un stamp de un archivo

    Parámetros recibidos:
    [Content-Type:application/json]
    - file_hash: El hash del archivo encodeado en sha256

    Devuelve un OTS (https://opentimestamps.org) para poder verificar en el futuro que el archivo fue incluido a la Blockchain

    Ejemplo:
    {
      "file_hash": "1957db7fe23e4be1740ddeb941ddda7ae0a6b782e536a9e00b5aa82db1e84547"
    }
    """

    schema = ManualSchema(fields=[
        coreapi.Field(
            name='file_hash',
            required=True,
            location='form',
            schema=coreschema.String(),
            description='El hash del archivo encodeado en sha256',


        ),
    ])

    def post(self, request):

        try:
            if not request.data.get('file_hash'):
                raise ValidationError('file_hash')

            file_hash = request.data.get('file_hash')

            ots_hash = Utils.get_ots_hash(file_hash)

            tx_hash = ContractManager.stamp(ots_hash, file_hash)

            #Al OTS se le agrega la transacción para poder verificar luego si está pendiente de subida
            ots = TEMPORARY_OTS_PREFIX + '-' + ots_hash + '-' + tx_hash.hex()

            return Response({_('status'): _('success'), _('temporary_ots'): base64.b64encode(ots.encode('utf-8')).decode('utf-8')}, status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response({_('status'): _('failure'), _('messages'): _('parameter_missing') % e.message}, status=status.HTTP_400_BAD_REQUEST)
        except CannotHandleRequest:
            return Response({_('status'): _('failure'), _('messages'): _('could_not_connect')}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            client.captureException()
            return Response({_('status'): _('failure'), _('messages'): _('operation_failed')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Verify(APIView):
    """
    [POST]
    Permite verificar que un archivo fue subido a la Blockchain

    Parámetros recibidos:
    [Content-Type:application/json]
    - file_hash: El hash del archivo original encodeado en sha256
    - ots: OTS recibido como prueba al momento de realizar el stamp

    Devuelve número de bloque, fecha y hora de subida a la Blockchain

    Ejemplo:
    {
      "file_hash": "1957db7fe23e4be1740ddeb941ddda7ae0a6b782e536a9e00b5aa82db1e84547",
      "ots": "NzNkYzA5OGJkODlmZjdlMjc4OGFjMzJlNmU2ODdiOTdmODdiMTBjMWIyNzg5OTFlMDNkN2E2YWVkMDk3ODJkZTAxLTB4NGM2ZmNiNDBhMmUyZGVjYzc2YWQzMjM3MDU2NzZjMjljYWE1MmIyYjZkMDdiMDIzYjBhY2EzOWYzZGIxYmRlZg=="
    }
    """

    schema = ManualSchema(fields=[
        coreapi.Field(
            name='file_hash',
            required=True,
            location='form',
            schema=coreschema.String(),
            description='El hash del archivo encodeado en sha256',
        ), coreapi.Field(
            name='ots',
            required=True,
            location='form',
            schema=coreschema.String(),
            description='El OTS recibido al hacer el stamp del archivo encodeado en sha256',
        )
    ])

    def post(self, request):

        try:
            if not request.data.get('file_hash'):
                raise ValidationError('file_hash')

            if not request.data.get('ots'):
                raise ValidationError('ots')

            file_hash = request.data.get('file_hash')
            base64_ots = request.data.get('ots')

            ots = base64.b64decode(base64_ots).decode('utf-8')

            ots_version = ots[:2]

            if ots_version == PERMANENT_OTS_PREFIX:

                ots_version, file_hash, ots_hash, tx_hash, block_number = ots.split('-')

                transaction = ContractManager.get_transaction(tx_hash)

                method_name, args = Utils.decode_contract_call(CONTRACTS['01']['abi'], transaction.input)

                tx_ots_hash = args[0].decode('utf-8')
                tx_file_hash = args[1].decode('utf-8')

                if tx_ots_hash == ots_hash and tx_file_hash == file_hash:

                    block = ContractManager.get_block(int(block_number))

                    permanent_ots = PERMANENT_OTS_PREFIX + '-' + file_hash + '-' + ots_hash + '-' + tx_hash + '-' + str(block_number)

                    return Response({_('status'): _('success'),
                                     _('permanent_ots'): base64.b64encode(permanent_ots.encode('utf-8')).decode('utf-8'),
                                     _('messages'): _('file_uploaded') % (
                                     file_hash, str(block.number), str(Utils.datetime_from_timestamp(block.timestamp)))},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({_('status'): _('failure'), _('messages'): _('file_not_found')},
                                    status=status.HTTP_404_NOT_FOUND)

            else:

                ots_version, ots_hash, tx_hash = ots.split('-')

                contract_version = ots_hash[-2:]

                verified = ContractManager.verify(contract_version, ots_hash, file_hash)

                if verified:
                    block_number = ContractManager.get_block_number(contract_version, ots_hash)
                    block = ContractManager.get_block(block_number)

                    permanent_ots = PERMANENT_OTS_PREFIX + '-' + file_hash + '-' + ots_hash + '-' + tx_hash + '-' + str(block_number)

                    return Response({_('status'): _('success'), _('permanent_ots'): base64.b64encode(permanent_ots.encode('utf-8')).decode('utf-8') ,_('messages'): _('file_uploaded') % (file_hash, str(block.number), str(Utils.datetime_from_timestamp(block.timestamp)))},status=status.HTTP_200_OK)
                else:
                    try:
                        transaction = ContractManager.get_transaction(tx_hash)
                        if transaction and not transaction.blockNumber:
                            return Response({_('status'): _('pending'), _('messages'): _('transaction_pending')}, status=status.HTTP_200_OK)
                    except ValueError:
                        pass

                    return Response({_('status'): _('failure'), _('messages'): _('file_not_found')},status=status.HTTP_404_NOT_FOUND)

        except ValidationError as e:
            return Response({_('status'): _('failure'), _('messages'): _('parameter_missing') % e.message}, status=status.HTTP_400_BAD_REQUEST)
        except CannotHandleRequest:
            return Response({_('status'): _('failure'), _('messages'): _('could_not_connect')}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            client.captureException()
            return Response({_('status'): _('failure'), _('messages'): _('operation_failed')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




