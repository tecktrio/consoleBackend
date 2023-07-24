import random
import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic import TemplateView
from . import constants 
# Create your views here.
import requests


class signin_u(APIView):
    def get(self,request):
        pass
    def post(self,request):
        Email = request.data['Email']
        # print('email',email)
        # print(f'http://34.230.46.127/Users/CheckEmail/{email}?key=widecitymakesitsimple')
        response = requests.get(f'{constants.core_url}/Users/CheckEmail/{Email}?key=widecitymakesitsimple')
        # print(response.json())  
        return JsonResponse( {'status':response.json()['status']})

class signin_p(APIView):
    def get(self,request):
        pass
    def post(self,request):
        
        Email = request.data['Email']
        Password = request.data['Password']
        print(Email, Password)
        data = {
            'Email':Email,
            'Password':Password
        }
        # print('email',email)
        # print(f'http://34.230.46.127/Users/CheckEmail/{email}?key=widecitymakesitsimple')
        response = requests.post(f'{constants.core_url}/Users/Login?key=widecitymakesitsimple',data=data)
        print(response.json())
        return JsonResponse({'status':response.json()['status']})
    
class signup_(APIView):
    def get(self,request):
        pass
    def post(self,request):
        Email = request.data['Email']
        Contact = request.data['Contact']
        # Validate the email using regX
        if not re.fullmatch( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',Email):
            return JsonResponse({'status':'failed','error':'invalid email'})
        # validating the email
        response = requests.get(f'{constants.core_url}/Users/CheckEmail/{Email}?key=widecitymakesitsimple')
        if response.json()['status'] == 'success':
                    return JsonResponse({'status':'failed','error':'Email id exist'})
                
        try:int(Contact)
        except:return JsonResponse({'status':'failed','error':'contact number should contain only numbers'})

        
        return JsonResponse({'status':'success'})
    
class signup__(APIView):
    def get(self,request):
        pass
    def post(self,request):
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        if len(firstname)<1:
            return JsonResponse({'status':'failed','error':'First Name cannot be null'})
        # validating Last name
        if len(lastname)<1:
            return JsonResponse({'status':'failed','error':'Last Name cannot be null'})
        return JsonResponse({'status':'success'})    
        
class signup___(APIView):
    def get(self,request):
        pass
    def post(self,request):
        password = request.data['password']
        password_re = request.data['password_re']

        if password != password_re:
            return JsonResponse({'status':'failed','error':'password does not match'})
        # Password Validation
        # testng the length
        if not len(password) >= 8:
            return JsonResponse({'status':'failed','error':'password should contain atleast 8 charecter'})
        # checking numbers in password
        if not re.search('[0-9]',password):
            return JsonResponse({'status':'failed','error':'password should contain atleast one number'})
        # checking whether the password contain any capital letters
        if not re.search('[A-Z]',password):
            return JsonResponse({'status':'failed','error':'password should contain atleast one Capital Letter'})
        # checking whether the password contain any small letters
        if not re.search('[a-z]',password):
            return JsonResponse({'status':'failed','error':'password should contain atleast one small letter'})
        
        return JsonResponse({'status':'success'})    
    
class validate_user(APIView):
    def get(self,request):
        return JsonResponse({'status':'failed'})
    def post(self,request):
        return JsonResponse({'status':'success'})
    

class otp_verification(APIView):
    def get(self,request):
        otp = random.randint(1000,9999)
        print('sending auto generated otp')
        return JsonResponse({'status':'success','otp':str(otp)})