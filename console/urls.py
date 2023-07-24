from django.urls import path
from console.views import signin_u,signin_p,signup_,signup__,signup___,validate_user,otp_verification

urlpatterns = [
    path('signin_u',signin_u.as_view()),
    path('signin_p',signin_p.as_view()),
    path('signup_',signup_.as_view()),
    path('signup__',signup__.as_view()),
    path('signup___',signup___.as_view()),
    path('otp_verification',otp_verification.as_view()),
    path('validate_user',validate_user.as_view()),
    
]