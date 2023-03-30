##기본포맷
from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

#방향제시   / 는 기본경로
@app.route('/')
def index():
    return render_template('search.html')

@app.route('/result', methods=['POST'])
def result():
    stock_ticker = request.form['stock_ticker']
    stock_data = yf.Ticker(stock_ticker).history(period="30d")

    return render_template('result.html', data=stock_data.to_html(calsses='table table-striped'))

## 기본함수
if __name__ == '__main__':
    app.run(debug=True)
