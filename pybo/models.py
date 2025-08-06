from django.db import models

# Create your models here.

# 질문 모델 
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 질문의 제목 CharField(길이가 제한된 텍스트)
    content = models.TextField()                # 질문의 내용 TextField(글자수에 제한이 없는 텍스트)
    create_date = models.DateField()            # 작성 일시   DateField(날짜/시간)
    
    def __str__(self):
        return self.subject  # 질문 객체를 문자열로 표현할 때 제목(subject)을 반환

# 답변 모델
class Answer(models.Model):
    
    # ForeignKey : 기존 모델을 속성으로 연결  on_delete : Answer이 연결된 Question이 삭제되면 같이 삭제)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 질문 (어떤 질문의 답변인지 알아야 하므로 질문 속성 필요)
    content = models.TextField()                 # 질문의 내용 
    create_date = models.DateField()             # 작성 일시                         

    def __str__(self):
        return self.content  # 답변 객체를 문자열로 표현할 때 내용(content)을 반환
