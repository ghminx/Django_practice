from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse   # 요청에 대한 응답 


# /pybo 페이지에 띄울 index 함수 
# request : HTTP 요청 객체 
def index(request):
    return HttpResponse('pybo')
