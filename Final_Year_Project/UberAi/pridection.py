import pandas as pd
import requests
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime
from csv import writer
import datetime


class Pridection:

    def __init__(self):
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        self.URL = self.BASE_URL + "q=khouribga&appid=b95aec434694dd2839ad0fd6810ef875"
        self.response = requests.get(self.URL)
        self.df = pd.read_csv("UberAi/static/testing/pridection.csv")
        self.db = pd.read_csv("UberAi/static/testing/test.csv")
        self.model = LinearRegression()

    def generate_weather(self):
        new_weather = []
        new_weather.append(datetime.datetime.today().weekday())
        if self.response.status_code == 200:
            data = self.response.json()
            weather = data['main']
            for i in weather.values():
                new_weather.append(i)
            for row in self.db.tail(1).iterrows():
                new_weather.append(int(row[1]['hour'].split(" ")[0]+row[1]['hour'].split(" ")[2]))
            return new_weather
        else:
            print("Error in the HTTP request")  
    
    def train_model(self):
        X = np.array(self.df[['day' , 'temp' , 'feels_like' , 'temp_min' , 'temp_max' , 'pressure' , 'humidity' , 'sea_level' ,'grnd_level' , 'last_time']])
        Y = np.array(self.df['new_time'])
        self.model.fit(X,Y)

    def time_pridection(self):
        array = self.generate_weather()
        self.train_model()
        result = self.model.predict(np.array([array]))
        array.append(int(result[0]))
        return array

    def add_to_csv(self):
        with open("UberAi/static/testing/pridection.csv" , 'a') as f:
            array = self.time_pridection()
            object_write = writer(f)
            object_write.writerow(array)
            f.close()
        return array
    
    def generate_time(self):
        array = self.add_to_csv()
        time_new= str(datetime.timedelta(seconds=int(array[10]))).split(":")
        time_new =time_new[0] + ":" +time_new[1] + " "+datetime.datetime.now().strftime("%p")
        for row in self.db.tail(1).iterrows():
            time_before = row[1]['hour'].split(" ")[0]+":"+row[1]['hour'].split(" ")[2]+" "+row[1]['hour'].split(" ")[3]
        return time_new , time_before

