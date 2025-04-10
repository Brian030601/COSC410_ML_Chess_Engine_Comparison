import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open("Previous4/stockfish_phase_eval.json") as f:
    sf_data = json.load(f)
with open("Previous4/lc0_move_with_stockfish_eval.json") as f:
    lc0_data = json.load(f)
with open("Previous4/komodo_move_with_stockfish_eval.json") as f:
    komodo_data = json.load(f)

assert len(sf_data) == len(lc0_data) == len(komodo_data)
for sf, lc, kd in zip(sf_data, lc0_data, komodo_data):
    assert sf["fen"] == lc["fen"] == kd["fen"]
    assert sf["phase"] == lc["phase"] == kd["phase"]

results = []
for sf, lc, kd in zip(sf_data, lc0_data, komodo_data):
    results.append({
        "fen": sf["fen"],
        "phase": sf["phase"],
        "move_match_sf": True,  # Stockfish always matches itself
        "move_match_lc0": sf["best_move"] == lc["lc0_move"],
        "move_match_komodo": sf["best_move"] == kd["komodo_move"]
    })

df = pd.DataFrame(results)

min_count = df["phase"].value_counts().min()
df_balanced = (
    df.groupby("phase", group_keys=False)
    .apply(lambda g: g.sample(n=min_count, random_state=42))
    .reset_index(drop=True)
)

summary = []
for phase in df_balanced["phase"].unique():
    subset = df_balanced[df_balanced["phase"] == phase]
    summary.append({
        "phase": phase,
        "engine": "Lc0",
        "match_pct": round(100 * subset["move_match_lc0"].mean(), 1)
    })
    summary.append({
        "phase": phase,
        "engine": "Komodo",
        "match_pct": round(100 * subset["move_match_komodo"].mean(), 1)
    })
    summary.append({
        "phase": phase,
        "engine": "Stockfish",
        "match_pct": 100.0  # Stockfish is 100%
    })

summary_df = pd.DataFrame(summary)

phase_order = ["opening", "midgame", "endgame"]
summary_df['phase'] = pd.Categorical(summary_df['phase'], categories=phase_order, ordered=True)

engine_order = ["Lc0", "Komodo", "Stockfish"]
summary_df['engine'] = pd.Categorical(summary_df['engine'], categories=engine_order, ordered=True)

summary_df = summary_df.sort_values(["phase", "engine"])

plt.figure(figsize=(8, 5))
sns.set(style="whitegrid")
palette = {
    "Lc0": "#1f77b4",      # blue
    "Komodo": "#ff7f0e",    # orange
    "Stockfish": "#2ca02c"  # green
}

barplot = sns.barplot(data=summary_df, x="phase", y="match_pct", hue="engine", palette=palette, hue_order=engine_order)

for i, row in summary_df.iterrows():
    group_index = phase_order.index(row['phase'])
    engine_index = engine_order.index(row['engine'])
    x_pos = group_index - 0.3 + 0.3 * engine_index
    y_pos = row["match_pct"] - 0.6  # Increased to avoid gridlines

    barplot.text(
        x=x_pos,
        y=y_pos,
        s=f"{row['match_pct']}%",
        ha="center",
        va="bottom",
        fontsize=9,
        fontweight="bold"
    )

plt.title("Move Agreement with Stockfish")
plt.ylabel("Match %")
plt.xlabel("Game Phase")
plt.ylim(0, 119)  # Increased to make room for labels
plt.legend(title="Engine", loc='upper left')
plt.tight_layout()
plt.savefig("move_agreement_by_phase_3engines.png")
plt.show()