import datetime

import backtrader as bt
import pandas as pd


# simple moving average
class SimpleMA(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data, period=5, plotname="5 SMA"
        )


# Instantiate Cerebro engine
cerebro = bt.Cerebro(stdstats=False)

# Set data parameters and add to Cerebro
data = pd.read_csv("daily_price.csv")
data["stck_bsop_date"] = pd.to_datetime(data["stck_bsop_date"], format="%Y%m%d")
data["open"] = data["stck_oprc"]
data["high"] = data["stck_hgpr"]
data["low"] = data["stck_lwpr"]
data["close"] = data["stck_clpr"]
data["volume"] = data["acml_vol"]
data_bt = bt.feeds.PandasData(dataname=data, datetime="stck_bsop_date")
cerebro.adddata(data_bt)

cerebro.addstrategy(SimpleMA)
# Run Cerebro Engine
cerebro.run()
cerebro.plot()
