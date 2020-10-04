from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def mainpage(request):
    return render(request, 'main.html', {'some_value':'text example'})

def health(request):
    return JsonResponse({'servername': 'lab server', 'random':1})