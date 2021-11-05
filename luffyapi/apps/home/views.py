from django.shortcuts import render
from luffyapi.utils.response import APIResponse
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from . import models,serializers
from django.conf import settings
class BannerAPIView(GenericViewSet,ListModelMixin):
    queryset = models.Banner.objects.filter(is_delete=False,is_show=True).order_by("orders")[0:settings.BANNER_COUNTER]
    serializer_class = serializers.BannerModelSerializers
