from django.shortcuts import render

# Create your views here.
from app.models import*
from django.http import HttpResponse
def insert_topic(request):
    tn= input('enter topic name')
    tod=Topic.objects.get_or_create(topic_name=tn)
    if tod[1]:
        LTO=Topic.objects.all()
        d={'LTO':LTO}
        return render(request,'display_topics.html',d)
        # return HttpResponse('new topic is create')
    else:
        return HttpResponse('Given Topic is already present')
    
    
def insert_WebPage(request):
    tn=input("enter topic name")
    n= input('enter name')
    url=input('enter url')
    email=input('enter Email')
    LTO= Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WTOD=WebPage.objects.get_or_create(topic_name=TO,name=n,url=url,email=email)
        if WTOD[1]:
            LWO=WebPage.objects.all()
            d={'LWO':LWO}
            return render(request,'display_web.html',d)
            # return HttpResponse('webpage is created')
        else:
            return HttpResponse('Webpage is not created')
    else:
        return HttpResponse('Given Topic is not Present')
    
def insert_AcessRecods(request):
    pk=int(input('enter pk of webpage'))
    author=input('enter author')
    date=input('enter date')
    LWO=WebPage.objects.filter(pk=pk)
    if LWO:
        WO=LWO[0]
        ATOD=AcessRecods.objects.get_or_create(name=WO,author=author,date=date)
        if ATOD[1]:
            LAO=AcessRecods.objects.all()
            d={'LAO':LAO}
            return render(request,'display_Acess.html',d)
            # return HttpResponse('new Access is created')
        else:
            return HttpResponse('with Given details access is already present')
    else:
        return HttpResponse('given parent Webpage Table data is not present in DB')
        
    





def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)



def display_web(request):
    LWO=WebPage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_web.html',d)
    
def display_acess(request):
    LAO=AcessRecods.objects.all()
    d={'LAO':LAO}
    return render(request,'display_Acess.html',d)
