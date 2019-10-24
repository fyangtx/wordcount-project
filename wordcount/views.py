from django.http import HttpResponse
from django.shortcuts import render
import operator
import re

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = re.split(' ', fulltext)
    worddictinary = {}
    for word in wordlist:
        
        if word in worddictinary:
            wrd = word.strip(',.-') #remove puntuations
            worddictinary[wrd] += 1
        else:
            wrd = word.strip(',.-')
            worddictinary[wrd] = 1

    sortedword = sorted(worddictinary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddictionary':sortedword})

def about(request):
    return render(request, 'about.html')
