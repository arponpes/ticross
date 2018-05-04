from django import forms
from django.forms import ModelForm, SelectMultiple, TextInput, Textarea
from core.models import Project
from django.contrib.auth.models import User


class TimeSelectMultiple(SelectMultiple):
    template_name = 'forms/selectBootstrap.html'


class ProjectForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(), widget=TimeSelectMultiple)

    class Meta:
        model = Project
        fields = ['user']