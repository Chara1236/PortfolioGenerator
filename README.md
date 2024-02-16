# PortfolioGenerator

### Installation
```
pip install yfinance
pip install pandas
```

### Setup
Place a minimum of 10 tickers in the file Tickers.csv one per line like so.
```
ORLY
AMP-A
LSCC
BKCC
HTH
CBA
HERO
AEH
FRC-C
LHO-G
```

### Output
After you run the program, the stocks/weights choosen will appear in Stocks_Group_8.csv

Furthur more the program will provide you with info as the program runs.

Eg. Shows list of 10 tickers choosen, displays average coorelation, and displays graph so coorelation may be visualized.
![image](https://github.com/Chara1236/PortfolioGenerator/assets/53840675/14664f32-c252-4783-acd0-db28ffb9b672)


### Theory
Rules for stock selection:

1. The goal is to make the risky portfolio possible
2. A minimum of 10 stocks are to be choosen (and as riskiness is the goal, you will be only generating 10 stocks)
3. Each stocks weight must not exceed 20% and must be more than 5%.
4. $750000 is allocated to buying the stocks.
5. For simplicitiy a portfolios success should be measured by the absolute difference between the original value of $750000 within 1 week.

The stocks are choosen based of their correlation to each other and their returns to both minimize cancellation between different stocks and maxmizie expected return/loss.
