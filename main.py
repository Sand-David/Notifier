from reader import CoinReader
import trigger
def get_asset_list():
    asset_file = open(os.path.join(os.path.dirname(__file__), 'symbols.txt'), 'r')
    return list(asset_file.read().splitlines())

def main():
    #test = {'BTC': 1, 'ETH': 2}
    test = ['BTC', 'ETH']

    trigger.init_overview(test)

# c = CoinReader(get_asset_list())

# c.getInfo()

import os
if __name__ == "__main__":
    main()
