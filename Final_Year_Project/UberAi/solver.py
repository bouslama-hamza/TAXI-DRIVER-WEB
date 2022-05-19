import datetime
from datetime import timedelta

def get_data(confidence):
    detection = {
        'date' : datetime.datetime.now().strftime("%d %B %Y"),
        'hour' : (datetime.datetime.now()- timedelta(minutes=15)).strftime("%H : %M %p") ,
        'type' : 'TAXI DRIVER',
        'confidence' : confidence,
        'status' : 'New Detection'
    }
    return str(detection['date'])+","+str(detection['hour'])+","+detection['type']+","+str(detection['confidence'])+","+detection['status']