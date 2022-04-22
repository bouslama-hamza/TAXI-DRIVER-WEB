import smtplib
import random

def send_email(email):
    EMAIL_ADDRESS = 'test.herbaly@gmail.com'
    EMAIL_PASSWORD = 'badBOY@2020'
    with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        subject = 'Request To Access Into UberAi Lab'
        body = '\nThis Person is trying to access to UberAi Lab System .if it able to : please inser it into the Data Base Query System with the fallowing email : '+str(email)
        msg = f'Subject : {subject} \n\n {body}'
        smtp.sendmail(EMAIL_ADDRESS , EMAIL_ADDRESS ,msg)

def send_email_change(email):
    EMAIL_ADDRESS = 'test.herbaly@gmail.com'
    EMAIL_PASSWORD = 'badBOY@2020'
    with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
        n = random.randint(11111111,99999999)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        subject = 'Request To Change Password'
        body = '\nYour request to change your password has been added successfuly please use the following code to access : \n'+str(n)
        msg = f'Subject : {subject} \n\n {body}'
        smtp.sendmail(EMAIL_ADDRESS , EMAIL_ADDRESS ,msg)
    return n

def contact_us(name , address , message):
    EMAIL_ADDRESS = 'test.herbaly@gmail.com'
    EMAIL_PASSWORD = 'badBOY@2020'
    with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        subject = 'Request For Contact'
        body = '\nThis Person Have Some Question Or Disscusing The He Want To Know , Thank Your For Answering After Saying The Message :\nFull Name : '+str(name)+'\nEmail Address : '+str(address)+'\nContact Message : '+str(message)
        msg = f'Subject : {subject} \n\n {body}'
        smtp.sendmail(EMAIL_ADDRESS , EMAIL_ADDRESS ,msg)