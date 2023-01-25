from django.shortcuts import render, redirect
from django.contrib import messages



# Create your views here.
def index_page(request):
    return render(request, 'index.html')
def chatbox(request):
    return render(request, 'chat.html')