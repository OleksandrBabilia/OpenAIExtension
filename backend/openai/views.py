from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

import json

def index(request):
    return HttpResponse("Hello, world!")

def get_openai_summary(request):
    topic = request.GET.get('topic', None)
    
    print(f'topic: {topic}')
    
    return JsonResponse({
        'ok': True,
        'data': topic
    })