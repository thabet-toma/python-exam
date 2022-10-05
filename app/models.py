from django.db import models
from distutils.log import error
# import email
# from tkinter.tix import Tree
# from venv import create
# from xml.etree.ElementTree import Comment

import re
class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['fname']) < 3:
            errors["fname"] = "First name should be at least 2 characters"
        if len(postData['lname']) < 3:
            errors["lname"] = "Last name should be at least 2 characters"
        if len(postData['email']) < 0:
            errors["email"] = "email is required"
        email_regex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        for i in Users.objects.all():
            if i.email==postData['email']:
                errors['email'] = "this email is already exist in our database"

        if len(postData['password']) < 9:
            errors["password"] = "password should be at least 8 characters"
        if not postData['password']==postData['confirm']:
            errors["password"]='invalid password'

        return errors


class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
