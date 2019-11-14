from django.urls import path
from . import views
# from django.contrib.auth.views as auth_views
urlpatterns = [
    path('chat/<int:user_id>/', views.index, name="home"),
    path('login/', views.login, name="login"),
    path('', views.login, name="login"),
]