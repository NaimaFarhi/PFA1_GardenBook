from django.shortcuts import render,redirect
from .forms import*
from .models import Livre, User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
""" def registerPage(request):
   form = CreateUserForm()

   if request.method == 'POST':
      form = CreateUserForm()
      if form.is_valid():
         form.save()
   
   context = {'form':form}
   return render(request,'registrationForm.html',context)

def loginPage(request):
   context = {}
   return render(request,'login.html',context)

def book_list(request):
    context = {'book_list':Livre.objects.all()}
    return render(request,"templates/books.html",context)
   

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
    return """

#Display all the users
def display_user(request):
   users = User.objects.all()
   context = {'users': users}
   return render(request, '../templates/users.html', context)



