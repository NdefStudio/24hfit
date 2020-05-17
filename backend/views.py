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
        user = UserInfo.objects.get(pk=id)
        # print(user)
        routinelist = []
        rt = user.routine_set.all().values("routine")
        for r in rt:
            routinelist.append({"name": r["routine"]})
        print(routinelist)
        selected = '睡眠'
        routinelist = [
            {'name': '睡眠', 'icon': 'bla1'},
            {'name': '学习', 'icon': 'bla1'},
            {'name': '工作', 'icon': 'bla1'},
            {'name': '跑步', 'icon': 'bla1'},
            {'name': '跳绳', 'icon': 'bla1'},
            {'name': '跑步', 'icon': 'bla1'},
            {'name': '自由活动', 'icon': 'bla1'},
            {'name': '其他娱乐', 'icon': 'bla1'},
        ]
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
        crt = Routine.objects.filter(routine=select).first()
        usr = UserInfo.objects.filter(pk=id).first()
        sttime = usr.crtroutine_starttime
        rt = usr.crtroutine
        RoutineRecord.objects.create(
            routine=rt, endtime=time, manualend=True, starttime=sttime)
        # 更新userinfo
        UserInfo.objects.filter(pk=id).update(
            crtroutine=crt, crtroutine_starttime=time)
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
        usr = UserInfo.objects.filter(pk=id).first()
        pst = PostInfo.objects.filter(user=usr)
        allposts = []
        for p in pst:
            allposts.append({
                'title': p.title,
                'content': p.content,
                'time': p.time
            })
        allposts = [{
            'title': '第一天',
            'content': '早上跑步一圈',
            'time': '2020-01-12 09:34:06'
        }, {'title': '第一天',
            'content': '熬夜',
            'time': '2020-01-12 23:31:45'}]
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
        usr = UserInfo.objects.filter(pk=id).first()
        PostInfo.objects.create(
            user=usr, title=post['title'], content=post['content'], time=post['time'])
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
        usr = UserInfo.objects.filter(pk=id).first()
        response['username'] = usr.username
        response['quote'] = usr.quote
        # response['usetime'] = '24'
        response['gender'] = usr.gender
        response['height'] = usr.height
        response['weight'] = usr.weight
        response['age'] = usr.age
        # 经过一番判断
        response['healthstatus'] = '优'
        response = JsonResponse(response)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)
