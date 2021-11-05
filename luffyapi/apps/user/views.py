import re
from . import models
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from luffyapi.utils.response import APIResponse
from rest_framework.decorators import action
# Create your views here.
from . import serializers
class LoginView(ViewSet):
    @action(methods=["post"],detail=False)
    def login(self,request,*args,**kwargs):
        ser = serializers.UserModelSerializers(data=request.data)
        ser.is_valid(raise_exception=True)
        token = ser.context.get("token")
        username = ser.context.get("username")
        id = ser.context.get("id")
        return APIResponse(token=token,username=username,id=id)

    @action(methods=["get"], detail=False)
    def telephone_exist(self,request,*args,**kwargs):
        telephone = request.GET.get("telephone")
        import re
        if not re.match("^1[3-9]\d{9}$",telephone):
            return APIResponse(code="0",msg="手机号不合法")
        else:
            models.User.objects.get(telephone=telephone)
            return APIResponse(msg="手机号存在")