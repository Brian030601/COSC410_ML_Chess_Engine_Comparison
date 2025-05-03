# COSC410_ML_Chess_Engine_Comparison

# Phase Four: Final Artifact

Here is the link to the Github Repo: https://github.com/Brian030601/COSC410_ML_Chess_Engine_Comparison.git

## Overview

Using Stockfish’s centipawn evaluation as the common benchmark, this project compares the strategic quality of three different chess engines—Stockfish, Leela Chess Zero (Lc0), and Komodo Dragon 1—across different phases of a game: opening, midgame, and endgame. Additionally, the project analyzes how each engine performs in terms of move quality and head-to-head matches under timed conditions. 

The project findings show that Stockfish consistently selects stronger moves according to its own evaluations. However, Lc0 performs better than Komodo in untimed evaluation contexts, while Komodo is more resilient under strict time constraints. Overall, while Stockfish dominates in both speed and accuracy, Lc0 has more potential to improve given more time, and Komodo is the most stable.

## Replication Instructions

Note: Update paths in all scripts to point to your local files in replication process as the project owner's own file and folder paths are used in this project and scripts. 

### 1. Download the Dataset
- Download PGN game data from the [Lichess Open Database](https://database.lichess.org/#standard_games). The project used `lichess_db_standard_rated_2013-01.pgn.zst`, which is uploaded in `Chess Data` folder.
- Unzip the file to get SemiTarraschMain.pgn, which is also uploaded in the `Chess Data` folder.

### 2. Extract Game Positions
- Run `extract_games_by_phase.py` in the `Evaluation Scripts` folder.
- This script extracts 600 FENs (positions) or 200 FENs per phase across opening, midgame, and endgame.
- The output is named `phase_fens.json`, and it is located in `Chess Data` folder.

### 3. Set Up Engines
- Download the Stockfish, Leela Chess Zero, and Komodo Dragon engines from the below links:
  - [Stockfish 16](https://stockfishchess.org/download/)
  - [Leela Chess Zero (Lc0)](https://lczero.org/play/)
  - [Komodo Dragon 1](https://komodochess.com/)
-  Note: Update paths in all scripts to point to your local engine executables and weights files (Lc0).

### 4. Run Engine Evaluations
- Run the following scripts in order in the `Evaluation Scripts` folder:
  - `evaluate_stockfish_by_phase.py` to get Stockfish's own evaluation on its move.
  - `evaluate_lc0_by_phase.py` to get Stockfish's evaluation on Lc0's move.
  - `evaluate_komodo_by_phase.py` to get Stockfish's evaluation on Komodo's move.

Outputs are stored in the `Engine Evaluation Results` folder under the following names:
- `stockfish_phase_eval.json` for Stockfish's own evaluation on its move. 
- `lc0_move_with_stockfish_eval.json` for Stockfish's evaluation on Lc0's move.
- `komodo_move_with_stockfish_eval.json` for Stockfish's evaluation on Komodo's move.

### 5. Run Engine Comparisons
In the `Comparison Scripts/` folder, run:
- `compare_lc0_stockfish_by_phase.py` to see which engine (Stockfish vs Lc0) does better on the 600 positions and get a graph.
- `compare_komodo_stockfish_by_phase.py` to see which engine (Stockfish vs Komodo) does better on the 600 positions and get a graph.
- `compare_lc0_komodo_by_phase.py` to see which engine (Lc0 vs Komodo) does better on the 600 positions and get a graph.
- `plot_move_agreement.py` to get Lc0 and Komodo's move agreement with Stockfish.

Outputs are stored in the `Comparison Results` folder under the following names:
`eval_diff_histogram_sf_vs_lc0.png` for total evaluation difference between SF vs Lc0.
`eval_diff_histogram_sf_vs_komodo.png` for total evaluation difference between SF vs Komodo.
`eval_diff_lc0_vs_komodo.png` for total evaluation difference between Lc0 vs Komodo.
`move_agreement_by_phase_3engines.png` for Lc0 and Komodo's move agreement with Stockfish.
`phase_eval_summary_table_sf_lc0.png` for phase evaluation difference between SF vs Lc0.
`phase_eval_summary_table_sf_komodo.png` for phase evaluation difference between SF vs Komodo.
`phase_eval_summary_table_lc0_komodo.png` for phase evaluation difference between Lc0 vs Komodo.

### 6. Run Head-to-Head Matches
In the `Head-to-Head Script` folder, run:
- `Lc0_vs_SF.py` to get the 10 head-to-head match result between Lc0 and Stockfish. You can change `time_per_move` to = 0.5 and 2.5 to replicate the project. 
- `Komodo_vs_SF.py` to get the 10 head-to-head match result between Komodo and Stockfish. You can change `time_per_move` to = 0.5 and 2.5 to replicate the project. 
- `Komodo_vs_Lc0.py` to get the 10 head-to-head match result between Komodo and Lc0. You can change `time_per_move` to = 0.5 and 2.5 to replicate the project. 

Outputs are stored in the `Head-to_head Results` folder in their respective names. 

## Future Directions

To build on this project:
- Test engine performance under varied time controls to increase sample size and robustness of head-to-head matches. To do so, you can change `time_per_move` to 0.1s, 0.25s, 1s, 2s, 5s per move in `Lc0_vs_SF.py`, `Komodo_vs_SF.py`, and `Komodo_vs_Lc0.py`.
- Benchmark engine evaluations using other engines such as Lc0's or Komodo's evaluation functions to avoid Stockfish bias. In each of `evaluate_stockfish_by_phase.py`, `evaluate_lc0_by_phase.py`, and `evaluate_komodo_by_phase.py`, you can use Komodo's or Lc0's evaluation metrics instead of Stockfish's for all three of them.
- Include human grandmaster (2600+ Elo) games in the dataset for engine-human comparison, which will require handpicked dataset. 

## Contributions

**Brian Kherlen**: I am the solo group member. I did the following:
- Downloaded dataset, developed codebase, evaluated all engines, built comparison framework, created head-to-head matches, and created final poster.
- Estimated time spent: **50–70 hours**.
