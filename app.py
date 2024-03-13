from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def bitcoin_price():
    # 업비트에서 비트코인 가격 가져오기
    upbit_url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    upbit_response = requests.get(upbit_url)
    upbit_data = upbit_response.json()[0]
    upbit_price = upbit_data['trade_price']
    upbit_change = upbit_data['signed_change_rate'] * 100  # 백분율 변화량

    # 바이낸스에서 BTC/USDT 가격 가져오기
    binance_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    binance_response = requests.get(binance_url)
    binance_data = binance_response.json()
    binance_price = binance_data['price']

    # 'index.html' 템플릿으로 변수 전달
    return render_template('index.html', upbit_price=upbit_price, upbit_change=upbit_change, binance_price=binance_price)

if __name__ == '__main__':
    app.run(debug=True)
