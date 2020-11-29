from django.shortcuts import render
from django.http import HttpResponse
from .models import Words

# Create your views here.
def wordlist(request):
    if request.method=='POST':
        noun = request.POST.get('noun', '')
        adjective = request.POST.get('adjective', '')
        place = request.POST.get('place', '')
        expression = request.POST.get('expression', '')
        words = Words(noun=noun, adjective=adjective, place=place, expression=expression)
        words.save()
    return render(request, 'views/form.html')