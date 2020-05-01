"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from StockExchange import app
from nsetools import Nse
from flask import request,url_for, redirect
from flask import jsonify

@app.route('/')
@app.route('/home')
def home():

    """Renders the home page."""
    return render_template('index.html',
                            year=datetime.now().year,)

@app.route('/stockcodes', methods=['GET','POST'])
def stockcodes():
    nse = Nse()
    all_stock_codes = nse.get_stock_codes()
    stockLists = []

    for stk in all_stock_codes:
        obj = {
            "Value" : all_stock_codes[stk],
            "Key" : stk
            }
        stockLists.append(obj)

    return jsonify(nseLists=stockLists)

@app.route('/company', methods=['GET','POST'])
def company():
    nse = Nse()
    clicked = None
    if request.method == 'POST':
        clicked = request.form["code"]
        data = nse.get_quote(clicked)

        obj = {
            "Company Name" : data["companyName"],
            "Symbol" : data["symbol"],
            "Open" : data["open"],
            "Previous Close" : data["previousClose"],
            "Average Price" : data["averagePrice"],
            "Day High" : data["dayHigh"],
            "Day Low" : data["dayLow"],
            "Low 52" : data["low52"],
            "High 52" : data["high52"],
            "ISIN Code" : data["isinCode"],
            "Last Price" : data["lastPrice"],
            "Total Traded Value" : data["totalTradedValue"],
            "Total Traded Volume" : data["totalTradedVolume"],
            "Price Band Lower" : data["pricebandlower"],
            "Change" : data["change"],
            "Percent Change" : data["pChange"]    
            }
        return jsonify(obj)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.')

@app.route('/about')
def about():
    nse = Nse()
    all_stock_codes = nse.get_stock_codes()
    return render_template('about.html', 
                           nseLists=all_stock_codes, 
                           title='About',
                            year=datetime.now().year,
                            message='Your application description page.')


@app.route('/nse')
def nse():
    nse = Nse()
    all_stock_codes = nse.get_stock_codes()
    return render_template('StockExchange.html', nseLists=all_stock_codes)

@app.route('/stockname', methods=['GET', 'POST'])
def stockname():
    nse = Nse()
    all_stock_codes = nse.get_stock_codes()
    if request.method == 'POST':
        stockcodes = request.form['stockcodes']
        data = nse.get_quote(stockcodes) 
        return render_template('StockExchange.html',nseLists=all_stock_codes, data= data)

@app.route('/test', methods=['GET','POST'])
def test():
    nse = Nse()
    clicked = None
    if request.method == 'POST':
        clicked = request.form["code"]
        data = nse.get_quote(clicked)

        obj = {
            "Company Name" : data["companyName"],
            "Symbol" : data["symbol"],
            "Open" : data["open"],
            "Previous Close" : data["previousClose"],
            "Average Price" : data["averagePrice"],
            "Day High" : data["dayHigh"],
            "Day Low" : data["dayLow"],
            "Low 52" : data["low52"],
            "High 52" : data["high52"],
            "ISIN Code" : data["isinCode"],
            "Last Price" : data["lastPrice"],
            "Total Traded Value" : data["totalTradedValue"],
            "Total Traded Volume" : data["totalTradedVolume"],
            "Price Band Lower" : data["pricebandlower"],
            "Change" : data["change"],
            "Percent Change" : data["pChange"]    
            }

        #return render_template('about.html')
        return jsonify(obj)