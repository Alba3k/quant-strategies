# 🧠 Quant Strategies

📈 A modular collection of algorithmic trading strategies built in Python. Designed for crypto markets and adaptable to other asset classes, this repository provides clean, testable implementations of technical strategies using `pandas`, `NumPy`, and `pandas-ta`.

---

## 🚀 Included Strategies

### 🔁 EMA + RSI Strategy

This strategy combines two key technical indicators:

- **EMA13 vs EMA30**: Measures short-term vs long-term trend direction
- **RSI (Relative Strength Index)**: Gauges momentum and potential overbought/oversold conditions

#### 📊 Signal Logic

| Signal Type | Condition | Interpretation |
|-------------|-----------|----------------|
| 🟢 **Buy (LONG)** | `EMA13 > EMA30` and `RSI > 50` | Uptrend confirmed and momentum strong |
| 🔴 **Sell (SHORT)** | `EMA13 < EMA30` and `RSI < 50` | Downtrend confirmed and momentum weak |

The strategy generates a position signal (`LONG` or `SHORT`) only when **both conditions align**, reducing noise and false entries.
<h3>📊 Signal Logic</h3>

<table>
  <thead>
    <tr>
      <th style="text-align:left;">Signal Type</th>
      <th style="text-align:left;">Condition</th>
      <th style="text-align:left;">Interpretation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>🟢 <strong>Buy (LONG)</strong></td>
      <td><code>EMA13 &gt; EMA30</code> and <code>RSI &gt; 50</code></td>
      <td>Uptrend confirmed and momentum strong</td>
    </tr>
    <tr>
      <td>🔴 <strong>Sell (SHORT)</strong></td>
      <td><code>EMA13 &lt; EMA30</code> and <code>RSI &lt; 50</code></td>
      <td>Downtrend confirmed and momentum weak</td>
    </tr>
  </tbody>
</table>

<p><em>The strategy generates a position signal (<strong>LONG</strong> or <strong>SHORT</strong>) only when both conditions align, reducing noise and false entries.</em></p>

<h3>📊 Signal Logic</h3>

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th style="text-align: left; padding: 8px;">⚡ Signal Type</th>
      <th style="text-align: left; padding: 8px;">📐 Condition</th>
      <th style="text-align: left; padding: 8px;">🧠 Interpretation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #eafaf1;">
      <td style="padding: 8px;"><strong>🟢 Buy (LONG)</strong></td>
      <td style="padding: 8px;"><code>EMA13 &gt; EMA30</code> and <code>RSI &gt; 50</code></td>
      <td style="padding: 8px;">Uptrend confirmed and momentum strong</td>
    </tr>
    <tr style="background-color: #fdecea;">
      <td style="padding: 8px;"><strong>🔴 Sell (SHORT)</strong></td>
      <td style="padding: 8px;"><code>EMA13 &lt; EMA30</code> and <code>RSI &lt; 50</code></td>
      <td style="padding: 8px;">Downtrend confirmed and momentum weak</td>
    </tr>
  </tbody>
</table>

<p style="margin-top: 12px;"><em>📌 The strategy generates a position signal (<strong>LONG</strong> or <strong>SHORT</strong>) only when both conditions align, reducing noise and false entries.</em></p>

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
