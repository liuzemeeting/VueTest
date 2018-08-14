#!/usr/bin/env python
# coding=utf-8
import logging, traceback
import simplejson as json
import time
from django.http import QueryDict, HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("start")
        try:
            return self._process_request(request)
        except:
            exc = traceback.format_exc()

    def cross_domain(self, request, response=None):
        """
        添加跨域头
        """
        origin = request.META.get('HTTP_ORIGIN', '*')
        if request.method == 'OPTIONS' and not response:
            response = HttpResponse()
        if not response:
            return
        response['Access-Control-Allow-Origin'] = origin
        response['Access-Control-Allow-Methods'] = 'GET,POST'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,App-Type,Tbkt-Token'
        response['Access-Control-Max-Age'] = '1728000'
        return response

    def _process_request(self, request):

        # REQUEST过期, 使用QUERY代替
        query = request.GET.copy()
        query.update(request.POST)
        # 把body参数合并到QUERY
        try:
            body = json.loads(request.body)
            query.update(body)
        except:
            pass
        request.QUERY = query

        r = self.cross_domain(request)
        if r:
            return r
        path = request.path
        if not request.user_id and not path.startswith('/admin/log') and not path.startswith('/apidoc/'):
            return HttpResponse("error,token失效")

    def process_response(self, request, response):
        # 更新token
        if getattr(request, '_newtoken', None):
            auth.login_response(response, request._newtoken)
        # 添加跨域头
        self.cross_domain(request, response)
        print("end")
        return response
