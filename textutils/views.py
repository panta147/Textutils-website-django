
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'first.htm')

def analyzer(request):
    text=request.GET.get('text','Default')
    removep=request.GET.get('removep','off')
    lower=request.GET.get('lower','off')
    capitalize=request.GET.get('capitalize','off')
    change=request.GET.get('change','off')
    upper=request.GET.get('upper','off')
    newline=request.GET.get('newline','off')
    extraspace=request.GET.get('extraspace','off')
    count=request.GET.get('count','off')
    if removep=="on":
        analyzed=""
        punctuation='!@#$%^&*()-+/":|{}[]<>.,?''"";'
        for char in text:
            if char not in punctuation:
                analyzed=analyzed+char

        params={'analyzed_text':analyzed,'purpose':"Remove Punctuation"}
        text=analyzed
     
    if upper=='on':
        analyzed=""
        for char in text:
            analyzed=analyzed+char.upper() 
        params={'analyzed_text':analyzed,'purpose':"Change The Charracter Into UpperCase"}
        text=analyzed
        
    if newline=='on':
        analyzed=""
        for char in text:
            if char!="\n" and char!="\r" :
                analyzed=analyzed+char
            else:
                pass   
        params={'analyzed_text':analyzed,'purpose':"Remove NewLine"}
        text=analyzed
        
    if extraspace=='on':
        analyzed=" "
        for index,char in enumerate(text):
            if not (text[index]==" " and text[index+1]==" "):
                    analyzed=analyzed+char
        params={'analyzed_text':analyzed,'purpose':"Remove Punctuation"}
        text=analyzed
                     
    if count=='on':
        count=0
        for char in text:
            count=count+1
        params={'analyzed_text':count,'purpose':"Count The Total Character"}
        text=analyzed
     
    if change=='on':
        analyzed=''
        for char in text:
            if char>="A" and char<="Z" :
                analyzed=analyzed+char.lower()
            elif char>="a" and char<="z":
                analyzed=analyzed+char.upper()
            else:
                analyzed=analyzed+char

        params={'analyzed_text':analyzed,'purpose':"Change the Case of the character"}
        text=analyzed          
    if lower=='on':
        analyzed=''
        for char in text:
            analyzed=analyzed+char.lower()
        params={'analyzed_text':analyzed,'purpose':"Change Character into LowerCase"}
        text=analyzed
          

    if capitalize=='on':
        analyzed=''
        for index,char in enumerate(text):
            if index==0:
                analyzed=analyzed+char.upper()
            else: 
                analyzed=analyzed+char   
        params={'analyzed_text':analyzed,'purpose':"capitalized the word"}
        text=analyzed
    return render(request,'analyze.htm',params)                                  
    if capitalize!='on' and lower!='on'and upper!='on'and change!='on' and count!='on' and extraspace!='on'and newline!='on'and  removep!="on":
        return HttpResponse("..ERROR..")    
 
     
          