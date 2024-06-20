from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request


class UserView(APIView):
    def get(self, request):
        # print(request.user) # 当前登录的用户 -> 匿名用户（源码DRF.request-> _not_authenticated）
        # print(request.auth)
        return Response("UserView get")