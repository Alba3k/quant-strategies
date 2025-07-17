# :bank: Quant Strategies

📈 A modular collection of algorithmic trading strategies built in Python. 
Designed for crypto markets and adaptable to other asset classes, this repository provides clean, testable implementations of technical strategies using `pandas`, `NumPy`, and `pandas-ta`.

---

## 🚀 Included Strategies

### :one: EMA + RSI Strategy

This strategy combines two key technical indicators:

1. **EMA13 vs EMA30**: Measures short-term vs long-term trend direction
2. **RSI (Relative Strength Index)**: Gauges momentum and potential overbought/oversold conditions


---

### 🔁 MACD + Stochastic Combo

Combines trend-following MACD with momentum-based Stochastic oscillator to identify high-probability reversal zones.

#### 📊 Indicators Used
- **MACD (12, 26, 9)**: Measures trend direction and momentum
- **Stochastic Oscillator (14, 3)**: Detects overbought/oversold conditions

#### 🔁 Signal Logic

```python
:green_book: **Buy (LONG)**:  
MACD line crosses above Signal line AND Stochastic %K crosses above %D in oversold zone (<20)
```
```python
:closed_book: **Sell (SHORT)**:  
MACD line crosses below Signal line AND Stochastic %K crosses below %D in overbought zone (>80)
```

#### 📦 Output Columns
`MACD`, `Signal`, `%K`, `%D`, `MACD_Signal`, `Stoch_Signal`, `Position`

This strategy is ideal for swing entries near exhaustion zones, with confirmation from both trend and momentum indicators.

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
