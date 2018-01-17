from django.shortcuts import render

def homepage(request):
    return render(request, 'product/homepage.html',{})
