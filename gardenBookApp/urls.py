
from django.urls import path,include
from .views import book_list,book_form,registerPage,loginPage
urlpatterns = [
    path('register/',registerPage,name='register'),
    path('login/',loginPage,name='login'),
    path('',book_form,name="book_insert"),
    path('list/',book_list),
    path('<str:ISBN>/',book_form,name="book_edit")

]
