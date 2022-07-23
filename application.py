#importing libraries
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

application=Flask(__name__)
app=application
app.config['DEBUG']=True

@app.route('/',methods=['GET','POST'])
def home():
    df=pd.read_json('https://www.mohfw.gov.in/data/datanew.json')
    data=[]
    for i in df.iloc[:36].index:
        data.append([df['sno'][i],df['state_name'][i],df['active'][i],df['cured'][i],df['positive'][i],df['death'][i]])
    return render_template('index.html',df=data)


if __name__=='__main__':
    app.run()
