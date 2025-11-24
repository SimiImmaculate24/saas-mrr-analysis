#!/usr/bin/env python3
"""
MRR Quarterly Analysis
Computes descriptive metrics and creates a trend plot comparing company MRR growth to industry benchmark.
Author: Automated script (to be committed). Email for verification: 24ds2000040@ds.study.iitm.ac.in
LLM assistance noted: Jules (ChatGPT Codex) / LLM-assisted commit labels.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Paths
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "mrr_quarterly.csv")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Parameters
INDUSTRY_BENCHMARK = 15.0

# Read data
df = pd.read_csv(DATA_PATH)
# Ensure numeric
df['mrr_growth'] = pd.to_numeric(df['mrr_growth'], errors='coerce')

# Compute metrics
avg_mrr = df['mrr_growth'].mean()
min_mrr = df['mrr_growth'].min()
max_mrr = df['mrr_growth'].max()

print("Quarterly MRR growth values:")
print(df.to_string(index=False))
print(f"\nComputed average MRR growth: {avg_mrr:.2f}")

# Save a small metrics CSV for evidence
metrics = {
    'average_mrr_growth': [round(avg_mrr, 2)],
    'min_mrr_growth': [round(min_mrr, 2)],
    'max_mrr_growth': [round(max_mrr, 2)],
    'industry_benchmark': [INDUSTRY_BENCHMARK]
}
metrics_df = pd.DataFrame(metrics)
metrics_df.to_csv(os.path.join(OUTPUT_DIR, "metrics_summary.csv"), index=False)

# Plotting
quarters = df['quarter']
values = df['mrr_growth']

plt.figure(figsize=(8,5))
plt.plot(quarters, values, marker='o', linewidth=2, label='Company MRR growth')
plt.hlines(INDUSTRY_BENCHMARK, xmin=-0.1, xmax=len(quarters)-0.9,
           linestyles='dashed', label=f'Industry benchmark ({INDUSTRY_BENCHMARK}%)')
# Annotate each point with values
for x, y in zip(quarters, values):
    plt.text(x, y + 0.4, f"{y:.2f}", ha='center', fontsize=9)
plt.title("Quarterly MRR Growth vs Industry Benchmark")
plt.ylabel("MRR Growth (%)")
plt.ylim(0, max(INDUSTRY_BENCHMARK + 5, values.max() + 5))
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

output_file = os.path.join(OUTPUT_DIR, "mrr_trend.png")
plt.savefig(output_file, dpi=150)
print(f"Saved plot to: {output_file}")
