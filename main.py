import pandas as pd
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from capitalAssetPricingModel import *

if __name__ == '__main__':

    portfolio = []
    weights = []
    data = {}

    print("\nPlease input start and end date for your analysis."
          "\n Accepted input (YYYY-MM-DD) : 2020-02-03 2022-01-01 \n(start date followed by end date).")
    dates = input("Dates: ")
    datesList = dates.split(' ')

    start_date = datesList[0]
    end_date = datesList[1]

    print("\nPlease input ticker symbol/ symbols of stocks/Bonds in your portfolio."
          "\nAccepted example input:\n1. \"AAPL NVDA Tsla ge AMZN\" if you've a portfolio.\n"
          "2. \"AAPL\" if you've a single stock.")
    inputPortfolio = input("Portfolio: ")

    # Splitting input by spaces in between
    portfolio = inputPortfolio.split(' ')

    if len(portfolio) == 0:
        NameError("\nInvalid input, please input a valid value.")

    portfolio.append('^GSPC')

    print(portfolio)

    # using adjusted closing price as it's more accurate representation of stocks value
    # Closing Price: Actual price at close of the trading day
    # Adjusted closing price: Closing Price but takes into account factors such as dividends, stock splits etc.
    print("\nchecking input values and fetching information for these stocks.\n")
    # Checking if there is a mistake in the input, if not downloading data
    for security in portfolio:
        ticker = yf.download(security, start_date, end_date)
        data[security] = ticker['Adj Close']

    stock_data = pd.DataFrame(data)

    if len(portfolio) > 1:
        print("\nPlease input weights of respective stocks/Bonds in your portfolio."
              "\na) Accepted example input:\n\"0.25 0.15 0.6\" (Sum should be equal to 1) if you've a portfolio of "
              "\"AAPL NVDA Tsla\".\n "
              "b) Means you have 25% of Apple stock in your portfolio, 15% NVIDIA and so on.")
        inputWeights = input("Weights: ")

        # Splitting weights by spaces in between
        weightsString = inputWeights.split(' ')

        floatMap = map(float, weightsString)
        weights = list(floatMap)
        if sum(weights) != 1:
            raise NameError("\nSum of weights is not 1, please re input right values.\n")

        stocks_data = stock_data.resample('M').last()

        logReturn = np.log(stocks_data / stocks_data.shift(1))

        stocks_logReturn = logReturn[1:]

        # Covariance matrix: Diagonal items are variances
        # Off diagonal are covariances
        # The matrix is symmetric: Cov[0,1] = Cov[1,0]

        covariance_matrix_df = stocks_logReturn.cov()

        betaValues = []

        length = len(covariance_matrix_df)

        covariance_matrix = covariance_matrix_df.to_numpy()

        for x in range(0, length-1):
            betaValues.append(covariance_matrix[x, length-1]/covariance_matrix[length-1, length-1])

        beta_np = np.array(betaValues)
        weights_np = np.array(weights)

        betaPortfolio = np.dot(weights_np.T, beta_np)

        print("\nBeta values for individual stocks: ")

        for x in range(0, len(betaValues)):
            print(str(portfolio[x]) + ": " + str(betaValues[x]))

        print("\nBeta value for entire portfolio: " + str(betaPortfolio))










