from django.db import models
import re
import bcrypt

EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#TODO finish out validator
    #email, make sure it isnt taken
    #passwords makesure both passwords match
#TODO set up login validator
    #TODO first find email


class manager(models.Manager):
    def register(self, data):
        hashed = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            firstname = data['firstname'],
            lastname = data['lastname'],
            password = hashed,
            email = data['email']
        )

    def validator(self, data):
        errors = {} #stores errors
        if len(data['firstname']) < 5:
            errors['firstname'] = 'First name must be longer than 5 characters'
        if len(data['lastname']) < 5:
            errors['lastname']= 'Last name must be longer than 5 characters'

        #Email Error check
        if len(data['email']) < 10:
            errors['email']='Email must be longer than 10 characters'
        if not EMAIL_MATCH.match(data['email']): 
            errors['email']='Invalid email format'
        users_with_this_email = self.filter(email = data['email']) #used to check if the email is already taken
        if users_with_this_email:
            errors['email'] = 'Email is already taken'
        
        #password check
        if len(data['password']) < 5:
            errors['password']= 'password is not long enough'
        if data['password']!= data['RePassword']:
            errors['password'] = 'Passwords don\'t match!!!'

        return errors
    
    def authenticator(self, email, pwd):
        email = self.filter(email = email)
        if not email: #if email is null
            return False
        user = email[0] #takes the first user in the list
        return bcrypt.checkpw(pwd.encode(), user.password.encode())
        

class users(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 250)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = manager()