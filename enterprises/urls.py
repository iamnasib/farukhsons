from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('about', views.About,name='about'),
    path('contact', views.Contact,name='contact'),
    path('gallery', views.Gallery,name='gallery'),
    path('boss', views.Boss,name='boss'),
    path('create', views.CreateInvoice,name='create'),
    path('view/<int:invoice_id>', views.ViewInvoice,name='view'),
    path('delete/<int:invoice_id>', views.DeleteInvoice,name='delete'),
    path("__reload__/", include("django_browser_reload.urls")),
]