from cProfile import label
from secrets import choice
from attr import fields
from django import forms
from matplotlib import widgets
from numpy import number
from .models import *;
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter Your Search :")