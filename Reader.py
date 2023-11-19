from notification import Notifier
import yfinance as yf

class CoinReader(Notifier):
    SOURCE_URL = 'coin.com'

    def __init__(self, coins: list):
        super().__init__(coins)
        
    def getInfo(self):
        print("overwritten method")
        for coin in self.registered_assets:
            print(f"Coin {coin} has been selected...")
            print(f"prepare info from  {self.url}")
            ticker = yf.Ticker(coin)
            print(ticker.history(period="1mo")['open'])