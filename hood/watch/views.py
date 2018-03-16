from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Welcome to Neighbourhood watch'

    return render (request , 'index.html')