import yfinance as yf
import matplotlib.pyplot as plt

tickers = [t.strip().upper() for t in input("ENTER THE TICKER(S) (EXAMPLE: TSLA, MSFT, AMZN): ").split(',')]

start_date=input("ENTER THE STARTING DATE TO GET THE DATA.(YYYY-MM-DD): ")
end_date=input("ENTER THE ENDING DATE TO GET THE DATA.(YYYY-MM-DD): ")
data=yf.download(tickers,start_date,end_date,threads=False,auto_adjust=False)

#getting returns
adj_close=data["Adj Close"]
returns = adj_close.pct_change().dropna()

#getting avg daily return
avg_daily_return=returns.mean()*100
print("Avg Daily Return(%):\n ",avg_daily_return)
print()

#FIG - 1: Daily Closing Price 
plt.figure(figsize=(14,7))

if len(tickers)==1:
    plt.plot(adj_close,label=tickers[0])

else:
    for ticker in tickers:
        plt.plot(adj_close[ticker],label=ticker)
plt.title("STOCK PRICE TREND")
plt.xlabel("Date")
plt.ylabel("Adjusted Closing Price (USD)")
plt.legend()
plt.show()


#FIG-2 Plotting the avg daily return
plt.figure(figsize=(10,6))

avg_daily_return.plot(kind="bar",color="green",edgecolor="black")
plt.title("AVG DAILY RETURN(%)",fontsize=16)
plt.xlabel("Ticker",fontsize=12)
plt.ylabel("% Return",fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.show()

#getting volatility
volatility= returns.std()*100
print("VOLATILITY OF EACH STOCK: ",volatility)
print()

#FIG-3 Plotting the Daily avg volatitlity(%) 
plt.figure(figsize=(10,6))

if len(tickers)==1:
    volatility.plot(kind="bar",color="blue",edgecolor="black",label=tickers[0])
    plt.title("AVG DAILY VOLATILITY(%)")
    plt.xlabel("Ticker",fontsize=12)
    plt.ylabel("Volatility (%)",fontsize=12)
    plt.legend()
    plt.show()

else:
    volatility.plot(kind="bar",color="blue",edgecolor="black")
    plt.title("AVG DAILY VOLATILITY(%)")
    plt.xlabel("Tickers",fontsize=12)
    plt.ylabel("Volatility (%)",fontsize=12)
    plt.legend()
    plt.show()

#FIG-4 Risk (Volatility) v/s Return 
plt.figure(figsize=(10,6))

plt.scatter(volatility,avg_daily_return,color="pink",s=100)

for i,ticker in enumerate(tickers):
    plt.text(volatility.loc[ticker],avg_daily_return.loc[ticker],ticker,fontsize=12,ha="right",va="bottom")

plt.title("RISK v/s RETURN",fontsize=16)
plt.xlabel("Volatility(%)",fontsize=12)
plt.ylabel("Avg Daily Return(%)",fontsize=12)
plt.axhline(0,color="gray",linestyle="--",linewidth=0.8,label="Zero Return Line")
plt.axvline(volatility.mean(),color="orange",linestyle="--",linewidth=0.8,label="Average Volatility")
plt.legend(loc="upper left")
plt.grid(alpha=0.3)
plt.show()

#FIG-5 Plotting Daily Volume
volume=data["Volume"]
plt.figure(figsize=(10,6))

if len(tickers) == 1:
    plt.plot(volume, label = tickers[0])

else:
    for ticker in tickers:
        plt.plot(volume[ticker],label=ticker)
plt.title("VOLUME PERIOD")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.legend()
plt.show()