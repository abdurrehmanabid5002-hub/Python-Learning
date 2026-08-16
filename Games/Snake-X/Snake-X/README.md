# 🐍 Snake X

A polished, modular Snake game built with Python and Pygame to demonstrate Data Structures, Algorithms, OOP, and clean project architecture.

## Features
- `deque` for O(1) head/tail snake operations
- `set` for O(1) average collision membership checks
- Progressive levels and speed
- Persistent high score
- Pause/restart/quit controls
- WASD and arrow-key controls
- Clean modules and no external assets required

## Project structure
```text
Snake-X/
├── main.py
├── game.py
├── snake.py
├── food.py
├── settings.py
├── requirements.txt
├── .gitignore
├── assets/
│   ├── sounds/
│   └── images/
├── data/
│   └── highscore.txt
└── README.md
```

## Run on Windows
```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python main.py
```

## Controls
- `W` / `↑` Up
- `S` / `↓` Down
- `A` / `←` Left
- `D` / `→` Right
- `SPACE` Pause/Resume
- `R` Restart
- `ESC` Quit

## DSA notes
The snake is modeled as a `deque`, so inserting a new head and removing the tail are O(1). A companion `set` stores occupied cells, making average membership checks O(1).

## Future upgrades
Sound effects, main menu, difficulty selection, obstacles, power-ups, animated food, local leaderboards, unit tests, and executable packaging can be added without changing the overall architecture.
