from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
]


# def home(request):
#     return HttpResponse('<h1> blog home</h1>')