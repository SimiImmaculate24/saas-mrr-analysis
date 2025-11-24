# SaaS MRR Quarterly Performance Analysis

**Author / Contact:** 24ds2000040@ds.study.iitm.ac.in

**Data source used (example):** data/mrr_quarterly.csv

## Executive Summary
The company’s average monthly recurring revenue (MRR) growth for 2024 quarters is **8.05**. The industry benchmark target is **15**. This indicates a clear shortfall versus competitor/industry expectations and requires strategic initiatives to accelerate growth.

## Data & Key Findings
- Quarterly values:
  - Q1: 6.73
  - Q2: 10.05
  - Q3: 5.42
  - Q4: 10.00
- **Computed average MRR growth:** **8.05**
- Trend: growth is inconsistent with two stronger quarters (Q2, Q4) and two weak quarters (Q1, Q3). Volatility suggests product-market fit and go-to-market inconsistency.
- The company is ~6.95 percentage points below the industry target of 15.

## Business Implications
- Slower revenue growth threatens ability to invest in product & sales capacity and may reduce valuation multiples at the next funding or reporting period.
- Volatility across quarters suggests either seasonal demand effects or inconsistent acquisition/retention efforts.
- Competitors meeting the 15% target likely have clearer segment fit and higher-converting acquisition channels.

## Recommendation (Actionable) — **Expand into new market segments**
To reach the 15% benchmark, prioritize:
1. **Targeted segment expansion**: Identify 1–2 high-ARPU segments adjacent to current customers (e.g., industry verticals, larger enterprise tiers).
2. **Dedicated GTM experiments**: Run short 12-week go-to-market experiments per segment (tailored landing pages, targeted ads, sales outreach, custom onboarding).
3. **Product packaging**: Create vertical-specific packages and pricing that simplify purchase decisions for the new segment.
4. **Sales & success resources**: Assign a small SDR + Customer Success pilot team to validate expansion and accelerate initial closed-won deals.
5. **Measure and iterate**: Use cohort-level metrics (CAC, LTV, conversion rate) from these pilots to forecast trajectory toward 15%.

These combined actions are expected to increase average MRR growth by improving conversion and ARPU from new segments.

## How this analysis was created
- Simple Python analysis reads `data/mrr_quarterly.csv`, computes the average (8.05), saves `output/mrr_trend.png`, and stores summary metrics in `output/metrics_summary.csv`.
- **LLM assistance:** This PR includes commits and messaging that note assistance from **Jules (ChatGPT Codex)** to generate analysis code and README content.

This project analyzes the quarterly MRR growth of a SaaS company and compares performance against the industry benchmark growth rate of **15%**.  
It includes trend analysis, visualizations, and a business-focused interpretation of results.

---

## 📊 Quarterly MRR Growth Chart

The visualization below shows the company’s quarter-over-quarter MRR growth compared to the industry benchmark:

![MRR Growth Chart](mrr_trend.png)

---

## 📈 MRR Growth Summary

| Quarter | MRR Start | MRR End | Growth (%) |
|--------|-----------|---------|------------|
| Q1 | 45,000 | 48,000 | 6.73% |
| Q2 | 48,000 | 52,825 | 10.05% |
| Q3 | 52,825 | 55,690 | 5.42% |
| Q4 | 55,690 | 61,260 | 10.00% |

---

## 📉 Comparison With Industry Benchmark (15%)

- **Q1:** Below benchmark  
- **Q2:** Below benchmark  
- **Q3:** Strongly below benchmark  
- **Q4:** Still below benchmark, but improves significantly  

At no point does the company reach or exceed the 15% benchmark.

---

## 🧠 Data Story & Interpretation

The company demonstrates **steady but inconsistent growth** through the year:

- Growth peaks in **Q2**, indicating successful acquisition or upsell efforts.
- **Q3 dips sharply**, signaling possible customer churn, seasonal effects, or reduced marketing efficiency.
- **Q4 rebounds**, suggesting improved retention or successful revenue-driving initiatives.

Overall, the year ends with a positive gain but **does not match industry expectations** for SaaS companies operating in a high-growth environment.

---

## 💡 Business Insights & Recommendations

### 1. Strengthen Q3 Retention Strategy  
The drop in Q3 is the biggest red flag. Deeper analysis needed on:
- churned customer segments  
- lost revenue sources  
- seasonal or operational disruptions  

### 2. Increase Upsell/Cross-sell Efforts  
Q2 and Q4 show the company *can* grow faster when efforts are aligned.  
A dedicated customer success motion may push growth closer to 15%.

### 3. Evaluate Marketing ROI  
Benchmark-ready SaaS companies maintain 12–20% quarterly growth.  
The company may need:
- higher lead volume  
- improved conversion rate  
- revised pricing model  

### 4. Benchmark Customer Acquisition Cost (CAC)  
If CAC is high, growth will remain capped below industry standards.

---

## 📂 Repository Structure

├── data/
│ └── mrr_data.csv
├── mrr_trend.png
├── analysis.ipynb (optional)
├── README.md


---

## 🚀 Conclusion

The company is growing, but not at the pace expected in the competitive SaaS market.  
With better churn management and stronger acquisition/retention strategies, the company can realistically target the **15% industry benchmark**.
## Files added
- `data/mrr_quarterly.csv`
- `analysis/analysis.py`
- `requirements.txt`
- `output/mrr_trend.png` (generated by running analysis)
- `README.md`

## Verification
- Run `python3 analysis/analysis.py` to reproduce metrics and create `output/mrr_trend.png`.

## Contact
Email: 24ds2000040@ds.study.iitm.ac.in
