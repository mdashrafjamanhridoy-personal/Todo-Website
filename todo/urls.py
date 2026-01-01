from django.urls import path
from . import views


urlpatterns = [
    path('',views.signUp,name='signup'),
    path('logIn/',views.logIn,name='logIn'),
    path('TodoPage/',views.TodoPage,name='TodoPage')
]
