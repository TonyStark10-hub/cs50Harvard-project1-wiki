from django.shortcuts import render,redirect
import re
import random


from . import util
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entrypage(request,title):
    if title not in util.list_entries():
        return render(request,"encyclopedia/error.html",{
            'message':'Searched topic is not available in database'
        })
    else:
        mkcontent=util.get_entry(title)
        if mkcontent:
            htmlcontent=markdown2.markdown(mkcontent)
            return render(request,'encyclopedia/entrypage.html',{
                'htmlcontent':htmlcontent,
                'title':title
            })
        else:
            return render(request,"encyclopedia/error.html")
def search(request):
    if request.method== 'POST':
        data=request.POST
        data=data['q']
        results=[]

        for entry in util.list_entries():

            if re.search(data.lower(),entry.lower()):
                results.append(entry)
        if len(results)==0:
            return render(request,'encyclopedia/error.html',{
                'message':'search result not found' 
            })
        else:    
            return render(request,'encyclopedia/search.html',{
                "results":results
            })
def newentry(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')

        if title in util.list_entries():
            return render(request,'encyclopedia/newentry.html',{
                'available':True
            })
        else:
            util.save_entry(title,content)
            return redirect(newentry,title=title)
    else:
        return render(request,'encyclopedia/newentry.html',{
            'available':False
        })
def editpage(request,title):
    content=util.get_entry(title)
    if request.method=='GET':
        return render(request,'encyclopedia/editpage.html',{
            'title':title,
            'content':content
        })
    if request.method=='POST':
        content=request.POST.get('newcontent')
        util.save_entry(title,content)
        return redirect(entrypage,title)
def randompage(request):
    lst=util.list_entries()
    randomentry=random.choice(lst)
    return redirect(entrypage,randomentry)




