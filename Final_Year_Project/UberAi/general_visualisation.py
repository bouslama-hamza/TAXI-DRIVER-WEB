import pandas as pd
def visualisation():
    list = []
    df = pd.read_csv("UberAi/static/testing/test.csv" , nrows = 10)
    for i in df.iterrows():
        list.append({'date' : i[1]['date'] , 'hour' : i[1]['hour'] , 'type' : i[1]['type'] , 'confidence' : i[1]['confidence'] , 'status' : i[1]['status']})
    return list