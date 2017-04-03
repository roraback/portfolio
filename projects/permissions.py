from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow user to list all items if logged in user is staff
        return request.method in permissions.SAFE_METHODS # and request.user and is_authenticated(request.user)

    def has_object_permission(self, request, view, obj):
        # allow allows staff to view all records
        return request.method in permissions.SAFE_METHODS