from django.urls import path
from . import views

app_name = 'conversation'
urlpatterns = [
    path('', views.inbox, name = 'inbox'),
    path('<int:pk>/', views.detail_conversation, name='detail_conversation'),
    path('new/<int:item_pk>/', views.new_conversation, name = 'new_conversation'),
]
