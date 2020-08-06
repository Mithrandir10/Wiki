from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . import util
from markdown2 import Markdown
import os.path
import random
from django.urls import reverse

def index(request):
    if request.method=='POST':
        srch=request.POST.get('q',None)
        chk=0
        sbstr=[]
        for i in util.list_entries():
            if(i.lower()==srch.lower()):
              chk=1
              f=util.get_entry(srch)
              conv=Markdown().convert(f)
              return render(request,"encyclopedia/entry.html",{
                  "entry":conv,"title":srch
              })
        for i in util.list_entries():
            if((srch.lower() in i.lower()) and chk!=1):
                chk=2
                sbstr.append(i)
        if(chk==2):
            return render(request,"encyclopedia/search.html",{
                "substr":sbstr
            })

        if (chk==0):
           return render(request, "encyclopedia/notfound.html")
    if request.method=='GET':
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),"rand":random.choice(util.list_entries())
         })

def entry(request, a):
    
      f=util.get_entry(a)
      if f==None:
        return render(request, "encyclopedia/notfound.html")
      conv=Markdown().convert(f)

      return render(request, "encyclopedia/entry.html",{
        "entry":conv,"title":a
       })

    

def new_page(request):
    if request.method=='POST':
        tmptitle=request.POST.get('title',None)
        print(tmptitle)
        tmpcont=request.POST.get('content',None)
        print(tmpcont)
        util.save_entry(tmptitle,tmpcont)
    return render(request,"encyclopedia/newentry.html",{
        "entries": util.list_entries(),"rand":random.choice(util.list_entries())
    })

def edit_page(request, x):
    f=util.get_entry(x)
    if request.method=='POST':
        tmptitle=request.POST.get('title',None)
        print(tmptitle)
        tmpcont=request.POST.get('content',None)
        print(tmpcont)
        util.save_entry(tmptitle,tmpcont)
        return HttpResponseRedirect(reverse('entry',args=(tmptitle,)))
    return render(request,"encyclopedia/edit.html",{
        "content":f,"title":x
    })