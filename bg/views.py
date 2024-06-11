from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ShowIndex(TemplateView):
    template_name = 'bg/index.html'


class ShowContact(TemplateView):
    template_name = 'bg/contact.html'


class ShowAbout(TemplateView):
    template_name = 'bg/about.html'


class ShowServices(TemplateView):
    template_name = 'bg/services.html'


