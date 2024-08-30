from django.db import models

# Create your models here.



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


'''The name of each Field instance 
(e.g. question_text or pub_date) 
is the field's name, in machine-friendly format. 
You'll use this value in your Python code, 
and your database will use it as the column name. hihi

bohot mushkil sa lag rha but we will NOT BACK DOWN
CAUSE NEVER BACK DOWN NEVER WHAT?
NEVER GIVE UPPPPPPP'''