# COSC410_ML_Chess_Engine_Comparison

# Phase Four: Final Artifact

Here is the link to the Github Repo: https://github.com/Brian030601/COSC410_ML_Chess_Engine_Comparison.git

## Overview

Using Stockfish’s centipawn evaluation as the common benchmark, this project compares the strategic quality of three different chess engines—Stockfish, Leela Chess Zero (Lc0), and Komodo Dragon 1—across different phases of a game: opening, midgame, and endgame. Additionally, the project analyzes how each engine performs in terms of move quality and head-to-head matches under timed conditions. 

The project findings show that Stockfish consistently selects stronger moves according to its own evaluations. However, Lc0 performs better than Komodo in untimed evaluation contexts, while Komodo is more resilient under strict time constraints. Overall, while Stockfish dominates in both speed and accuracy, Lc0 has more potential to improve given more time, and Komodo is the most stable.

## Replication Instructions

### 1. Download the Dataset
- Download PGN game data from the [Lichess Open Database](https://database.lichess.org/#standard_games). The project used `lichess_db_standard_rated_2013-01.pgn.zst`, which is uploaded in `Chess Data` folder.
- Unzip the file to get SemiTarraschMain.pgn, which is also uploaded in the `Chess Data` folder.

### 2. Extract Game Positions
- Run `extract_games_by_phase.py` in the `Evaluation Scripts` folder.
- This script extracts 600 FENs (positions) or 200 FENs per phase across opening, midgame, and endgame.
- The output is named `phase_fens.json`, and it is located in `Chess Data` folder.

### 3. Set Up Engines
- Download and place the following engines in the `Chess Engines/` folder:
  - [Stockfish 16](https://stockfishchess.org/download/)
  - [Leela Chess Zero (Lc0)](https://lczero.org/play/)
  - [Komodo Dragon 1](https://komodochess.com/)
-  Note: Update paths in all scripts to point to your local engine executables and weights files (Lc0).

### 4. **Run Engine Evaluations**
- Run the following scripts in order:
  - `evaluate_stockfish_by_phase.py`
  - `evaluate_lc0_by_phase.py`
  - `evaluate_komodo_by_phase.py`

Outputs:
- `stockfish_phase_eval.json`
- `lc0_move_with_stockfish_eval.json`
- `komodo_move_with_stockfish_eval.json`

### 5. **Run Engine Comparisons**
In the `Comparison Scripts/` folder, run:
- `compare_lc0_stockfish_by_phase.py`
- `compare_komodo_stockfish_by_phase.py`
- `compare_lc0_komodo_by_phase.py`
- `plot_move_agreement.py`

### 6. **Run Head-to-Head Matches (Optional but Encouraged)**
Use the `head_to_head_match.py` scripts to simulate 10-game matches between:
- Stockfish vs. Lc0
- Stockfish vs. Komodo
- Lc0 vs. Komodo

## 🧪 Future Directions

To build on this project:
- Test engine performance under **varied time controls** (e.g., 0.1s, 1s, 5s per move)
- Benchmark engine evaluations using their own scoring functions
- Include **human grandmaster games** for engine-human comparison
- Explore **hybrid symbolic-neural engines** as baselines

## 👥 Contributions

**Brian Kherlen** (solo contributor)
- Developed codebase, evaluated all engines, built comparison framework, wrote final poster.
- Estimated time spent: **60–70 hours**.
