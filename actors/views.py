from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.
def movies(request):
    return render(request, 'bolly_adda.html')

def directors(request):
    return render(request, 'entertainment.html')

def producers(request):
    return render(request, 'prd_team.html')

def cameraman(request):
    return render(request, 'shooting.html')