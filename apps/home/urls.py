from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('prueba/', views.PruebaView.as_view()),
    path('home1/', views.HomeTemplate1View.as_view()),
    path('home2/', views.HomeTemplate2View.as_view()),
    path('home3/', views.HomeTemplate3View.as_view()),
]
