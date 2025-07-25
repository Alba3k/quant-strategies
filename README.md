# :bank: Quant Strategies

📈 A modular collection of algorithmic trading strategies built in Python.<br> 
Designed for crypto markets and adaptable to other asset classes, this repository provides clean, testable implementations of technical strategies using `pandas`, `NumPy`, and `pandas-ta`.

---

## 🚀 Included Strategies

#### :one: `EMA + RSI Strategy`

This strategy combines two key technical indicators:

1. **EMA 13 vs EMA 30**: Measures short-term vs long-term trend direction
2. **RSI (Relative Strength Index)**: Gauges momentum and potential overbought/oversold conditions

#### :two: `MACD + Stochastic Combo`

Combines trend-following MACD with momentum-based Stochastic oscillator to identify high-probability reversal zones. Indicators Used:

1. **MACD (12, 26, 9)**: Measures trend direction and momentum
2. **Stochastic Oscillator (14, 3)**: Detects overbought/oversold conditions

#### :three: `Bollinger Bands Squeeze Breakout`

Combines volatility breakout detection with momentum filtering to capture explosive moves while avoiding false entries. 
This strategy is ideal for breakout traders who want to avoid chasing exhausted moves. 
It works well in high-volatility environments and can be paired with volume filters or trailing stops.
Indicators Used:

1. **Bollinger Bands (20, 2)**: Measures volatility and price extremes
2. **RSI (14)**: Confirms momentum and filters overbought/oversold conditions

#### :four: `ATR Trailing Stop`

Uses volatility-based stop-loss logic to manage breakout entries. Indicators Used:

1. **ATR (14)**: Measures average volatility
2. **High/Low Breakouts (20)**: Entry triggers

#### :five: `Triple EMA Momentum`

Identifies strong directional trends using layered EMAs. Indicators Used:

1. **EMA 7**
2. **EMA 21**
3. **EMA 50**
	
#### :six: `Stochastic + Price Action`	

Combines momentum and trend confirmation for cleaner entries. Indicators Used:

1. **Stochastic (14, 3, 3)**
2. **SMA50**

#### :seven: `EMA Regular Order Strategy`

EMA Regular Order Strategy Uses short-term EMA crossover (EMA4 vs EMA9) to generate entry signals. 
Ideal for intraday trading on minute or 15-minute timeframes. Indicators Used:

1. **EMA 4 fast**
2. **EMA 9**

#### :eight: `MACD Bracket Order Strategy`

MACD Bracket Order Strategy Based on MACD line crossing the signal line, with potential for bracket orders (TP/SL).
Ideal for intraday trading on minute or 15-minute timeframes. Indicators Used:

1. **MACD**

#### :nine: `Silver Channel Strategy`

Silver Channel Strategy Trades price bounces within dynamic channels built from recent highs and lows.
Suited for short-term swing setups on 1H or 4H timeframes.

#### :one::zero: `RSI Divergence Strategy (Enhanced)`

Detects hidden bullish/bearish divergences between price and RSI. Indicators Used:

1. **RSI (14)**

and many others...

---

## 🧩 Features

- 🧱 Modular architecture for easy strategy expansion
- 🔌 Seamless integration with [CCXT](https://github.com/ccxt/ccxt) for real-time crypto data
- 🧼 Clean and readable codebase for rapid development
- 🖥️ CLI-ready for live monitoring and automation
- 📦 Lightweight dependencies for fast deployment

---

## ⚙️ Installation

```bash
git clone https://github.com/Alba3k/quant-strategies.git
cd quant-strategies
pip install -r requirements.txt
