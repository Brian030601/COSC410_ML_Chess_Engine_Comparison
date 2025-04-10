import json
import chess
import chess.engine

komodo_path = "/Users/brian/Desktop/COSC Research Paper/dragon_05e2a7/OSX/dragon-osx"
stockfish_path = "/Users/brian/Desktop/COSC Research Paper/stockfish/stockfish-macos-m1-apple-silicon"
input_path = "phase_fens.json"
output_path = "komodo_move_with_stockfish_eval.json"
komodo_depth = 15
stockfish_depth = 15

with open(input_path) as f:
    fens = json.load(f)

results = []

with chess.engine.SimpleEngine.popen_uci(komodo_path) as komodo_engine:
    for entry in fens:
        fen = entry["fen"]
        phase = entry["phase"]
        game_id = entry["game_id"]

        board = chess.Board(fen)

        try:
            komodo_move = komodo_engine.play(board, chess.engine.Limit(depth=komodo_depth)).move # Get Komodo's Best move
            if komodo_move is None or komodo_move not in board.legal_moves:
                continue
            board.push(komodo_move) # Makes the move

            with chess.engine.SimpleEngine.popen_uci(stockfish_path) as sf_engine:
                info = sf_engine.analyse(board, chess.engine.Limit(depth=stockfish_depth))
                eval_score = info["score"].white().score(mate_score=10000) # Evaluates the position with Stockfish

            results.append({
                "game_id": game_id,
                "fen": fen,
                "phase": phase,
                "komodo_move": komodo_move.uci(),
                "stockfish_eval_on_komodo_move": eval_score
            })

        except Exception as e:
            print(f"Error for FEN {fen}: {e}")

with open(output_path, "w") as f:
    json.dump(results, f, indent=2)

print("Komodo Evaluation Complete")