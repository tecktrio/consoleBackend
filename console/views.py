'''
This program should be in the views.py file on widecity console. 
Author AMAL BENNY
contact amalpullan4@gmail.com
####################################################################
'''
'''
Imporing neccessary modules for the program
'''
import random
import re
from django.http import JsonResponse
from rest_framework.views import APIView

from console.Serializers import ProductSerializer
from console.models import Products
from . import constants 
import requests

'''
Console Backend Methods
Responsible for Verifying user name on signin
'''
class signin_u(APIView):
    def get(self,request):
        return JsonResponse( {'status':'Get method not allowed at this endpoint'})
    def post(self,request):
        Email = request.data['Email']
        response = requests.get(f'{constants.core_url}/Users/CheckEmail/{Email}?key=widecitymakesitsimple')
        return JsonResponse( {'status':response.json()['status']})

''' 
Responsible for Verifying user password on signin
'''
class signin_p(APIView):
    def get(self,request):
        return JsonResponse( {'status':'Get method not allowed at this endpoint'})
    def post(self,request):
        Email = request.data['Email']
        Password = request.data['Password']
        data = {
            'Email':Email,
            'Password':Password
        }
        response = requests.post(f'{constants.core_url}/Users/Login?key=widecitymakesitsimple',data=data)
        return JsonResponse({'status':response.json()['status']})

'''
Responsible for verifying email and contact number during signup
'''
class signup_(APIView):
    def get(self,request):
        return JsonResponse( {'status':'Get method not allowed at this endpoint'})
    def post(self,request):
        Email = request.data['Email']
        Contact = request.data['Contact']
        if not re.fullmatch( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',Email):
            return JsonResponse({'status':'failed','error':'invalid email'})
        response = requests.get(f'{constants.core_url}/Users/CheckEmail/{Email}?key=widecitymakesitsimple')
        if response.json()['status'] == 'success':
            return JsonResponse({'status':'failed','error':'Email id exist'})             
        try:int(Contact)
        except:return JsonResponse({'status':'failed','error':'contact number should contain only numbers'})
        return JsonResponse({'status':'success'})
    
'''
Responsible for verifying firstname and lastname during signup
'''
class signup__(APIView):
    def get(self,request):
        return JsonResponse( {'status':'Get method not allowed at this endpoint'})
    def post(self,request):
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        if len(firstname)<1:
            return JsonResponse({'status':'failed','error':'First Name cannot be null'})
        if len(lastname)<1:
            return JsonResponse({'status':'failed','error':'Last Name cannot be null'})
        return JsonResponse({'status':'success'})    
    
class signup____(APIView):
    def get(self,request):
        return JsonResponse( {'status':'Get method not allowed at this endpoint'})
    def post(self,request):
        Otp = request.data['Otp']
        First_Name = request.data['First_Name']
        Last_Name = request.data['Last_Name']
        Email = request.data['Email']
        Country_Code = request.data['Country_Code']
        Contact_Number = request.data['Contact_Number']
        Password = request.data['Password']
        data = {
            'Email':Email,
            'Password':Password,
            'First_Name':First_Name,
            'Last_Name':Last_Name,
            'Country_Code':Country_Code,
            'Contact_Number':Contact_Number,
        }
        response = requests.post(f'{constants.core_url}/Users/Register?key=widecitymakesitsimple',data=data)
        if response.json()['status'] == 'success':
            return JsonResponse({'status':'success'})   
        return JsonResponse({'status':'failed'})   
         
'''
Responsible for verifying password during signup
'''    
class signup___(APIView):
    def get(self,request):
        return JsonResponse( {'status':'Get method not allowed at this endpoint'})
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
    
'''
Responsible for validating user name
'''
class validate_user(APIView):
    def get(self,request):
        return JsonResponse({'status':'failed'})
    def post(self,request):
        return JsonResponse({'status':'success'})
    
'''
Responsible for generating otp verification
'''
class otp_verification(APIView):
    def get(self,request):
        otp = random.randint(1000,9999)
        print('sending auto generated otp')
        return JsonResponse({'status':'success','otp':str(otp)})
    
    
class products(APIView):
    def get(self,request):
        products = Products.objects.all()
        serialized_products = ProductSerializer(products,many=True)
        return JsonResponse({'status':'success','data':serialized_products.data})
    def post(self,request):
        return JsonResponse({'status':'post method not allowed in this endpoint'})    
    
class handleuserproducts(APIView):
    def get(self,request,Email):
        response = requests.get(f'{constants.core_url}/Products/HandleUserProducts/{Email}?key=widecitymakesitsimple')
        print(response.json()['status'])
        if not response.json()['status'] == 'success':
            return JsonResponse({'status':'failed','error':'Email id exist','data':{[]}})             
        return JsonResponse({'status':'success','data':response.json()['data']})
    def put(self,request):

        UserEmail = request.data['UserEmail']
        ProductName = request.data['ProductName']
        DueDate = request.data['DueDate']
        data = {
            'UserEmail' : UserEmail,
            'ProductName':ProductName,
            'DueDate':DueDate
        }
        response = requests.put(f'{constants.core_url}/Products/HandleUserProducts?key=widecitymakesitsimple',data=data)
        if  response.json()['status'] == 'success':
            return JsonResponse({'status':'success'})
        return JsonResponse({'status':'failed','error':'Email id exist'})             
    def post(self,request):
        UserEmail = request.data['UserEmail']
        ProductName = request.data['ProductName']
        DueDate = request.data['DueDate']
        data = {
            'UserEmail' : UserEmail,
            'ProductName':ProductName,
            'DueDate':DueDate
        }
        response = requests.post(f'{constants.core_url}/Products/HandleUserProducts?key=widecitymakesitsimple',data=data)
        if  response.json()['status'] == 'success':
            return JsonResponse({'status':'success'})
        return JsonResponse({'status':'failed','error':response.json()['error']})             

        # return JsonResponse({'status':'post method not allowed in this endpoint'})