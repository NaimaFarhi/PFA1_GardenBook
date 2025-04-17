
from django.urls import path,include
from .views import book_list,book_form,register,login_view,home, users, register_person,custom_logout_view
urlpatterns = [
   
    path('login/',login_view,name='login'),
     path('register/', register, name='register'),
    path('home/',home,name='home'),
    path('addbook/',book_form,name='addbook'),
    path('book_list/',book_list,name="book_list"),
    path('<int:id>/',book_form,name="book_edit"),
    path('users-list', users, name="users-list"),
  path('create-user', register_person, name="create-user"),
     path('logout/', custom_logout_view, name='logout'),
]
