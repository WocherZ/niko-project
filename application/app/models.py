from django.db import models

class User(models.Model):
    email = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

def create_user(email: str, name: str, surname: str, password: str):
    user = User(email=email, name=name, surname=surname, password=password)
    user.save()

def is_exist_user_by_email(email: str) -> bool:
    user_by_email = User.objects.filter(email=email).count()
    if user_by_email != 0: return True
    else: return False

def is_correct_password_by_email(email: str, password: str) -> bool:
    print("is_correct_password_by_email")
    print(email + " " + password)
    if is_exist_user_by_email(email):
        print("User by email exists")
        user_by_email_password = User.objects.filter(email=email).filter(password=password).count()
        print("Found number of user: " + str(user_by_email_password))
        if user_by_email_password != 0: return True
        else: return False
    else:
        return False

