import requests
import pandas as pd
import matplotlib.pyplot as plt

# === Config ===
API_URL = "https://gateway.thegraph.com/api/subgraphs/id/4TbqVA8p2DoBd5qDbPMwmDZv3CsJjWtxo8nVSqF2tA9a"
API_KEY = "62709cbe0e7d1e85544041e04d00cd46"

query = """
{
  accounts(first: 100) {
    id
    borrowCount
    repayCount
    liquidationCount
  }
}
"""

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.post(API_URL, headers=headers, json={"query": query})

if response.status_code != 200:
    print("❌ Error fetching data:", response.status_code, response.text)
    exit()

accounts = response.json()["data"]["accounts"]

wallets = []
scores = []

for acc in accounts:
    wallet = acc["id"]
    borrows = acc.get("borrowCount", 0)
    repays = acc.get("repayCount", 0)
    liquidations = acc.get("liquidationCount", 0)

    # === Score Logic (realistic 600–1000 range) ===
    score = 600 \
            + repays * 4.2 \
            - borrows * 1.5 \
            - liquidations * 5.5 \
            + (repays - borrows) * 3.3 \
            + (15 if repays > borrows else -20)

    score = int(min(1000, max(600, score)))

    wallets.append(wallet)
    scores.append(score)

# === Save to CSV ===
df = pd.DataFrame({"wallet_id": wallets, "score": scores})
df.to_csv("wallet_risk_scores.csv", index=False)
print("✅ CSV saved: wallet_risk_scores.csv")

# === Plot histogram ===
plt.figure(figsize=(10, 6))
plt.hist(df["score"], bins=20, color='mediumorchid', edgecolor='black')
plt.title("Wallet Risk Score Distribution")
plt.xlabel("Risk Score (600–1000)")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.savefig("wallet_score_histogram.jpeg", format="jpeg")
print("📊 JPEG saved: wallet_score_histogram.jpeg")
