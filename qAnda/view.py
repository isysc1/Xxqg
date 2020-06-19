"""
Created by Young on 2019/9/28 20:39
"""
import json
from django.shortcuts import render
import requests

seaNum = [448962]


def index(request):
    return render(request, "index.html", {"count": seaNum[0]});


def search(request):
    seaNum[0] = seaNum[0] + 1
    key_word = request.POST.get("question")
    url = 'https://api.deeract.com/l2s/api/questions?keyword=' + key_word
    result = requests.get(url)
    user_dict = json.loads(result.text)
    answer_id = []
    answer = []
    for i in user_dict:
        answer.append(i['title'])
    for j in range(len(answer)):
        answer_id_name = "title" + str(j)
        answer_id.append(answer_id_name)
    answer_context = dict(zip(answer_id, answer))
    return render(request, "result.html", {"answer_context": answer_context})
