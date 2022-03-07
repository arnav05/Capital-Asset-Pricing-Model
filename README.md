Holding only one kind of stock is risky, should hold portfolio of stocks. 

2 kinds of risks: Systematic and unsystematic 

Systematic risk: The risk inherent to the entire market or market segment. It cannot be diversified. It happens because of following changes:
- Recession
- Interest rates
- Inflation
- Rise in unemployment
- Wars etc.

Unsystematic risk: It is unique to a specific company or industry. Also known as non-systematic risk, specific risk, diversifiable risk, or residual risk. It can be 
diversified away by holding multiple stocks in portfolio. Markowitz model reduces this risk.

CAPM: Linear relationship between any stock and market premium

E[r(a)] = r(f) + β(a)*(E[r(m)]-r(f))

E[r(a)] = Expected return of investment
r(f) = Base return (Risk free rate)
β(a) = Measure of systematic risk. Defines risk we have to take.
E[r(m)] = Market return (S&P 500 return)

β(a) = 1 : Stock moving exactly with market
β(a) < 1 : Stock is less volatile than market
β(a) > 1 : Stock is more volatile than market

CAPM measures risk with beta (β) parameter. Beta in CAPM is measure of systematic risk. It gauges the tendency of the return of security to 
move in parallel with the return of the stock market as a whole. Another way to think about it is as a gauge of a security's volatility 
relative to the market's volatility. 

Stock expected return ∝ (Directly Proportional) Market Premium

From Linear equation: 
β(a) = (E[r(a)] - r(f))/(E[r(m)]-r(f))

Other way to write β(a):
β(a) = (cov(r(a), r(m)))/var(r(m))

β(a) = (E[r(a)] - r(f))/(E[r(m)]-r(f)) = (cov(r(a), r(m)))/var(r(m))

For a portfolio: 
β(a) value is the weighted sum of stocks betas within portfolio

β(a) = w1β1 + w2β2 + ... + wnβn

Linear Regression: Approach for modelling scalar dependent variable y and one or more explanatory variables x (independent). It's called linear regression 
because we use linear predictor functions.
H(x) = b0 + b1x

2 types of linear regressions (LR) : Simple LR and Multiple LR

Simple LR: Single x explanatory variable
Multiple LR: Multiple x variables

Accuracy of Linear Regression: Mean Squared Error (MSE)
(H(x)-y)^2

R^2 statistic:
R^2 = 1 - (RSS/TSS)

RSS: Residual sum of squares. Measures variability left unexplained after regression.
Σ[(H(x)-y)^2]

TSS: Measures total variability
(1/n) Σ[(y-µ)^2]

CAPM + LR
E[r(a)] - r(f) = α + β(a)*(E[r(m)]-r(f))

α = Difference between return and expected return
In CAPM, it is 0.


# Market rate = S&P 500
