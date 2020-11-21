import pandas as pd

#global df
df = pd.DataFrame({'nome': pd.Series([], dtype='str'), 'email': pd.Series([], dtype='str'), 'data': pd.Series([], dtype='str')})

def updateVar(newDF):
    global df
    df = newDF