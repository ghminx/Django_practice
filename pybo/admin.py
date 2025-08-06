from django.contrib import admin
from .models import Question

# Register your models here.

# 관리자 화면에서 제목(subject)으로 질문 데이터를 검색하기 위한 클래스
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    
admin.site.register(Question)