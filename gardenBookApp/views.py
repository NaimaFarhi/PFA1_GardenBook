from django.shortcuts import render,redirect
from .forms import*
from .models import Livre
# Create your views here.

def book_list(request):
    context = {'book_list':Livre.objects.all()}
    return render(request,"books/book_list.html",context)
   

def book_form(request,ISBN=0):
    if request.method == "GET":
        if ISBN == 0 :
          form = LivreForm()
        else:
           Livre = Livre.objects.get(pk=ISBN)
           form = LivreForm(instance=Livre)
        return render(request,"books/book_form.html",{'form':form})
    else:
        if ISBN == 0 : 
           form = LivreForm(request.POST)
        else : 
            Livre = Livre.objects.get(pk=ISBN)
            form = LivreForm(request. POST,instance=Livre)
        if form.is_valid():
         form.save()
         return redirect("/list")

def book_delete(request):
    return


