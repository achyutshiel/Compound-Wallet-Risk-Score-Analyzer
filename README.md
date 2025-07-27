# 🔐 Compound Wallet Risk Score Analyzer




> 🚀 A cybersecurity & AI-focused Python project to analyze Compound Protocol wallet activity and assign dynamic **risk scores** based on user behavior.

---

## 📌 Objective

This project fetches **Compound Protocol wallet data** using **The Graph API**, analyzes wallet behaviors (borrows, repays, liquidations), and computes a **risk score** per wallet. The goal is to flag risky wallets and profile healthy ones — similar to a **DeFi credit score system**.

---

## 📊 Features

- 🔎 Fetches live data for **100+ Compound wallets**
- 📈 Computes a **risk score** based on borrow/repay/liquidation ratios
- ⚠️ Identifies risky wallet behavior patterns
- 📉 Auto-generates **risk histogram** (embedded in README)
- 📁 Outputs data in `CSV` format
- ✅ Uses **dynamic scoring ranges** (e.g., 650–1000+)
- 🔐 Built for **AI-powered cyber risk auditing in DeFi**

---

## 📂 Project Structure
```
compound_wallet_risk/
├── compound_risk_score.py # Main logic to fetch, calculate, and plot
├── wallet_risk_scores.csv # CSV output with wallet scores
├── risk_histogram.jpeg # Auto-generated histogram of wallet scores
├── README.md # This file
└── requirements.txt # Dependencies

```
---

## 🧪 Sample Output

| Wallet Address                             | Borrow Count | Repay Count | Liquidation Count | Risk Score |
|-------------------------------------------|--------------|-------------|-------------------|------------|
| 0x00000000009a41862f3b2b0c688b7c0d1940511e | 5            | 4           | 0                 | 843        |
| 0x000000aaee6a496aaf7b7452518781786313400f | 174          | 140         | 6                 | 765        |
| 0x0039f22efb07a647557c7c5d17854cfd6d489ef3 | 1            | 1           | 0                 | 980        |
| ...                                       | ...          | ...         | ...               | ...        |

---

## 🖼️ Histogram of Risk Scores

![wallet_score_histogram](https://github.com/user-attachments/assets/570a88aa-dc79-40f1-9d60-0c9ca1a41b26)

---

## 🧠 Risk Score Logic

```python
score = 1000
score -= (borrow_count * 1.3)
score -= (liquidation_count * 20)
score += (repay_count * 1.7)

# Normalize between 650 and 1000
score = max(650, min(score, 1000))

```

## 🔌 Tech Stack 

🐍 Python 3.10

📊 pandas, matplotlib

🧠 AI Logic (risk scoring)

🌐 The Graph API (GraphQL queries)

## 🛠️ Setup & Usage

1.Clone the repo:

```
git clone https://github.com/achyutshiel/compound-wallet-risk.git
cd compound-wallet-risk
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the project:
```
python compound_risk_score.py
```

## 📍 Use Cases

🎯 Cybersecurity Forensics (flagging malicious wallet behavior)

🧠 AI-driven risk profiling for DeFi apps

🧾 Regulatory compliance & wallet auditing

📉 Fraud detection in blockchain lending protocols

## 🧑‍💻 Author

**Achyut Pandey**  
🎓 Cybersecurity | AI | Blockchain | Developer  

🔗 [LinkedIn](https://www.linkedin.com/in/achyut-pandey/)  
🔗 [GitHub](https://github.com/achyutshiel)


## 📄License
This project is licensed under the MIT License

⭐ Give a star if you like this repo and find it useful!
