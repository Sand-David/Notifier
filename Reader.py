from Notification import Notifier

class CoinReader(Notifier):
    SOURCE_URL = 'tradingview.com'
    def __init__(self, coins: list):
        print("test")
        super().__init__(coins, self.SOURCE_URL)
        
    def get_url(self):
        return self.SOURCE_URL