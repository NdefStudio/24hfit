from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.
def getRoutineList(request):
    response = {}
    try:
        # 从数据库中获取routinelist信息和selected信息
        routinelist = [
            {'name': '睡眠', 'icon': 'bla1'},
            {'name': '学习', 'icon': 'bla1'},
            {'name': '工作', 'icon': 'bla1'},
            {'name': '跑步', 'icon': 'bla1'},
            {'name': '跳绳', 'icon': 'bla1'},
            {'name': '跑步', 'icon': 'bla1'},
            {'name': '跳绳', 'icon': 'bla1'},
            {'name': '跑步', 'icon': 'bla1'},
            {'name': '跳绳', 'icon': 'bla1'},
            {'name': '跑步', 'icon': 'bla1'},
            {'name': '跳绳', 'icon': 'bla1'},
            {'name': '跑步', 'icon': 'bla1'},
            {'name': '跳绳', 'icon': 'bla1'},
            {'name': '走路', 'icon': 'bla1'},
            {'name': '自由思考', 'icon': 'bla1'},
            {'name': '跑步', 'icon': 'bla1'},
            {'name': '跳绳', 'icon': 'bla1'},
            {'name': '跑步', 'icon': 'bla1'},
            {'name': '跳绳', 'icon': 'bla1'},
            {'name': '跑步', 'icon': 'bla1'},
            {'name': '跳绳', 'icon': 'bla1'},
            {'name': '走路', 'icon': 'bla1'},
            {'name': '自由思考', 'icon': 'bla1'}
        ]
        selected = '睡眠'
        response['routinelist'] = routinelist
        response['selected'] = selected
        response = JsonResponse(response)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)


def postRoutineList(request):
    select = request.POST.get('selected')
    time = request.POST.get('time')
    print(select)
    print(time)
    # 存入数据库
    response = HttpResponse('completed')
    response["Access-Control-Allow-Origin"] = "*"
    return response
