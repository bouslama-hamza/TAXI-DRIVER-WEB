import pandas as pd
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

