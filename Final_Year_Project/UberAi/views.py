from django.shortcuts import render
from django.contrib.auth.models import User
from UberAi.forms import UserLoginForm
from UberAi.email_sender import SendEmail

def home(request):
    return render(request , 'home.html' , {'title' : 'Home'})

def app(request):
    return render(request , 'app.html' ,{'title' : 'App'})

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

    