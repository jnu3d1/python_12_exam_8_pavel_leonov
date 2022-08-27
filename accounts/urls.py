from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import *

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('create/', RegisterView.as_view(), name='create_user'),
]
