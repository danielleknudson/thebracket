from django.shortcuts import render
from django.views.generic.base import TemplateView


class LandingScreen(TemplateView):
    template_name = 'landing.xml'


class LoginScreen(TemplateView):
    template_name = 'login.xml'


class SignupScreen(TemplateView):
    template_name = 'signup.xml'