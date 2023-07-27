from django.urls import path
from console.views import signin_u,signin_p,signup_,signup__,signup___,signup____,validate_user,handleuserproducts,otp_verification,products

urlpatterns = [
    path('signin_u',signin_u.as_view()),
    path('signin_p',signin_p.as_view()),
    path('signup_',signup_.as_view()),
    path('signup__',signup__.as_view()),
    path('signup___',signup___.as_view()),
    path('signup____',signup____.as_view()),
    path('otp_verification',otp_verification.as_view()),
    path('validate_user',validate_user.as_view()),
    path('products',products.as_view()),
    path('handleuserproducts/<str:Email>',handleuserproducts.as_view()),
    path('handleuserproducts',handleuserproducts.as_view()),
]