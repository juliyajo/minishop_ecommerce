from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:c_slug>/',views.index,name='pro_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.details,name='detail'),
    path('search',views.search,name='Search'),
    path('about',views.about,name='About'),
    path('blog',views.blog,name='Blog'),
    path('contact',views.contact,name='Contact'),


]
