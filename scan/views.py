from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.contrib import messages

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'scan/index.html'

    def post(self, request):
        data = request.POST
        return redirect(reverse('scan:index'))

    def get(self, request):
        return super(IndexView, self).get(request)
