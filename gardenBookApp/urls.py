
from django.urls import path,include
<<<<<<< HEAD
from . import views # book_list,book_form,registerPage,loginPage, 
urlpatterns = [
    #path('register/',registerPage,name='register'),
    #path('login/',loginPage,name='login'),
    #path('',book_form,name="book_insert"),
    #path('list/',book_list),
    #path('<str:ISBN>/',book_form,name="book_edit"),

    path('users-list', views.display_user, name="users-list"),
=======
from .views import book_list,book_form,register,login_view,home
urlpatterns = [
   
    path('login/',login_view,name='login'),
     path('register/', register, name='register'),
    path('',home,name='home'),
    path('addbook/',book_form,name='addbook'),
    path('book_list/',book_list,name="book_list"),
    path('<int:id>/',book_form,name="book_edit")
    
>>>>>>> 7f89e379592479be3285f73d3f91592274217ed7

]
