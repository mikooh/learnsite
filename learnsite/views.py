from django.http import HttpResponse  # this is basically just some django code, that allows us to very simply return back, some information as HTTP response. we can essentially send back the 'hello' below.
from django.shortcuts import render
import operator


# def home(request):
#     return HttpResponse('Hello')  # just returning 'hello' won't work because we can't just send a string. we need to send an HTTP response. we can also directly write html instead of 'Hello'. for e.g. return HttpResponse(<h1>'Hello'</h1>) and this would work.

def home(request):
    return render(request, 'home.html')  # render... first argument request takes in the parameter and second is the path to the template where we want to send the user after the request.


def count(request):
    fulltext = request.GET['fulltext']  # .get will pull the information provided in the 'fulltext'. and then we assign it to fulltext variable.
    # print(fulltext)  # and this print will show up in the terminal/command prompt.
    wordlist = fulltext.split()  # split() breaks the sentence into a list of words, by identifying the spaces.

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word] += 1
        else:
            # add word to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)  # .items will turn a dictionary key:value pair into one item in the list... ultimately a list with key value pairs stored like [(name, shridhar), (height, 180)]. also operator needs to be imported.

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})  # here in the curly brackets... 'fulltext' refers to the variable that we will pass in our count.html page... and then it will display the value contained in the fulltext which is written after the :. here, fulltext is a variable that contains the value of that we got from the URL through .get.


def about(request):
    return render(request, 'about.html')
