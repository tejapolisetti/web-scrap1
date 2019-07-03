# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from selenium import webdriver
from myapp.models import Movie
import json


# Create your views here.


def display(request):
    obj=list(c.all())
    titles=[]
    casts=[]
    ratings=[]
    movieids=[]
    return render(request,'myapp/display.html',{'q':obj})


def detail(request, movie_id):
    if(movie_id>1000 or movie_id<=0):
        return render(request,'myapp/display.html',{'q':[],'flag':0})
    obj=Movie.objects.filter(movie_id=movie_id)
    return render(request,'myapp/display.html',{'q':obj,'flag':1})


def prefix(request, prefix):
    obj=Movie.objects.all()
    ans=[]
    for i in obj:
        if(i.name.lower().find(prefix.lower())==0):
            ans.append(i)
    l=len(ans)
    if(len(ans)>5):
        ans=ans[:5]

    return render(request,'myapp/display.html',{'q':ans,'flag':l})



def search(request,string):
    obj=Movie.objects.all()
    ans=[]
    for i in obj:
        if(string.lower() in i.name.lower()):
            ans.append(i)
    l=len(ans)
    if(len(ans)>5):
        ans=ans[:5]
    return render(request,'myapp/display.html',{'q':ans,'flag':l})

def deep_search(request,string):
    obj=Movie.objects.all()
    ans=[]
    string=string.lower()
    for i in obj:
        p=i.name.lower()
        flag=0
        for j in string:
            if(j in p):
                k=p.find(j)
                p=p[k+1:]
            else:
                flag=1
                break
        if(flag==0):
            ans.append(i)
    l=len(ans)
    if(len(ans)>5):
        ans=ans[:5]
    return render(request,'myapp/display.html',{'q':ans,'flag':l})


def style(request):
    obj=Movie.objects.all()
    data=[]
    for i in obj:
        data.append([i.name,i.rating,i.cast])
    return render(request,'myapp/style.html',{"data":json.dumps(data)})






def data_push(request):
    driver=webdriver.Chrome('')
    driver.get("https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&ref_=adv_prv")
    count=0
    for i in range(10):
        temps=driver.find_elements_by_class_name('lister-item-content')
        for temp in temps:
            title=temp.find_element_by_class_name("lister-item-header")
            title=temp.find_element_by_tag_name("a")
            title=title.text
            rate=temp.find_element_by_class_name("ratings-imdb-rating")
            rate=rate.text
            casts=[]
            st=''
            cast=temp.find_elements_by_tag_name("p")
            cast=cast[2]
            cast=cast.find_elements_by_tag_name("a")
            for j in cast:
                casts.append(j.text)
                st+=j.text
                st+=','
            count+=1
            m=Movie(movie_id=count,name=title,rating=rate,cast=st)
            m.save()
        if(i==9):
            break
        btn=driver.find_element_by_class_name('next-page')
        btn.click()


    return render(request,'myapp/home.html')
