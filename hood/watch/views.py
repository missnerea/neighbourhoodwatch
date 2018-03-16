from django.shortcuts import render

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    title = 'Welcome to Neighbourhood watch'

    return render (request , 'index.html')