from  django.urls import path
from . import views

app_name = 'user_accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]
