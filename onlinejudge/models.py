from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime


# Create your models here.
class Problem(models.Model):
    problem_id = models.CharField(max_length=30, primary_key=True)
    problem_title = models.CharField(max_length=30)
    problem_statement = models.TextField()

    def __str__(self):
        return str(self.problem_id) + " : " + self.problem_statement[0:10]

class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete= models.CASCADE)
    time_of_submission = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    LANGUAGES = [['py','Python 3'],['cpp','C++']]
    language = models.CharField(max_length = 20, default = 'py', choices = LANGUAGES)

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['problem','code','language']


