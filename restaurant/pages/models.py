from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError
# Create your models here.

class Messages(models.Model):
    name = models.CharField(max_length=255,default='')
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2555)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.name
    
    class Meta:	
        db_table = 'messages'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'email','subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Name"}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter Email"}),
            'subject': forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Subject"}),
            'message': forms.Textarea(attrs={'class':'form-control'}),
        }