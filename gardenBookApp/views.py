from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,LivreForm
from .models import Livre, User
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



def custom_logout_view(request):
    logout(request)  # This clears the session
    return redirect('login')  # Redirect to login page or homepage

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
@login_required
def book_list(request):
    context = {'book_list':Livre.objects.all()}
    return render(request,"books.html",context)
   
@login_required
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
        
@login_required
def book_delete(request):
    return
@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def users(request):
  users = User.objects.all()
  context = {'users': users}
  return render(request, 'users.html', context)
@login_required
def register_person(request):
  form = CustomUserCreationForm()
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('users-list')
  
  context = {'form' : form}
  return render(request, 'addUser.html', context)
