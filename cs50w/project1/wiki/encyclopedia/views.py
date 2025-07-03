from django.shortcuts import render,redirect
from django.contrib import messages

from . import util
import markdown
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    c=util.get_entry(title)
    if not c:
        for n in util.list_entries():
            if title.lower()==n.lower():
                return redirect('encyclopedia:entry', title=n)
        return render(request, "encyclopedia/error.html",{
            "error":title,
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "body":  markdown.markdown(c)
    })

def query(request):
    q = request.GET.get('q', '').strip()
    arr=[]
    for n in util.list_entries():
        if q.lower()==n.lower():
            return redirect('encyclopedia:entry', title=n)
        if q.lower() in n.lower():
            arr.append(n)
    return render(request, "encyclopedia/results.html", {
        "q": q,
        "results": arr
    })

def randompage(request):
    random_item = random.choice(util.list_entries())
    return redirect('encyclopedia:entry', title=random_item)

def create(request):
    if request.method == "POST":
        title = request.POST.get("newtitle")
        body = request.POST.get("newbody")
        for n in util.list_entries():
            if title.lower()==n.lower():
                return render(request, "encyclopedia/create.html",{
                    "title":title,
                    "body":body,
                    "error": f"The page '{title}' already exists."
                })
        util.save_entry(title, body)
        return redirect('encyclopedia:entry', title=title)
    else:
        return render(request, "encyclopedia/create.html",)

def edit(request, title):
    if request.method=="POST":
        body = request.POST.get("newbody")
        util.save_entry(title, body)
        return redirect('encyclopedia:entry', title=title)
    else:
        body = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title":title,
            "body":body,
        })
