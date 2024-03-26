"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('show_tests/', show_tests, name='show_tests'),
    path('show_categories/', show_categories, name='show_categories'),
    path('show_categories/<int:category_id>', show_tests, name='show_tests'),
    path('go_test/<int:test_id>', go_test, name='go_test'),
    path('results_test/', results_test, name='results_test'),
    path('registration/', user_registration, name='regis'),
    # path('login/', user_login, name='log_in'),
    path('logout/', user_logout, name='log_out'),
]