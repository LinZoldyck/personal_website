from django.urls import path
from . import views
app_name ='blog'
urlpatterns = [
     path('', views.index, name='index'),
     path('new', views.create, name='article_new'),
     path('view/<int:pk>', views.detail, name='article_view'),
     path('update/<int:pk>', views.update, name='article_update'),
     path('delete/<int:pk>', views.delete, name ='article_delete'),
 ]