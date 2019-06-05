from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text = request.GET['fulltext']
    words=text.split()
    sentenses=text.split('\n')
    sentenses=text.split('\r')
    word_dictionary={}
    sentense_dictionary={}
    for word in words :
        if word in word_dictionary:
            word_dictionary[word]+=1
        else :
            word_dictionary[word]=1

    for sentense in sentenses :
        if sentense in sentense_dictionary:
            sentense_dictionary[sentense]+=1
        else:
            sentense_dictionary[sentense]=1


    return render(request,'result.html',{'full' : text,'total' : len(words),'dictionary' : word_dictionary.items(),'total_s':len(sentenses),'s_dictionary':sentense_dictionary.items()})