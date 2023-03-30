##기본포맷
from flask import Flask, render_template
##
import yfinance as yf

app = Flask(__name__)

#방향제시   / 는 기본경로
@app.route('/')
def stock_data():
    frbk = yf.Ticker("FRBK")
    df = frbk.history(period="max")
    df = df.tail(120)
    ## stock_data.html 결과값을 표시하겠다
    ## to_html 형식으로 변환하겠다
    return render_template('stock_data.html', data=df.to_html())

## 기본함수
if __name__ == '__main__':
    app.run(debug=True)
