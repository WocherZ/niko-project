import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest

from .models import *

def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            name = data.get('name')
            surname = data.get('surname')
            password = data.get('password')

            if not is_exist_user_by_email(email):
                create_user(email, name, surname, password)
                return HttpResponse("OK")
            else:
                return HttpResponseBadRequest("User already exists")
        except Exception as e:
            print(e)
            return HttpResponseBadRequest("Bad data format")
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])

def authorization(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if is_correct_password_by_email(email, password):
                return HttpResponse("OK")
            else:
                return HttpResponseBadRequest("Incorrect email or password")

        except Exception as e:
            print(e)
            return HttpResponseBadRequest("Bad data format")
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])