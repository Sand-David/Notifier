import yfinance as yf

class Notifier:
    #global url?
    def __init__(self, assets: list, url: str = "yfiance.com"):
        print("notifier initialized")
        self.registered_assets = assets
        self.url = url
        print(self.url)

    def getInfo(self):
        print("here is the info")
        for asset in self.registered_assets:
            # print("coin has been selected...")
            # print(f"prepare info from {self.url}")
            ticker = yf.Ticker(asset)
            print(ticker.info)

    