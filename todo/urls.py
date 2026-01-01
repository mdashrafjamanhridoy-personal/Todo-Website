from django.urls import path
from . import views


urlpatterns = [
    path('',views.signUp,name='signup'),
    path('logIn/',views.logIn,name='logIn'),
    path('TodoPage/',views.TodoPage,name='TodoPage'),
    path('edit_title/<int:id>/',views.edit_title, name="edit_title"),
    path('logout/', views.logout_view, name='logout'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),
]
