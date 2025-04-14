from django.shortcuts import render,redirect
<<<<<<< HEAD
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
=======
from .forms import CustomUserCreationForm,LivreForm
from .models import Livre
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

#    START INSCRIPTION

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data) 
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrationForm.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def book_list(request):
    context = {'book_list':Livre.objects.all()}
    return render(request,"books.html",context)
>>>>>>> 7f89e379592479be3285f73d3f91592274217ed7
   

def book_form(request, id=0):
    if request.method == "GET":
       
        if id == 0:
            form = LivreForm()
        else:
           
            book = get_object_or_404(Livre, pk=id)
            form = LivreForm(instance=book)
        return render(request, "addBook.html", {'form': form})

    else:
        if id == 0:
           
            form = LivreForm(request.POST)
        else:
      
            book = get_object_or_404(Livre, pk=id)
            form = LivreForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            
            print(form.errors)
            return render(request, "addBook.html", {'form': form})
        

def book_delete(request):
<<<<<<< HEAD
    return """

#Display all the users
def display_user(request):
   users = User.objects.all()
   context = {'users': users}
   return render(request, '../templates/users.html', context)

=======
    return
@login_required
def home(request):
    return render(request, 'home.html')
>>>>>>> 7f89e379592479be3285f73d3f91592274217ed7


