from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donors/', views.donors, name='donors'),
    path('request/', views.request_blood, name='request'),
    path('add-donor/', views.add_donor, name='add_donor'),
    path('my-donors/', views.my_donors, name='my_donors'),
    path('emergency/', views.emergency_requests, name='emergency'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('emergency/', views.emergency_requests, name='emergency'),
    path('donor/edit/<int:id>/', views.edit_donor, name='edit_donor'),
    path('donor/delete/<int:id>/', views.delete_donor, name='delete_donor'),
    path('emergency/edit/<int:id>/', views.edit_request, name='edit_request'),
    path('emergency/delete/<int:id>/', views.delete_request, name='delete_request'),
]