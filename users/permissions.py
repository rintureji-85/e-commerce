from rest_framework.permissions import BasePermission
class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=='admin'

class IsMerchant(BasePermission):
     def has_permission(self,request,view):
            return request.user.is_authenticated and request.user.role=='merchant'
     
class Iscustomer(BasePermission):
     def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=='customer'