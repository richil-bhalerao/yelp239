from django import forms
import datetime

class CourseForm(forms.Form):
    Categories=(('1','Software Engineering'),('2','Computer Engineering'),('3','Electrical Engineering'))
    category = forms.ChoiceField(choices=Categories)
    title = forms.CharField()
    Sections=(('1','Section 1'),('2','Section 2'))
    section= forms.ChoiceField(choices=Sections)
    Departments=(('1','SE'),('2','CE'),('3','EE'))
    dept=forms.ChoiceField(choices=Departments)
    term=forms.CharField()
    year=forms.CharField()
    instructorname=forms.CharField()
    instructoremail=forms.CharField()
    days=forms.CharField()
    hours=forms.CharField()
    description=forms.CharField()
    attachment=forms.CharField()
    version=forms.CharField()
    
