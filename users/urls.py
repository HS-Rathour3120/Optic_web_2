# users/urls.py
from django.urls import path
from django.urls.base import reverse
from .views import SignUpView, EditProfileView
 

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('edit_profile', EditProfileView.as_view(), name='edit_profile'),
    

    
]