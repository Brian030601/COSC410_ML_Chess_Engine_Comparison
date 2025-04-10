import json
import chess
import chess.engine

stockfish_path = "/Users/brian/Desktop/COSC Research Paper/stockfish/stockfish-macos-m1-apple-silicon"
input_path = "phase_fens.json"
output_path = "stockfish_phase_eval.json"
depth = 15  # for analysis

with open(input_path) as f:
    fens = json.load(f)

results = []

with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
    for entry in fens:
        fen = entry["fen"]
        phase = entry["phase"]
        game_id = entry["game_id"]

        try:
            board = chess.Board(fen)
            best_move = engine.play(board, chess.engine.Limit(depth=depth)).move # stockfish's best move
            if best_move in board.legal_moves:
                board.push(best_move) # makes the move
                info = engine.analyse(board, chess.engine.Limit(depth=depth))
                eval_score = info["score"].white().score(mate_score=10000) # evluate with stockfish after the move
            else:
                eval_score = None
            results.append({
                "game_id": game_id,
                "fen": fen,
                "phase": phase,
                "best_move": best_move.uci(),
                "eval_after_move": eval_score
            })
        except Exception as e:
            print(f"Error evaluating FEN: {fen}\n{e}")

with open(output_path, "w") as f:
    json.dump(results, f, indent=2)

print("Stockfish Evaluation Complete")