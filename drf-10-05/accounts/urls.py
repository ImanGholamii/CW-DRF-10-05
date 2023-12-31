from django.urls import path
from .views import user_list, UserLoginView, UserRegistrationView

urlpatterns = [
    path('user/', user_list, name='user'),
    path('user-login/', UserLoginView.as_view(), name="login"),
    path('user-registration/', UserRegistrationView.as_view(), name='register'),
]
