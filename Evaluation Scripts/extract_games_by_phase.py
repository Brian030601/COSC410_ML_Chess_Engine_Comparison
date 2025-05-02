import chess.pgn
import json
import random

pgn_path = "/Users/brian/Desktop/COSC Research Paper/SemiTarraschMain.pgn"
output_path = "phase_fens.json"
target_per_phase = 200
phases = [("opening", 4), ("midgame", 20), ("endgame", 60)] # get positions after these plies

all_games = []

with open(pgn_path) as pgn_file:
    while True:
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break
        all_games.append(game)

random.shuffle(all_games)

phase_fens = {phase: [] for phase, _ in phases}

for game in all_games:
    if all(len(phase_fens[p]) >= target_per_phase for p, _ in phases):
        break  # stop after reaching target

    board = game.board()
    plies = list(game.mainline_moves())
    site = game.headers.get("Site", "unknown_site")

    for phase, ply_index in phases:
        if len(plies) > ply_index and len(phase_fens[phase]) < target_per_phase:
            board.reset()
            for i in range(ply_index + 1):
                board.push(plies[i])
            fen = board.fen()
            phase_fens[phase].append({
                "game_id": site,
                "fen": fen,
                "phase": phase
            })

all_fens = []
for fens in phase_fens.values():
    all_fens.extend(fens)

with open(output_path, "w") as f:
    json.dump(all_fens, f, indent=2)

print("200 FENs per phase from random games.")