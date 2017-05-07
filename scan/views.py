from django.shortcuts import render, reverse, redirect
from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'scan/index.html'

    def post(self, request):
        data = request.POST
        print data
        return redirect(reverse('scan:index'))
