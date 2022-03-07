import pandas as pd
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

RISK_FREE_RATE = 0.015
# we will consider monthly returns - and we want to calculate the annual return
MONTHS_IN_YEAR = 12

class CAPM:
    def __init__(self, stocks_data):
        self.stocks_data = stocks_data
        self.data = None

    def initialize(self):
        self.data = pd.DataFrame({'s_adjclose': stocks_data[self.stocks[0]], 'm_adjclose': stocks_data[self.stocks[1]]})

        # log monthly returns
        self.data[['s_returns', 'm_returns']] = np.log(
            self.data[['s_adjclose', 'm_adjclose']] / self.data[['s_adjclose', 'm_adjclose']].shift(1))

        self.data = self.data[1:]


    def calculate_beta(self):
        # Covariance matrix: Diagonal items are variances
        # Off diagonal are covariances
        # The matrix is symmetric: Cov[0,1] = Cov[1,0]

        covariance_matrix = np.cov(self.data['s_returns'], self.data['m_returns'])
        print(covariance_matrix)
        # Beta from formula
        beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]
        return beta


    def regression(self):
        # using linear regression to fit a line to the data
        # [stock_returns, market_returns] - slope
        beta, alpha = np.polyfit(self.data['m_returns'], self.data['s_returns'], deg=1)
        print(beta)
        # calculate expected return according to CAPM formula
        # we want annual return, so *12
        expected_return = RISK_FREE_RATE + beta * (self.data['m_return'].mean() * MONTHS_IN_YEAR - RISK_FREE_RATE)
        print(expected_return)
        self.plot_regression(alpha, beta)


    def plot_regression(self, alpha, beta):
        fig, axis = plt.subplots(1, figsize=(20, 10))
        axis.scatter(self.data['m_returns'], self.data['s_returns'], label="Data Points")
        axis.plot(self.data)