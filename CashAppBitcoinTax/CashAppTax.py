import pandas as pd
import numpy as np

PATH="" #enter in path to csv file downloaded from Cash App 
dfCash = pd.read_csv(PATH)
dfCashBuy=pd.DataFrame(dfCash[dfCash["Transaction Type"].str.contains("Buy")])
dfCashBuy2020=pd.DataFrame(dfCashBuy[dfCashBuy["Date"].str.contains("2020")])
dfCashBuy2021=pd.DataFrame(dfCashBuy[dfCashBuy["Date"].str.contains("2021")])
totalCashDollarBuy2020=dfCashBuy2020['Amount'].str.lstrip("-$").str.replace(",","").astype(float).sum()
totalCashBTCBuy2020=dfCashBuy2020['Asset Amount'].astype(float).sum()
totalCashDollarBuy2021=dfCashBuy2021['Amount'].str.lstrip("-$").str.replace(",","").astype(float).sum()
totalCashBTCBuy2021=dfCashBuy2021['Asset Amount'].astype(float).sum()
aggCashPurchasePrice2020=totalCashDollarBuy2020/totalCashBTCBuy2020
aggCashPurchasePrice2021=totalCashDollarBuy2021/totalCashBTCBuy2021
totalBTCPurchased = totalCashBTCBuy2020 + totalCashBTCBuy2021
totalDollarSpent = totalCashDollarBuy2020 + totalCashDollarBuy2021
finalBTCPrice = totalDollarSpent/totalBTCPurchased

print("CASH APP SPEND")
print("2020")
print("Total BTC: "+str(round(totalCashBTCBuy2020,8)))
print("BTC Price: "+str(round(aggCashPurchasePrice2020,2)))
print("Dollar Spend: " +str(round(totalCashDollarBuy2020,2)))
print("2021")
print("Total BTC: "+str(round(totalCashBTCBuy2021,8)))
print("BTC Price: "+str(round(aggCashPurchasePrice2021,2)))
print("Dollar Spend: " +str(round(totalCashDollarBuy2021,2)))
print("Total")
print("Total BTC: "+str(round(totalBTCPurchased,8)))
print("BTC Price: "+str(round(finalBTCPrice,2)))
print("Dollar Spend: " +str(round(totalDollarSpent,2)))

dfCashSale=pd.DataFrame(dfCash[dfCash["Transaction Type"].str.contains("Sale")])
dfCashSale2021=pd.DataFrame(dfCashSale[dfCashSale["Date"].str.contains("2021")])
totalCashDollarSell2021=dfCashSale2021['Amount'].str.lstrip("$").str.replace(",","").astype(float).sum()
totalCashBTCSell2021=dfCashSale2021['Asset Amount'].astype(float).sum()
aggCashSellPrice2021=totalCashDollarSell2021/totalCashBTCSell2021
totalBTCSold = totalCashBTCSell2021
totalDollarSold = totalCashDollarSell2021
finalBTCPrice = totalDollarSold/totalBTCSold

print()
print("CASH APP SELL")
print("2020")
print("Total BTC: 0")
print("BTC Price: NA")
print("Dollar Recipt: NA")
print("2021")
print("Total BTC: "+str(round(totalCashBTCSell2021,8)))
print("BTC Price: "+str(round(aggCashSellPrice2021,2)))
print("Dollar Recipt: " +str(round(totalCashDollarSell2021,2)))
print("Total")
print("Total BTC: "+str(round(totalBTCSold,8)))
print("BTC Price: "+str(round(finalBTCPrice,2)))
print("Dollar Recipt: " +str(round(totalDollarSold,2)))