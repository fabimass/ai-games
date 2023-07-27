# AI Minesweeper

The goal of this project is to build an AI that can play Minesweeper. It will be done using a knowledge-based agent that will make decisions by considering its knowledge base, and making inferences based on that knowledge.

We'll represent each sentence of our AI's knowledge like the below:

```
{A, B, C, D, E, F, G, H} = 1
```

Every logical sentence in this representation has two parts: a set of `cells` on the board that are involved in the sentence, and a number `count`, representing the count of how many of those cells are mines. The above logical sentence says that out of cells A, B, C, D, E, F, G, and H, exactly 1 of them is a mine.

- Any time we have a sentence whose `count` is 0, we know that all of that sentence's cells must be safe.
- Any time the number of `cells` is equal to the `count`, we know that all of that sentence's cells must be mines.
- Any time we have two sentences `set1` = `count1` and `set2` = `count2` where `set1` is a subset of `set2`, then we can construct the new sentence `set2 - set1 = count2 - count1`.

There are two main files in this project: `minesweeper.py` contains all of the logic the game itself and for the AI to play the game. `runner.py` contains all of the code to run the graphical interface for the game.

There are three classes defined in `minesweeper.py`, `Minesweeper`, which handles the gameplay; `Sentence`, which represents a logical sentence that contains both a set of `cells` and a `count`; and `MinesweeperAI`, which handles inferring which moves to make based on knowledge.

The `Sentence` class will be used to represent logical sentences of the form described previously. Each sentence has a set of `cells` within it and a `count` of how many of those cells are mines. The class also contains functions `known_mines` and `known_safes` for determining if any of the cells in the sentence are known to be mines or known to be safe. It also contains functions `mark_mine` and `mark_safe` to update a sentence in response to new information about a cell.

Finally, the `MinesweeperAI` class will implement an AI that can play Minesweeper. The AI class keeps track of a number of values. `self.moves_made` contains a set of all cells already clicked on, so the AI knows not to pick those again. `self.mines` contains a set of all cells known to be mines. `self.safes` contains a set of all cells known to be safe. And `self.knowledge` contains a list of all of the Sentences that the AI knows to be true.

The `mark_mine` function adds a cell to `self.mines`, so the AI knows that it is a mine. It also loops over all sentences in the AI's knowledge base and informs each sentence that the cell is a mine, so that the sentence can update itself accordingly if it contains information about that mine. The `mark_safe` function does the same thing, but for safe cells instead.

The `add_knowledge` function will receive a cell and its corresponding count, and will update `self.mines`, `self.safes`, `self.moves_made`, and `self.knowledge` with any new information that the AI can infer, given that cell is known to be a safe cell with count mines neighboring it.