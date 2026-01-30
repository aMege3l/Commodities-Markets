import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tickers = {
    "ZS=F": "Soybeans_Futures",
    "DBA": "Agriculture_ETF",
    "SOYB": "Soybean_ETF",
    "CORN": "Corn_ETF",
    "ADM": "ADM",
    "BG": "Bunge",
    "CTVA": "Corteva",
    "FMC": "FMC",
    "MOS": "Mosaic",
    "ANDE": "Andersons",
    "VFF": "VillageFarms",
    "NTR": "Nutrien",
    "CF": "CFIndustries",
    "DE": "Deere"
}

start = "2019-01-01"
end = "2026-12-31"

prices = pd.DataFrame()

for ticker, name in tickers.items():
    df = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=False
    )
    prices[name] = df["Adj Close"]

prices.dropna(inplace=True)
prices = prices.round(6)
prices.to_csv(
    "soybeans_dataset_ESILV.csv",
    sep=';',
    decimal='.'
)


print("Dataset OK :", prices.shape)


weekly_prices = prices.resample("W").last()
plt.figure(figsize=(14, 8))
for col in weekly_prices.columns:
    plt.plot(weekly_prices.index, weekly_prices[col]/weekly_prices[col].iloc[0], label=col)
plt.title("Soybeans Market – Weekly", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend(ncol=2, fontsize=9)
plt.grid(True)

plt.tight_layout()
plt.show()