import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open("stockfish_phase_eval.json") as f:
    sf_data = json.load(f)

with open("komodo_move_with_stockfish_eval.json") as f:
    komodo_data = json.load(f)

assert len(sf_data) == len(komodo_data), "Mismatch in number of FENs!"

results = []
for sf_entry, komodo_entry in zip(sf_data, komodo_data):
    assert sf_entry["fen"] == komodo_entry["fen"] and sf_entry["phase"] == komodo_entry["phase"], "FEN or phase mismatch!"

    move_match = sf_entry["best_move"] == komodo_entry["komodo_move"]
    eval_diff = sf_entry["eval_after_move"] - komodo_entry["stockfish_eval_on_komodo_move"]

    results.append({
        "fen": sf_entry["fen"],
        "phase": sf_entry["phase"],
        "best_move_sf": sf_entry["best_move"],
        "komodo_move": komodo_entry["komodo_move"],
        "eval_diff": eval_diff
    })

df = pd.DataFrame(results)

summary = df.groupby("phase").agg(
    total=("fen", "count"),
    avg_eval_diff=("eval_diff", "mean")
).reset_index()

overall = {
    "total": len(df),
    "avg_eval_diff": round(df["eval_diff"].mean(), 2)
}

print("Summary by Phase:")
print(summary)
print("Overall Summary:")
for k, v in overall.items():
    print(f"{k}: {v}")

plt.figure(figsize=(8, 5))
sns.set(style="whitegrid")

filtered = df["eval_diff"].dropna()
filtered = filtered[(filtered > -200) & (filtered < 200)]
bins = list(range(-200, 210, 10))  # From -200 to 200 by 10

#plot
ax = sns.histplot(filtered, bins=bins, kde=True, color="lightgreen", edgecolor="black")

for patch in ax.patches:
    height = patch.get_height()
    if height > 0:
        ax.annotate(f'{int(height)}',
                    (patch.get_x() + patch.get_width() / 2, height),
                    ha='center', va='bottom', fontsize=8)

plt.title("Stockfish Evaluation Difference (SF - Komodo Move)")
plt.xlabel("Centipawn Difference")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("eval_diff_histogram_komodo_with_counts.png")
plt.show()

#table
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
plt.savefig("phase_eval_summary_table_sf_komodo.png", dpi=300)
plt.close()

