import json
import chess
import chess.engine

lc0_path = "/usr/local/bin/lc0"
lc0_weights = "/usr/local/Cellar/lc0/0.31.2/libexec/42850.pb.gz"
stockfish_path = "/Users/brian/Desktop/COSC Research Paper/stockfish/stockfish-macos-m1-apple-silicon"
input_path = "phase_fens.json"
output_path = "lc0_move_with_stockfish_eval.json"
nodes = 50
depth = 15

with open(input_path) as f:
    fens = json.load(f)

results = []

with chess.engine.SimpleEngine.popen_uci(lc0_path) as lc0_engine, \
     chess.engine.SimpleEngine.popen_uci(stockfish_path) as sf_engine:

    lc0_engine.configure({"WeightsFile": lc0_weights})

    for entry in fens:
        fen = entry["fen"]
        phase = entry["phase"]
        game_id = entry["game_id"]

        try:
            board = chess.Board(fen)
            lc0_move = lc0_engine.play(board, chess.engine.Limit(nodes=nodes)).move #Lc0's best move
            if lc0_move not in board.legal_moves:
                sf_eval = None
            else:
                board.push(lc0_move) # Makes the move
                info = sf_engine.analyse(board, chess.engine.Limit(depth=depth))
                sf_eval = info["score"].white().score(mate_score=10000) # Evaluates the position with stockfish analysis
            results.append({
                "game_id": game_id,
                "fen": fen,
                "phase": phase,
                "lc0_move": lc0_move.uci(),
                "stockfish_eval_on_lc0_move": sf_eval
            })

        except Exception as e:
            print(f"Error on FEN {fen}: {e}")

with open(output_path, "w") as f:
    json.dump(results, f, indent=2)

print("Lc0 Evaluation Complete")