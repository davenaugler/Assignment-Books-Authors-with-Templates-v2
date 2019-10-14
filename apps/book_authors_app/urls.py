from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.addBookPage),
    path('addnewbook/', views.addNewBook),
    path('authors/', views.addAuthorPage),
    path('addnewauthor/', views.addNewAuthor),
    path('books/<int:id>/', views.viewBook),
    path('viewauthoraddbook/', views.viewAuthorAddBook),
    path('authors/<int:id>/', views.viewAuthor),
    path('viewbookaddauthor/', views.viewBookAddAuthor)
]