from django.contrib import admin
from django.urls import path,include
from game import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),

    path('loginRegisterPage/', views.loginRegisterPage, name='loginRegisterPage'),

    path('mytodos/', views.mytodos, name='mytodos')
]
