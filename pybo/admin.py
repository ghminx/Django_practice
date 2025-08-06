from django.contrib import admin
from .models import Question, Answer

# Register your models here.

# 관리자 화면에서 제목(subject)으로 질문 데이터를 검색하기 위한 클래스
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'content', 'create_date')  # 목록에 보여줄 필드
    search_fields = ['content']                                  # 검색 가능 필드
    list_filter = ['create_date']                                # 오른쪽 필터
    ordering = ['-create_date']                                  # 기본 정렬
    # readonly_fields = ['create_date']                            # 읽기 전용 필드

admin.site.register(Question, QuestionAdmin)                    # Question 모델을 관리자 화면에 등록
admin.site.register(Answer, AnswerAdmin)                        # Answer 모델을 관리자 화면에 등록