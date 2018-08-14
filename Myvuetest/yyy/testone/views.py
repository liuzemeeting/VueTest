import json
import time
import hashlib
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login,\
    logout as auth_logout, get_user_model
from django.contrib.auth.models import User
User = get_user_model()


#注册
def regist(req):
    if req.method == 'POST':
        username = req.POST.get("account")
        password = req.POST.get("passwords")
        #  添加到数据库
        User.objects.create_user(username= username,password=password)
        return HttpResponse('ok')
    return HttpResponse('error')


#登陆
def login(req):
    print(req.POST)
    if req.method == 'POST':
        username = req.POST.get("username")
        password = req.POST.get("passwords")
        user = authenticate(username = username,password = password)
        if user:
            data = get_token(user.id)
            auth_login(req, user)
            return HttpResponse(json.dumps({"status":'ok',"token":data}),content_type="appl")
        else:
            return HttpResponse('error')
    return HttpResponse('error')


#  登陆成功
def index(req):
    userdata = []
    data = req.META.get("HTTP_TBKT_TOKEN")
    if data:
        datalist = User.objects.filter()
        for i in datalist:
            data = {
                'id': i.id,
                'username': i.username,
                'email': i.email,
                'datatime': (i.date_joined).strftime('%Y-%m-%d %H:%M:%S')
            }
            userdata.append(data)
        return HttpResponse(json.dumps({"status": 'ok','response':userdata}), content_type="application")
    return HttpResponse(json.dumps({"status": 'error', 'response': userdata}), content_type="application")


def useredit(req):
    userid = int(req.POST.get("id"))
    username = req.POST.get("username")
    email = req.POST.get("email")
    try:
        User.objects.filter(id=userid).update(username=username, email=email)
        return HttpResponse('ok')
    except Exception as e:
        print(e)
        return  HttpResponse('error')


#  退出
def logout(req):
    auth_logout(req)
    return HttpResponse("ok")


def delete(req):
    id = int(req.POST.get("id"))
    try:
        User.objects.filter(id=id).delete()
        return HttpResponse('ok')
    except Exception as e:
        print(e)
        return HttpResponse("error")


def get_token(userid):
    """
    生成token值
    """
    data = int(time.time())
    data = str(data) + str(userid)
    h1 = hashlib.md5()
    h1.update(data.encode(encoding='utf-8'))
    response = h1.hexdigest()
    return response
