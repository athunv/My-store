from django.urls import path
from owner import views

urlpatterns = [

    path("home",views.Homeview.as_view()),
    path("register",views.Signupview.as_view()),
    path("login",views.SigninView.as_view()),
    path("product/add",views.ProductAddview.as_view())
    
    
]