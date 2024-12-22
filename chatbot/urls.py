from django.urls import path
from chatbotapp.views import send_message, list_messages
from chatbotapp import views


urlpatterns = [
    path('send', views.send_message, name='send_message'),
    path('', views.list_messages, name='list_messages'),
    path('clear_chat/', views.clear_chat, name='clear_chat'),  # Added clear chat path
]