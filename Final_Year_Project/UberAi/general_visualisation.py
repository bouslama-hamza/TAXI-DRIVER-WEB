import pandas as pd
import datetime
def visualisation(n):
    list = []
    df = pd.read_csv("UberAi/static/testing/test.csv" , nrows = n)
    for i in df.iterrows():
        list.append({'date' : i[1]['date'] , 'hour' : i[1]['hour'] , 'type' : i[1]['type'] , 'confidence' : i[1]['confidence'] , 'status' : i[1]['status']})
    return list

def latest_detection():
    df = pd.read_csv("UberAi/static/testing/test.csv")
    latest = df['status'].value_counts()
    for row in df.iloc[[-1]].iterrows():
        confidence = row[1]['confidence'].split("%")[0]
    return latest['New Detection'] - latest['Passed Detection'] ,float(confidence)*100 ,  latest['New Detection']

def to_solve():
    df = pd.read_csv("static/testing/test.csv")
    latest = df['status'].value_counts()
    for row in df.iloc[[-1]].iterrows():
        confidence = row[1]['confidence'].split("%")[0]
    return latest['New Detection'] - latest['Passed Detection'] 

def return_time():
    df = pd.read_csv("UberAi/static/testing/pridection.csv")
    line = df.tail(1)
    for row in line.iterrows():
        new = row[1]['new_time']
        before = row[1]['last_time']
    time_new= str(datetime.timedelta(seconds=new)).split(":")
    time_before = str(datetime.timedelta(seconds=int(before))).split(":")
    time_new =time_new[0] + ":" +time_new[1] + " "+datetime.datetime.now().strftime("%p")
    time_before =time_before[0] + ":" +time_before[1] + " "+datetime.datetime.now().strftime("%p")
    return time_new , time_before
