# COSC410_ML_Chess_Engine_Comparison

This project compares Leela Chess Zero and Komodo Dragon 1 to Stockfish chess engine and evaluates their  best moves on Stockfish Analysis Engine. Based on the analysis, the project ranks the three chess engines and plays head to head matches with one another under different situations. 

# First Step - Data Collection / Extraction

More than 100,000 chess games in a notation known as PGNs have been downloaded from Lichess Open Database: https://database.lichess.org/#standard_games. The data is downloaded and uploaded in Chess Data folder as lichess_db_standard_rated_2013-01.pgn.zst. Then, the data is unzipped and and 200 positions from each phase have been selected randomly. The phases are opening, midgame, and endgame. All the phases are selected from white's perspective. Opening is white's 3rd move, midgame is white's 11th move, and endgame is white's 31st move. The phases and positions are selected from only white's movement so the comparison of centipawn losses will be consistent. So, total of 600 positions or known as FENs have been extracted in phase_fens.json through extract_games_by_phase.py script in Evaluation Scripts.  This dataset of 600 positions have been used for Stockfish vs Lc0, Stockfish vs Komodo, and Lc0 vs Komodo comparisons and evaluations. The source files and download links for the engines are provided in Chess Engines folder.

# Second Step - Engine Analysis

Initially, the randomly selected 600 positions (200 in each phase of the game) gets analyzed by Stockfish chess engine.  The Stockfish engine produces the best move given the position. Then, after making the best move of the engine, the Stockfish Anlysis Engine evaluates the position and produces the evaluation in centipawn (a unit of measure, equal to 1/100th of a pawn, used to evaluate the strategic advantage or disadvantage of a position). After the stockfish analysis, the same process is repeated for Lc0 and Komodo engines and gets analysed by Stockfish Analysis. From the three analysis, the project get Stockfish's best move and it's analysis of the position after the best move, Lc0's best move and Stockfish's analysis of the position after the best move, and Komodo's best move and Stockfish's analysis of the position after the best move. Now they analysis and evaluations are ready for comparison. The analysis results are saved in Engine Evaluation Results file. Each result has their own folder.

# Third Step - Engine Comparison

After the engine analysis, each engines are compared to one another based on the Stockfish's Analysis of the position and the best move. The comparison scripts are in the file "Comparison Script." The comparison scripts are run on json files that are outputed from the engine analysis (Engine Evaluation Results) which has the best move and the centipawn valuation of each engine. Firstly, Lc0 and Stockfish are compared using the following script "compare_lc0_stockfish_by_phase.py". The results are saved in Comparison Results. There is a historgram and table saved from the script. The similar script "compare_komodo_stockfish_by_phase.py" and "compare_komodo_lc0_by_phase.py" are also run to get a histogram and a table of summary and comparison. Finally, the "plot_move_agreement.py" is run to get movement agreement between the three engines compared to stockfish. 

# Results

Based on the initial discovery. Stockfish performs better compared to both Lc0 and Komodo engines. Lc0 comes in second and Komodo in last. Based on centipawn analysis of 600 positions, Stockfish found the better move in 289 positions compared to Lc0. Lc0 found the better move in 281, and they found equal move in 30 positions according to Stockfish's centipawn analysis. Secondly, Stockfish found the better move in 355 positions compared to Komodo. Komodo found the better move in 218 and they found the euqal move in 27 positions according to Stockfish's centipawn analysis. Finally, Lc0 found the better move in 361 positions compared to Komodo. Komodo found the better move in 212 and they found the euqal move in 27 positions according to Stockfish's centipawn analysis. As previously states, the Stockfish centipawn analysis suggest that Stockfish is the strongest engine from the three of them. Additionally, Stockfish analysis was able to identify situations when other engines suggested the better move than it did. 

As for best movement agreement, Komodo found the same best move 80.5% of the time as Stockfish did in the opening. Lc0 did 81.5% of the time in the opening. As for midgame, Komodo found the same best move 56.5% of the time as Stockfish did and Lc0 found the same best move 56% of the times. As for endgame, Komodo found the same best move 65.5% and Lc0 found the same best move 53.5% of the times as Stockfish did. So from the agreement, we can see that the engines agree with each other's best moves most of the times in opening and varies from there on. 

# Future Directions

In the future, the project will look into head to head matches between the three engines under different time constraints. That way, the project will be able to see which engine runs faster and makes the best evaluations. 

Additionally, the project will look at opening, midgame, and endgame centipawn valuation differences and see which engine is better at which phase. 

# Project Replication

To replicate the project, the paths for file and engine location needs to be modified.