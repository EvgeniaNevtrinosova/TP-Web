# from django.views.generic import TemplateView
#
#
# class AboutView(TemplateView):
#     template_name = "about.html"
from django.http import HttpResponse

from django.shortcuts import render

def about(request):
    return render(request, "questions/about.html")

def get_post(request):
    return HttpResponse(request.GET.urlencode())