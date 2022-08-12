from django.urls import path
from .import views


urlpatterns = [
 path("", views.callpage, name='loginpage'),
 path("signuppage/", views.callsingup, name='signuppage'),
 path("head_foot/", views.callheadfoot, name='head_foot'),
 path("check_t/", views.callchecktest, name='check_test'),
]