"""
Created by Young on 2019/9/28 20:39
"""
import json

from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    return render(request, "index.html")


def search(request):
    keyWord = request.POST.get("question")
    url = 'https://api.deeract.com/l2s/api/questions?keyword=' + keyWord
    print(url)
    result = requests.get(url)
    user_dict = json.loads(result.text)
    answerId = ['title1', 'title2', 'title3', 'title4', 'title5', 'title6', 'title7']
    answer = []
    for i in user_dict:
        answer.append(i['title'])
    answerContext = dict(zip(answerId, answer))
    return render(request, "index.html", context=answerContext)


