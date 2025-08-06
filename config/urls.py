"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include   # include를 사용하면 별도로 불러오지 않아도됨

# # 새로운 페이지 추가
# from pybo import views   # 앱별 매핑을 개별로 하는건 권장되지 않음 

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("pybo/", views.index),   # pybo 폴더의 view.py에서 index 함수
    
# ]

# 권장 방법 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),   # pybo/로 시작하는 페이지를 요청하면 이제 pybo/urls.py 파일의 매핑 정보를 읽어서 처리하라는 의미
]                                          # pybo/로 시작하는 URL을 추가해야 할 때 config/urls.py 파일을 수정할 필요없이 pybo/urls.py 파일을 생성하여 수정하면 됨