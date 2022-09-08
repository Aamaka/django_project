from django.urls import path
from . import views

app_name = 'my_app'
urlpatterns = [
    path('', views.index, name='redirect_to_about'),
    path('redirect/', views.redirect),
    path('about/', views.about, name='about')
]