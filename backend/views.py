from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from backend.models import *


# Create your views here.
def getRoutineList(request):
    id = request.GET.get('id')
    response = {}
    try:
        # 此处从数据库中获取routinelist信息和selected信息
        user = UserInfo.objects.get(userid=id)
        # print(user)
        routinelist = []
        rt = user.routine_set.all().values("routine")
        for r in rt:
            routinelist.append({"name": r["routine"]})
        print(routinelist)
        selected = '睡眠'
        response['routinelist'] = routinelist
        response['selected'] = selected
        response = JsonResponse(response)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)


def postRoutineList(request):
    id = request.POST.get('id')
    select = request.POST.get('selected')
    time = request.POST.get('time')
    print(id+r'事务变更：')
    print(select)
    print(time)
    try:
        # 存入数据库
        response = HttpResponse('completed')
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)


def getAllPosts(request):
    id = request.GET.get('id')
    response = {}
    try:
        # 从数据库里面读取
        allposts = [{
            'title': '第一条',
            'content': 'zsbdzsbd',
            'time': 'yyyy-mm-dd hh:mf:ss'
        }, {'title': '第一条',
            'content': 'zsbdzsbd',
            'time': 'yyyy-mm-dd hh:mf:ss'}]
        response['allposts'] = allposts
        response = JsonResponse(response)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)


def newPost(request):
    id = request.POST.get('id')
    post = request.POST.get('post')
    print(id+r'存储帖子：')
    print(post)
    try:
        # 存入数据库
        response = HttpResponse('completed')
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)


def getUser(request):
    id = request.GET.get('id')
    response = {}
    try:
        # 从数据库中读取
        response['username'] = '约翰史密斯'
        response['quote'] = '做时间的主人，过健康的生活'
        response['usetime'] = '24'
        response['gender'] = 'female'
        response['height'] = '166'
        response['weight'] = '52'
        response['age'] = '24'
        # 经过一番判断
        response['healthstatus'] = '优'
        response = JsonResponse(response)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)
