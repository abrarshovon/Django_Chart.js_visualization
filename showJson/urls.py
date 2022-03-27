from django.urls import path
from . import views
from .views import JsonListView,JsonDetailView,JsonCreateView,JsonUpdateView,JsonDeleteView
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('json/', JsonListView.as_view(),name='jsonlist' ),
    path('jsondetail/<int:pk>', JsonDetailView.as_view(), name='jsondetail'),
    path('jsonlist/add/', JsonCreateView.as_view(), name='jsoncreate'),
    path('jsonupdate/<int:pk>', JsonUpdateView.as_view(), name='jsonupdate'),
    path('jsondelete/<int:pk>', JsonDeleteView.as_view(), name='jsondelete'),

   
]