from django.urls import path, include

from .views import UserProfile, UsersList

urlpatterns = [
    path('profiles', UsersList.as_view()),
    path('profile', UserProfile.as_view())
]