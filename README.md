# SOS Game with AI Player

## Overview
This project implements a modified version of the SOS game, where players aim to create SOS sequences on a 5x5 grid board. The game can be played between human players, between human and AI players, or between AI players. The AI player is implemented using minimax or negamax with alpha-beta pruning, with a tree depth of 4-ply. Additionally, two evaluation (heuristic) methods, namely h1 and h2, are provided for the AI player.

## Features
- Implementation of SOS game on a maximum of 10x10 grid board
- Support for human vs human, human vs AI, and AI vs AI gameplay
- AI player using minimax or negamax with alpha-beta pruning
- Two evaluation methods (h1 and h2) for the AI player
- Text-based interface for gameplay
- Recording of maximum time required to find the best move
- Video recordings for AI vs AI and Human vs AI gameplay configurations

## Project Structure
- `src/`: Contains the source code for the SOS game and AI player implementation
- `docs/`: Includes the design document describing the classes, fields, methods, and evaluation methods used in the project

## Usage
Execute main.py file.
