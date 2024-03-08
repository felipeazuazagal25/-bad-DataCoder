from django import forms
from core.models import Course, Test, Question, Student, TestDate
from authentication.models import User
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields=['shortname','fullname','semester']

class TestForm(forms.ModelForm):
    class Meta:
        model = Test   
        fields = ['testName','rubric']

class TestQuestionsMassiveForm(forms.Form):
    testName = forms.CharField(max_length=64)
    rubric = forms.FileField()
    questions = forms.FileField()


class StudentForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    
    
class TestDateForm(forms.Form):
    test = forms.ModelChoiceField(queryset=Test.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    testdate = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local'}))


class ValidateCodeForm(forms.Form):
    code = forms.SlugField(max_length=16)


class AnswersForm(forms.Form):
    answers_excel = forms.FileField()