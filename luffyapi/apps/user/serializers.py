from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.utils import jwt_encode_handler,jwt_payload_handler

class UserModelSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = models.User
        fields = ("username","id","password")
        extra_kwargs = {
            "id":{"read_only":True},
            "password":{"write_only":True}
        }

    def validate(self, attrs):
        # 获取用户
        user_obj = self._get_user(attrs)
        # 签发token
        token = self._get_token(user_obj)
        # 放到context在视图中接受
        self.context["token"] = token
        self.context["username"] = user_obj.username
        self.context["id"] = user_obj.id
        return attrs

    def _get_token(self,user_obj):
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        return token

    @staticmethod
    def _get_user(attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        import re
        if re.match("^1[3-9]\d{9}$",username):
            # 手机号登录
            user_obj = models.User.objects.filter(telephone=username).first()
        elif re.match("^.*@.*\.com$",username):
            # 邮箱
            user_obj = models.User.objects.filter(email=username).first()
        else:
            # 用户名
            user_obj = models.User.objects.filter(username=username).first()
        if user_obj:
            if user_obj.check_password(password):
                return user_obj
            else:
                raise ValidationError("密码错误")
        else:
            raise ValidationError("用户不存在")