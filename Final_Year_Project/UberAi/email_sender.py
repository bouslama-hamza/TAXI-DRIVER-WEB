import smtplib
import random
from email.message import EmailMessage

class SendEmail():

    def __init__(self):
        self.message = EmailMessage()
        self.EMAIL_ADDRESS = 'test.herbaly@gmail.com'
        self.EMAIL_PASSWORD = 'badBOY@2020'
        self.message['From'] = self.EMAIL_ADDRESS
        self.message['To'] = self.EMAIL_ADDRESS

    def send_access_email(self , email):
        self.message['Subject'] = 'Request To Access Into UberAi Lab'
        self.message.set_content('\nThis Person is trying to access to UberAi Lab System .if it able to : please inser it into the Data Base Query System with the fallowing email : '+str(email))
        with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.EMAIL_ADDRESS,self.EMAIL_PASSWORD)
            smtp.send_message(self.message)

    def send_change_password(self , email):
        self.message['Subject'] = 'Request To Change Password'
        number = random.randint(11111111,99999999)
        self.message.set_content('\nYour request to change your password has been added successfuly please use the following code to access : \n'+str(number))
        with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.EMAIL_ADDRESS,self.EMAIL_PASSWORD)
            smtp.send_message(self.message)
        return number

    def send_contact_us(self , name , address , subject):
        self.message['Subject'] = 'Request For Contact'
        self.message.set_content('\nThis Person Have Some Question Or Disscusing The He Want To Know , Thank Your For Answering After Saying The Message :\nFull Name : '+str(name)+'\nEmail Address : '+str(address)+'\nContact Message : '+str(subject))
        with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.EMAIL_ADDRESS,self.EMAIL_PASSWORD)
            smtp.send_message(self.message)

