"""
Created by Young on 2019/9/28 20:39
"""
import json
from django.shortcuts import render
import requests

list = [210]

def index(request):
    return render(request, "index.html")


def search(request):
    list[0] = list[0] + 1
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
    answerContext['countService'] = list[0]
    print(answerContext)
    return render(request, "index.html", answerContext)


