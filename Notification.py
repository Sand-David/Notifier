

class Notifier:
    #global url?
    def __init__(self, assets: list, url: str):
        print("notifier initialized")
        self.registered_assets = assets
        self.url = url

    def getInfo(self):
        print("here is the info")
        for coin in self.registered_assets:
            print("coin has been selected...")
            print(f"prepare info from {self.url}")

    