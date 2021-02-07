from django.http import HttpResponse, JsonResponse
import json

def showIndex(request):
    html_text='<html><body bgcolor="orangeyellow"><h1>Python Is easy Language</h1></body></html>'
    return HttpResponse(html_text)

def showjsonindex(request) :
    d1={'name':'sanjay','mob':9178302988,'status':True}
    json_data=json.dumps(d1)
    return HttpResponse(json_data,content_type="application.json")

def showjson1index(request):
    d1 = {'name': 'kumar', 'mob': 9178302998, 'status': True}
    return JsonResponse(d1)

def showjson2index(request):
    d1=[
        {'name': 'kumar', 'mob': 9178302998, 'status': True},
        {'name': 'sanjay', 'mob': 9178302988, 'status': True}
    ]

    json_data=json.dumps(d1)
    return HttpResponse(json_data)
