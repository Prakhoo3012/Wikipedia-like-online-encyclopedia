from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    t = util.get_entry(name)
    if(t != None):
        template = loader.get_template('encyclopedia/Django.html')
        context = {
            "title": name,
            "text": t
        }
    else:
        template = loader.get_template('encyclopedia/error.html')
        context = {
            "title": name
        }
    return HttpResponse(template.render(context, request))

def search(request):
    n1 = request.GET.get('q')
    try:
        t = util.get_entry(n1)
        if(t != None):
            template = loader.get_template('encyclopedia/Django.html')
            context = {
                "title": n1,
                "text": t
            }
        else:
            template = loader.get_template('encyclopedia/search.html')
            entries = util.list_entries()
            SearchResult = []
            for entry in entries:
                x = entry.find(n1)
                if x != -1:
                    SearchResult.append(entry)

            context = {
                "title": n1,
                "list": SearchResult
            }
        return HttpResponse(template.render(context, request))
    except:
        pass

def searchByname(request, name):
    t = util.get_entry(name)
    if(t != None):
        template = loader.get_template('encyclopedia/Django.html')
        context = {
            "title": name,
            "text": t
        }
    else:
        template = loader.get_template('encyclopedia/error.html')
        context = {
            "title": name
        }
    return HttpResponse(template.render(context, request))

def create(request):
    return render(request, "encyclopedia/create.html")

def add_entry(request):
    n1 = request.GET.get('title')
    n2 = request.GET.get('content')
    mylist = util.list_entries()
    for entry in mylist:
        if entry == n1:
            template = loader.get_template('encyclopedia/already_exit.html')
            context = {
                "title": "Already exits",
            }
            return HttpResponse(template.render(context, request))
    util.save_entry(n1, n2)
    t = util.get_entry(n1)
    template = loader.get_template('encyclopedia/Django.html')
    context = {
        "title": n1,
        "text": t
    }
    return HttpResponse(template.render(context, request))


def randomly(request):
    myList = util.list_entries()
    q = random.choice(myList)
    template = loader.get_template('encyclopedia/Django.html')
    context = {
        "title": q,
        "text": util.get_entry(q)
    }
    return HttpResponse(template.render(context, request))

def edit(request):
   return render(request, "encyclopedia/edit.html", {
        "entries": util.list_entries()
    })

def editpage(request):
    t = request.GET.get('title')
    q = util.get_entry(t)
    template = loader.get_template('encyclopedia/editpage.html')
    context = {
        "title": t,
        "text": q
    }
    return HttpResponse(template.render(context, request))

def update_entry(request):
    n1 = request.GET.get('title')
    n2 = request.GET.get('content')
    util.save_entry(n1, n2)
    t = util.get_entry(n1)
    template = loader.get_template('encyclopedia/Django.html')
    context = {
        "title": n1,
        "text": t
    }
    return HttpResponse(template.render(context, request))

