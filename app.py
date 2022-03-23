from flask import Flask, request, render_template
import joblib
import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)
def forecast(n):
    df = readData()
    best_model = joblib.load('timeSeries.pkl')
    forecast_values = best_model.get_forecast(steps = n)
    forecast_ci = forecast_values.conf_int()
    print(df['Order_Date'],df['Sales'])
    ax = plt.plot(df['Order_Date'], df['Sales'], figsize = (16, 6), legend = True, color='purple')
    forecast_values.predicted_mean.plot(ax=ax, label='Forecast', figsize = (16, 6), grid=True)
    ax.fill_between(forecast_ci.index,
                    forecast_ci.iloc[: , 0],
                    forecast_ci.iloc[: , 1], color='pink', alpha = .5)
    plt.title('Sales Forecast', size = 16)
    plt.ylabel('Sales', size=12)
    plt.legend(loc='upper left', prop={'size': 12})
    ax.axes.get_xaxis().set_visible(True)
    ax.text(540, 400, 'Forecasted Values', fontsize=12,  color='black')
    plt.savefig('static/forecast1.png')
    #plt.show()
    return True

#@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method == "POST":
        '''df = readData()
        best_model = joblib.load('timeSeries.pkl')'''
        #forecast(int(request.form.get('steps')))
        #forecast_values = best_model.get_forecast(steps=int(request.form.get('steps')))
        '''df.plot(x='Order_Date', y='Sales', figsize=(16, 6), legend=True, color='purple')
        plt.title('Sales', size=16)
        plt.ylabel('Sales', size=12)
        plt.legend(loc='upper left', prop={'size': 12})
        plt.savefig('static/Sales.png')
        plt.clf()
        forecast_values.predicted_mean.plot(label='Forecast', figsize=(16, 6), grid=True)
        plt.title('Forecast', size=16)
        plt.ylabel('Sales', size=12)
        plt.legend(loc='upper left', prop={'size': 12})
        plt.savefig('static/Forecast.png')'''
    return render_template('index.html')

def readData():
    df = pd.read_csv("mainDF.csv", encoding='latin')
    return df

if __name__ == "__main__":
    #app.run(debug=True)
    forecast(70)
