from datetime import datetime

def generate_markdown(sector, analysis):
    return f"""
# 📊 Trade Opportunities Report
## Sector: {sector.title()}
## Region: India
## Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}

---

## 🧾 Market Overview
{analysis}

---

## 📈 Trade Opportunities
- Growth stocks
- Export potential
- Policy-driven opportunities

---

## ⚠️ Risks
- Regulatory changes
- Market volatility

---

## 🔮 Outlook
Moderate growth expected.

---

## 📌 Disclaimer
This is AI-generated analysis and not financial advice.
"""