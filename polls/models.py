from email.policy import default
from tkinter import CASCADE
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    date_pub = models.DateTimeField('date published: ')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.models.IntegerField(default=0)