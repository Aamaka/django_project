from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    # path('', views.index, name='redirect_to_about'),
    # path('redirect/', views.redirect),
    # path('about/', views.about, name='about'),
    path('book-list/', views.BookList.as_view(), name='book-list'),
    # path('book-detail/<int:pk>/', views.book_detail, name='book-detail'),
    path('book-detail/<int:pk>/', views.BookDetails.as_view(), name='book-detail'),
    path('publishers/', views.PublisherList.as_view(), name='publisher'),
    path('publisher_details/<int:pk>/', views.PublisherDetails.as_view(), name='publisher_details'),
]

