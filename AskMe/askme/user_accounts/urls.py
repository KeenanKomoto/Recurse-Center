from  django.urls import path
from . import views

app_name = 'user_accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('homepage/', views.homepage, name='homepage'),
    path('settings/', views.settings, name='settings'),
]
