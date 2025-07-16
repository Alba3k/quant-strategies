# Quant Strategies

📈 A modular collection of algorithmic trading strategies built in Python. Designed for crypto markets and adaptable to other asset classes, this repository provides clean, testable implementations of technical strategies using pandas, NumPy, and pandas-ta.

## Included Strategies

- **EMA + RSI Strategy**  
  Combines short- and long-term exponential moving averages with the Relative Strength Index to identify directional bias and momentum. Generates long or short signals based on trend confirmation and strength.

## Features

- Modular architecture for easy strategy expansion
- Clean integration with CCXT for real-time crypto data
- Lightweight and readable codebase
- CLI-ready for live monitoring and automation

## Installation

```bash
git clone https://github.com/yourusername/quant-strategies.git
cd quant-strategies
pip install -r requirements.txt
