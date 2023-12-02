1. `from pathlib import Path`: Imports the `Path` class from the `pathlib` module to handle file paths in a cleaner way.

2. `import re`: Imports the `re` module to work with regular expressions.

3. `gameRegex = re.compile(r"Game (\d+): (.*)$")`: Compiles a regular expression to search for specific patterns in lines of the file. This regex searches for a line that starts with "Game," followed by a number (\d+) representing the game number, then ":" and captures the rest of the line (`(.*)`).

4. `colorRegex = re.compile(r"(\d+) (.*)")`: Another regular expression that searches for patterns in colors. It captures a number (\d+) followed by a space, then captures the rest of the line (`(.*)`).

5. `limits = {"red": 12, "green": 13, "blue": 14}`: Sets limits for the red, green, and blue colors.

6. `def part1(line):`: Defines a function `part1` that takes a line as input and performs specific checks on colors.

7. `match = gameRegex.search(line)`: Uses the `gameRegex` to find matches in the current line.

8. `for color in match[2].replace(";", ",").split(", "):`: Iterates over the colors extracted from the second part of the regex match.

9. `colorMatch = colorRegex.search(color)`: Uses the `colorRegex` to extract specific information about the color.

10. `if int(colorMatch[1]) > limits[colorMatch[2]]:`: Checks if the color value exceeds the defined limit.

11. `return int(match[1])`: If no color exceeds the limits, returns the game number.

12. `def part2(line):`: Defines a function `part2` similar to `part1` but with different logic.

13. `minimas = {"red": 0, "green": 0, "blue": 0}`: Initializes a dictionary to store minimum values for each color.

14. `for color in match[2].replace(";", ",").split(", "):`: Iterates over the colors as in `part1`.

15. `value = int(colorMatch[1])`: Extracts the color value.

16. `color = colorMatch[2]`: Extracts the color name.

17. `if value > minimas[color]:`: Updates the minimum value if the current value is greater.

18. `return minimas["red"] * minimas["green"] * minimas["blue"]`: Returns the product of the minimum values for the three colors.

19. `path = Path(__file__).parent / "day2.txt"`: Builds the path to the "day2.txt" file from the script's directory.

20. `with path.open() as f:`: Opens the file using `with` to ensure it is properly closed after use.

21. `lines = f.readlines()`: Reads all lines from the file.

22. `result = [part1(line) for line in lines]`: Applies the `part1` function to each line and stores the results in a list.

23. `print("part1: ", sum(result))`: Prints the sum of the part 1 results.

24. `result = [part2(line) for line in lines]`: Applies the `part2` function to each line and stores the results in a list.

25. `print("part2: ", sum(result))`: Prints the sum of the part 2 results.
