from rest_framework import permissions


class IsInspectorOrStaff(permissions.BasePermission):
    message = "Inspector restricted or Staff member"

    def has_permission(self, request, view):
        return request.user and (request.user.is_inspector or request.user.is_staff)


class IsInsuranceOrStaff(permissions.BasePermission):
    message = "Insurance restricted or Staff member"

    def has_permission(self, request, view):
        return request.user and (request.user.is_from_insurance or request.user.is_staff)


class IsStaff(permissions.BasePermission):
    message = "Staff restricted"

    def has_permission(self, request, view):
        return request.user and request.user.is_staff
