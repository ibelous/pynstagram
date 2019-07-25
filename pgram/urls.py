from django.urls import path

from . import views

app_name = 'pgram'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('registration/', views.registration, name='registration'),
    path('user_login/', views.user_login, name='user_login'),
]
