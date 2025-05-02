import chess
import chess.engine
import matplotlib.pyplot as plt

#Engine paths
komodo_path = "/Users/brian/Desktop/COSC Research Paper/dragon_05e2a7/OSX/dragon-osx"
lc0_path = "/usr/local/bin/lc0"
lc0_weights = "/usr/local/Cellar/lc0/0.31.2/libexec/42850.pb.gz"

time_per_move = 2.5  # seconds per ply
max_moves = 100      # full moves (200 plies)
num_games = 10

results = {
    "Komodo": 0,
    "Lc0": 0,
    "Draw": 0
}
game_records = []

for game_num in range(num_games):
    board = chess.Board()

    if game_num % 2 == 0: # Alternate sides
        engines = ["Komodo", "Lc0"]
    else:
        engines = ["Lc0", "Komodo"]

    print(f"\n=== Game {game_num + 1}: {engines[0]} (White) vs {engines[1]} (Black) ===")

    with chess.engine.SimpleEngine.popen_uci(komodo_path) as komodo_engine, \
         chess.engine.SimpleEngine.popen_uci(lc0_path) as lc0_engine:

        lc0_engine.configure({"WeightsFile": lc0_weights})
        engine_map = {
            "Komodo": komodo_engine,
            "Lc0": lc0_engine
        }

        move_count = 0
        moves_list = []

        while not board.is_game_over() and move_count < 2 * max_moves:
            engine_index = move_count % 2
            engine_name = engines[engine_index]
            engine = engine_map[engine_name]

            try:
                result = engine.play(board, chess.engine.Limit(time=time_per_move))
                board.push(result.move)
                moves_list.append((engine_name, result.move.uci()))
                move_count += 1
            except Exception as e:
                print(f"Error on move {move_count} by {engine_name}: {e}")
                break

        outcome = board.result()
        print(f"Result: {outcome}")
        print("Final position:\n", board)

        if outcome == "1-0":
            winner = engines[0]
            results[winner] += 1
        elif outcome == "0-1":
            winner = engines[1]
            results[winner] += 1
        else:
            results["Draw"] += 1

        game_records.append({
            "game": game_num + 1,
            "white": engines[0],
            "black": engines[1],
            "result": outcome,
            "moves": moves_list
        })

print("\n Final Score After 10 Games:")
for k, v in results.items():
    print(f"{k}: {v}")

plt.figure(figsize=(6, 4))
plt.bar(results.keys(), results.values(), color=["mediumseagreen", "deepskyblue", "gray"])
plt.title("Komodo vs. Lc0 – Match Results")
plt.ylabel("Number of Games")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("2.5s_komodo_vs_lc0_match_results.png")
plt.show()