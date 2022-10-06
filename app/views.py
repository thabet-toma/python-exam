from ast import Return
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import  bcrypt

def logandRegs(request):
    return render(request,'LogAndRegs.html')
def regs(request):
    errors = Users.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
    
        hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        Users.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],password=hash)
        request.session['user']=Users.objects.last().first_name
        request.session['state']='registered'
        return redirect('/success1')
def success1(request):
    if 'user' in request.session:
        context={'last':Users.objects.last()}
        return render(request,'success.html',context)
    else:
        return redirect('/') 
def login(request):
    
    # see if the username provided exists in the database
    user = Users.objects.filter(email=request.POST['email']) # why are we using filter here instead of get?
    if user: # note that we take advantage of truthiness here: an empty list will return false
        logged_user = user[0] 
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['user'] = logged_user.first_name
            request.session['state']='logged in'
            request.session['Uid']=logged_user.id
            # never render on a post, always redirect!
            return redirect('/logged')
        else:
            messages.error(request, 'invalid email or password')
            print(messages,"*"*9)
            return redirect("/")

    else:
        messages.error(request, 'invalid email or password')
        return redirect("/")
def logout(request):
    del request.session['user']
    del request.session['Uid']
    return redirect('/')
def logged(request):
    
    if "Uid" in request.session:
        context={'user':Users.objects.get(id=request.session['Uid']),
        'allTrees':Trees.objects.all()
        }
        return render(request,'logged.html',context)
    else:
        return redirect('/')
def addNew(request):
    if "Uid" in request.session:
        context={'user':Users.objects.get(id=request.session['Uid'])
        
        }
        return render(request,'addNew.html',context)
    else:
        return redirect('/')
def addProcess(request):
    errors = Trees.objects.basic_validator(request.POST)
        
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/new/tree')
    else:
        user=Users.objects.get(id=request.session['Uid'])
        Trees.objects.create(Species=request.POST['species'],location=request.POST['location'],reason=request.POST['reason'],date_planted=request.POST['date'],user=user)
        return redirect('/backToDash')
def backToDash(request):
    return redirect('/logged')
def myTrees(request):
    if "Uid" in request.session:
        context={'user':Users.objects.get(id=request.session['Uid'])
        
        }
        return render(request,'mytree.html',context)
    else:
        return redirect('/')
def editShow(request,id):
    context={'tree':Trees.objects.get(id=id)}
    return render(request,'editShow.html',context)
def editProcess(request):
    errors = Trees.objects.basic_validator(request.POST)
        
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        
        
    else:
        x=Trees.objects.get(id=request.POST['get'])
        x.Species=request.POST['species']
        x.location=request.POST['location']
        x.reason=request.POST['reason']
        x.date_planted=request.POST['date']
        x.save()
    return redirect('/edit/'+str(request.POST['get']))
def showTree(request,id):
    context={'tree':Trees.objects.get(id=id)}
    return render(request,'showTree.html',context)
def delete(request,id):
    tree=Trees.objects.get(id=id)
    tree.delete()
    return redirect('/user/account')
    






    
        
# Create your views here
