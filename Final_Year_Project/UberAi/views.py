from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import RequestContext
from .models import Taxi
from UberAi.forms import UserLoginForm , UserUpdateForm
from UberAi.email_sender import SendEmail
from UberAi.download import download
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from UberAi.pridection import Pridection
from UberAi.general_visualisation import visualisation , latest_detection , return_time
import datetime
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


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
    data = visualisation(10)
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
    new_time , before_time = return_time()
    data = visualisation(100)
    _ , confidence ,_ = latest_detection()
    data.reverse()
    date ={
        'day' : datetime.datetime.now().strftime("%A"),
        'fulldate' : datetime.datetime.now().strftime("%d %B %Y"),
        'time' : datetime.datetime.now().strftime("%H:%M %p")
    }
    if datetime.datetime.strptime(new_time.split(" ")[0], "%H:%M") < datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M"), "%H:%M"):
        new_time , before_time = Pridection().generate_time()
        return render(request , 'system_pridection.html' ,{'title': 'Ai System Pridection' , 'date' : date , 'data' : data , 'latest' : data[0]["hour"] , 'new' : new_time , 'before' : before_time , 'confidence' : int(confidence)})
    return render(request , 'system_pridection.html' ,{'title': 'Ai System Pridection' , 'date' : date , 'data' : data , 'latest' : data[0]["hour"] , 'new' : new_time , 'before' : before_time , 'confidence' : int(confidence)})

@login_required
def dashboard(request):
    date ={
        'day' : datetime.datetime.now().strftime("%A"),
        'fulldate' : datetime.datetime.now().strftime("%d %B %Y"), 
        'time' : datetime.datetime.now().strftime("%H:%M %p")
    }
    return render(request , 'dashboard.html' , {'title' : 'DashBoard' ,'date' : date}) 

@login_required
def taxi_order(request):
    data_taxi = Taxi.objects.all()
    date ={  
        'day' : datetime.datetime.now().strftime("%A"),
        'fulldate' : datetime.datetime.now().strftime("%d %B %Y"),
        'time' : datetime.datetime.now().strftime("%H:%M %p")
    }
    return render(request ,'taxi_order.html' , {'title' : 'Taxi Order System' , 'date' :date , 'data' : data_taxi})

@csrf_exempt
def datajson(request):
    data = visualisation(100)
    data.reverse() 
    latest , confidence ,total = latest_detection()
    return JsonResponse({'data' : data , 'latest' : str(latest) ,'confidence' :str(int(confidence))  ,'deconfidence' : str(round(100 - int(confidence) , 2)), 'total' : str(total)}) 