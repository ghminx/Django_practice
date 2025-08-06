from django.urls import path

from . import views 

app_name = 'pybo'  # 앱 이름 설정

urlpatterns = [
    path('', views.index, name='index'),  # pybo/ 페이지에 index 함수 연결
    path('<int:question_id>/', views.detail, name='detail'),
]