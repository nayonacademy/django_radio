from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import *


class Index(View):
    template_name = 'color.html'
    form_class = ColorForm
    def get(self, request):
        # <view logic>
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': self.form_class})


class MyCaps(View):
    template_name = 'mycaps.html'
    form_class = MyCapsForm
    def get(self, request):
        color = Color.objects.all()
        # <view logic>
        return render(request, self.template_name, {'form': self.form_class, 'cls': color})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': self.form_class})

