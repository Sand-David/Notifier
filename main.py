from reader import CoinReader
import trigger
def get_asset_list():
    asset_file = open(r'C:\Users\David\Projects\Notifier\kryptos.txt', 'r')
    return list(asset_file.read().splitlines())


test = {'BTC': 1, 'ETH': 2}
trigger.fetch_triggered_assets(test)

# c = CoinReader(get_asset_list())

# c.getInfo()

