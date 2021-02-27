from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from pages.models import Messages, MessagesForm
from django.views.generic.edit import FormView, CreateView


class home(TemplateView):
    template_name="home.html"
    
class menu(TemplateView):
    template_name="menu.html"

class about(TemplateView):
    template_name="about.html"

class timing(TemplateView):
    template_name="timing.html"

class contact(TemplateView):
    template_name="contact.html"

class index(FormView):
    template_name = "index.html"
    form_class = MessagesForm
    success_url = '/'

class add(CreateView):
    form_class = MessagesForm
    template_name = 'contact.html'
    success_url = "/"

    
