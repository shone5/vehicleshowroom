from django.urls import path
from Frontend import views

urlpatterns = [
    path('index_page/', views.index_page, name='index_page'),
    path('chatbox/', views.chatbox, name='chatbox'),


]
