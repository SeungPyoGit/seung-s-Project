import yfinance as yf

frbk = yf.Ticker("FRB")
df = frbk.history(period="max")
df = df.tail(120)
print(df)
