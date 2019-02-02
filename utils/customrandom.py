from datetime import datetime, timedelta
from random import getrandbits, randint


def random_boolean():
    return bool(getrandbits(1))


def random_document_number(characters):
    result = ''

    for i in range(characters):
        number = randint(0, 9)
        result += str(number)

    return result


def random_date_using_range_days(number_of_days):
    """
    Returns a random date in range of +/- number_of_days of current date.
    """
    start_date = datetime.now() + timedelta(days=-number_of_days)
    end_date = datetime.now() + timedelta(days=number_of_days)
    return start_date + timedelta(
        seconds=randint(0, int((end_date-start_date).total_seconds()))
    )
