import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open("lc0_move_with_stockfish_eval.json") as f:
    lc0_data = json.load(f)

with open("komodo_move_with_stockfish_eval.json") as f:
    komodo_data = json.load(f)

assert len(lc0_data) == len(komodo_data), "Mismatch in number of FENs!" #One-to-One Comparison

results = []
for lc0_entry, komodo_entry in zip(lc0_data, komodo_data):
    assert lc0_entry["fen"] == komodo_entry["fen"] and lc0_entry["phase"] == komodo_entry["phase"], "FEN or phase mismatch!"
    eval_diff = lc0_entry["stockfish_eval_on_lc0_move"] - komodo_entry["stockfish_eval_on_komodo_move"]
    results.append({
        "fen": lc0_entry["fen"],
        "phase": lc0_entry["phase"],
        "lc0_move": lc0_entry["lc0_move"],
        "komodo_move": komodo_entry["komodo_move"],
        "eval_diff": eval_diff  # If positive, Lc0's move is better than Stockfish
    })

df = pd.DataFrame(results)

summary = df.groupby("phase").agg(
    total=("fen", "count"),
    avg_eval_diff=("eval_diff", "mean")
).reset_index()

overall = {
    "total": len(df),
    "lc0_better": int((df["eval_diff"] > 0).sum()),
    "komodo_better": int((df["eval_diff"] < 0).sum()),
    "equal": int((df["eval_diff"] == 0).sum()),
    "avg_eval_diff": round(df["eval_diff"].mean(), 2)
}

print("Summary by Phase:")
print(summary)
print("verall Summary:")
for k, v in overall.items():
    print(f"{k}: {v}")

plt.figure(figsize=(8, 5))
sns.set(style="whitegrid")

filtered = df["eval_diff"].dropna()
filtered = filtered[(filtered > -200) & (filtered < 200)]
bins = list(range(-200, 210, 10))  #bin by 10s

# plot
ax = sns.histplot(filtered, bins=bins, kde=True, color="plum", edgecolor="black") 

for patch in ax.patches:
    height = patch.get_height()
    if height > 0:
        ax.annotate(f'{int(height)}',
                    (patch.get_x() + patch.get_width() / 2, height),
                    ha='center', va='bottom', fontsize=8)

plt.title("Stockfish Evaluation Difference (Lc0 - Komodo)")
plt.xlabel("Centipawn Difference")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("eval_diff_lc0_vs_komodo.png")
plt.show()

# table
fig, ax = plt.subplots(figsize=(5, 1.5))  # Adjusting size
ax.axis('off')
table = ax.table(cellText=summary.values,
                 colLabels=summary.columns,
                 cellLoc='center',
                 loc='center')
table.scale(1.2, 1.5)
table.auto_set_font_size(False)
table.set_fontsize(12)

plt.tight_layout()
plt.savefig("phase_eval_summary_table_lc0_komodo.png", dpi=300)
plt.close()
