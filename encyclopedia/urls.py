from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>',views.entrypage,name='entrypage'),
    path('search',views.search,name='search'),
    path('newentry',views.newentry,name='newentry'),
    path('editpage/<str:title>',views.editpage,name='editpage'),
    path('randompage',views.randompage,name='randompage')
]
