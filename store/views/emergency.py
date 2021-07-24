from django.views import View
from django.shortcuts import render, redirect


class Emergency(View):
    def get(self, request):
        return render(request, 'emergency.html')