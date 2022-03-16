import pandas as pd
import numpy as np
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os.path
import matplotlib.pyplot as plt

### APP INIT ###
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ubuntu/weather_app/data/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

### CREATE DB MODEL ###
class Temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    ba_avg = db.Column(db.Float(), nullable=False)
    bb_avg = db.Column(db.Float(), nullable=False)

### DB INIT IF NOT EXIST###
if not os.path.exists("data/data.db"):
    db.create_all()

### READ EXCEL TO PANDAS DF ###
BA_data = pd.read_excel("data/BA_TEMP_02_2022.ods")
BB_data = pd.read_excel("data/BB_TEMP_02_2022.ods")

### CREATE ONE DATAFRAME FROM 2 EXCEL FILES ###
data_sum = pd.DataFrame(BA_data["Date"].apply(lambda x: x.date().strftime('%m-%d')))
data_sum["BA_AVG"] = pd.DataFrame(BA_data["Avg"].apply(lambda x: float(x[:-3])))
data_sum["BB_AVG"] = pd.DataFrame(BB_data["Avg"].apply(lambda x: float(x[:-3])))

### IF DB IS NOT EMPTY - FILL DATA FROM DATAFRAME
if not Temp.query.first():
    for index, row in data_sum.iterrows():
        new_db_record = Temp(date=row['Date'], ba_avg=row['BA_AVG'], bb_avg=row['BB_AVG'])
        db.session.add(new_db_record)
    db.session.commit()

### GET DATA FROM DB
graph_data = Temp.query.all()

### PLOT BAR GRAPH FOR BA
ax = data_sum.plot.bar(x='Date', y='BA_AVG')
ax.set_title('BA monthly temperatures')
ax.set_ylabel("Temperature in °C")
fig = ax.get_figure()
fig.savefig('data/BA_AVG_TEMP.pdf')

### PLOT BAR GRAPH FOR BB
ax = data_sum.plot.bar(x='Date', y='BB_AVG')
ax.set_title('BB monthly temperatures')
ax.set_ylabel("Temperature in °C")
fig = ax.get_figure()
fig.savefig('data/BB_AVG_TEMP.pdf')


### PLOT LINE GRAPH FOR BA
ax = data_sum.plot.line(x='Date', y='BA_AVG')
ax.set_title('BA monthly temperatures')
ax.set_ylabel("Temperature in °C")
fig = ax.get_figure()
fig.savefig('data/BA_LINE_AVG_TEMP.pdf')

### PLOT LINE GRAPH FOR BB
ax = data_sum.plot.line(x='Date', y='BB_AVG')
ax.set_title('BB monthly temperatures')
ax.set_ylabel("Temperature in °C")
fig = ax.get_figure()
fig.savefig('data/BB_LINE_AVG_TEMP.pdf')

### PLOT BAR GRAPH FOR BA AND BB
ax = data_sum.plot.bar(secondary_y='BA_AVG')
ax.set_title('BA_BB monthly temperatures')
ax.set_ylabel("Temperature in °C")
fig.savefig('data/BA_BB_AVG_TEMP.pdf')

plt.show()

