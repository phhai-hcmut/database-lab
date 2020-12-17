 

from django.urls import path

from . import views

urlpatterns = [
    path('', views.searchView, name='search'),
    path('search_result/', views.SearchResultView.as_view(), name='search-results'),
]
