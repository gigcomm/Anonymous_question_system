from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=30, null=True,blank=True)
    question_answer = models.CharField(max_length=40,null=True, blank=True)
    count_of_answers = models.IntegerField(blank=True, null=True)