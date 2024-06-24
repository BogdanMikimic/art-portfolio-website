from django.urls import path
from . import views

urlpatterns = [
            path('', views.homepage, name='home'),
            path('categories/', views.categories, name='categories'),
            path('category/<str:categorie>', views.category, name='category'),
            path('painting/<int:id_pictura>', views.pictura, name='pictura'),
            path('aboutme/', views.aboutme, name='aboutme'),
            path('contact/<int:question>', views.contact, name='contact'),    

]
