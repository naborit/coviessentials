from django.views import View
from django.shortcuts import render, redirect
from store.models.product import Product


class AboutUs(View):
    def get(self, request):
        return render(request, 'aboutus.html')

