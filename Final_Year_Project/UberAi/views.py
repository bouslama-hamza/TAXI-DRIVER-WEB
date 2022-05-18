from django.shortcuts import render
from django.contrib.auth.models import User
from UberAi.forms import UserLoginForm , UserUpdateForm
from UberAi.email_sender import SendEmail
from UberAi.download import download
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse, Http404
from UberAi.general_visualisation import visualisation
import os

def home(request):
    return render(request , 'home.html' , {'title' : 'Home'})

def singup(request):
    send_email = SendEmail()
    if request.method == 'POST':
        send_email.send_access_email(request.POST['email'])
        message = 'Your Email Has Been Sent Successfully'
        return render(request , 'signup.html' , {'title' : 'SignUp' , 'message' : message})
    return render(request , 'signup.html' , {'title' : 'SignUp'})

def forget_password(request):
    send_email = SendEmail()
    global change_number
    global user
    if request.method == 'POST':
        email = request.POST['change_email']
        try :
            user = User.objects.get(email = email)
            change_number = send_email.send_change_password(user.email)
            return render(request ,'confirm_password.html' , {'title' : 'Confirm Password'})
        except:
            error = 'This User Dont Have An Account , Please Chaque Your Information'
            return render(request , 'forget_password.html' , {'error': error , 'title' : 'Forget Password'})
    return render(request , 'forget_password.html' , {'title' : 'Forget Password'})

def confirm_password(request):
    if request.method == 'POST':
        if change_number != int(request.POST['number']):
            error = 'Error! Wrong Number please chaque and try Again'
            return render(request , 'confirm_password.html' , {'error' : error , 'title' : 'Confirm Password'})
        elif request.POST['change_password'] != request.POST['conf_change_password']:
            error = 'Error! Password and Confirm password are not the same'
            return render(request , 'confirm_password.html' , {'error' : error , 'title' : 'Confirm Password'})
        else:
            user.set_password(request.POST['conf_change_password'])
            user.save()
            form = UserLoginForm()
            message = 'Your password has been change Successfully'
            return render(request , 'login.html' , {'form' : form ,'message' : message , 'title' : 'Log In'})
    return render(request , 'confirm_password.html' , {'title' : 'Confirm Password'})

def about(request):
    return render(request , 'about.html' , {'title' : 'About'})

def contact(request):
    send_email = SendEmail()
    if request.method == 'POST':
        name = request.POST['fullname']
        email= request.POST['address']
        message = request.POST['message']
        send_email.send_contact_us(name ,email ,message)
        alert = 'Your Contact Message Has Been Sent Successfully'
        return render(request , 'contact.html' , {'title' : 'Contact', 'alert' : alert})
    return render(request , 'contact.html' , {'title' : 'Contact' })

@login_required
def general_visualisation(request):
    data = visualisation()
    data.reverse()
    date ={
        'day' : datetime.datetime.now().strftime("%A"),
        'fulldate' : datetime.datetime.now().strftime("%d %B %Y"),
        'time' : datetime.datetime.now().strftime("%H:%M %p")
    }
    if request.method == 'POST':
        path = download(int(request.POST['data']))
        with open(path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
            os.remove(path)
            return response
    return render(request , 'general_visualisation.html' , {'title' : 'General Visualisation' , 'date' : date , 'data' : data})
    
@login_required
def profile_modification(request):
    date ={
        'day' : datetime.datetime.now().strftime("%A"),
        'fulldate' : datetime.datetime.now().strftime("%d %B %Y"),
        'time' : datetime.datetime.now().strftime("%H:%M %p")
    }
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance = request.user)
        if update_form.is_valid():
            request.user.set_password(update_form.cleaned_data.get('password2'))
            update_form.save()
            message = 'Setting has been Updating Successfully'
            return render(request , 'profile_modification.html' , {'update_form':update_form , 'message':message , 'title' : 'Profile Modification' , 'date' : date})
        else:
            error = 'Invalid Information Please Try Again'
            return render(request , 'profile_modification.html' , {'update_form':update_form , 'error':error , 'title' : 'Profile Modification' , 'date' : date})
    else:
        update_form = UserUpdateForm(instance = request.user)
    return render(request, 'profile_modification.html' , {'title' : 'Profile Modification' , 'update_form':update_form ,'date' : date} )

@login_required
def system_pridection(request):
    date ={
        'day' : datetime.datetime.now().strftime("%A"),
        'fulldate' : datetime.datetime.now().strftime("%d %B %Y"),
        'time' : datetime.datetime.now().strftime("%H:%M %p")
    }
    return render(request , 'system_pridection.html' ,{'title': 'Ai System Pridection' , 'date' : date})
