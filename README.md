
# Mastermind

Welcome to **Mastermind**, a classic code-breaking game! The objective of the game is to guess a secret code within a limited number of attempts. The code is composed of a sequence of colors, and your goal is to deduce the correct sequence based on feedback provided after each guess.

## Table of Contents

- [Overview](#overview)
- [How to Play](#how-to-play)
- [Game Modes](#game-modes)
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

Mastermind is a logic-based puzzle game that challenges players to crack a secret code. The game offers varying difficulty levels, allowing both beginners and experts to enjoy the challenge. The game can be played against the computer or with two players.

## How to Play

1. **Objective**: The computer will randomly generate a secret code consisting of a sequence of colors. Your task is to guess the correct sequence.

2. **Input**: For each guess, you will input a sequence of colors. The length of the sequence and the number of available colors depend on the difficulty level.

3. **Feedback**: After each guess, the game will provide feedback in the form of:
   - **Black Peg**: A correct color in the correct position.
   - **White Peg**: A correct color but in the wrong position.
   - **No Peg**: A color that doesn't exist in the secret code.

4. **Winning**: You win the game if you guess the exact code sequence within the allowed number of attempts.

5. **Losing**: If you fail to guess the code within the allowed attempts, the game will reveal the correct sequence, and you lose the game.

## Game Modes

- **Single Player**: Play against the computer. The computer generates the secret code.
- **Two Player**: One player sets the secret code, and the other tries to guess it.

## Installation

To install and run the Mastermind game, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mastermind.git
   ```

2. Navigate to the project directory:
   ```bash
   cd mastermind
   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

To start the game, simply run the main script:

```bash
python mastermind.py
```

Follow the on-screen instructions to start playing!

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name:
   ```bash
   git checkout -b feature-new-feature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-new-feature
   ```
5. Open a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions, suggestions, or issues, feel free to contact me:

- **Name**: Alireza Mehraban
- **Email**: [mr.kind1382@gmail.com](mailto:mr.kind1382@gmail.com)

Happy gaming!
