import pandas as pd

def download(number_of_column):
    df = pd.read_csv('UberAi/static/testing/test.csv' , nrows = number_of_column)
    name = f"UberAi/static/testing/General_Visualisation_{number_of_column}.csv"
    df.to_csv(name)
    return name