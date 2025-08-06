from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse   # 요청에 대한 응답 
from .models import Question 

# /pybo 페이지에 띄울 index 함수 
# request : HTTP 요청 객체 
# def index(request):
#     return HttpResponse('pybo')



def index(request):
    question_list = Question.objects.order_by('-create_date')  # 최신 질문 순으로 정렬
    context = {'question_list': question_list}  # 템플릿에 전달할 데이터
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # 질문 ID로 질문 객체 가져오기
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)  # 질문 상세 페이지 렌더링

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())  # 답변 생성
    answer.save()
    
    return redirect('pybo:detail', question_id=question.id)  # 답변 후 질문 상세 페이지로 리다이렉트
    
    # redirect 함수는 페이지 이동을 위한 함수로, pybo:detail 별칭에 해당하는 페이지로 이동하기 위해 사용