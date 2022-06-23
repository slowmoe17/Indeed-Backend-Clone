from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth import get_user_model


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type == 'employer'

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type == 'employee'

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS


