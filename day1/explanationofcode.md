```python
import re
```
This line imports the regular expression (re) module, which is used for pattern-matching operations.

```python
def read_lines():
    with open('day1.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines
```
This function, `read_lines`, opens the file named 'day1.txt' in read mode, reads its content, and then splits the content into a list of lines using `splitlines()`. It returns the list of lines.

```python
lines = read_lines()
```
This line calls the `read_lines` function and assigns the list of lines from 'day1.txt' to the variable `lines`.

```python
def get_numbers_with_indices(line):
    num_with_indices = []

    for i, ch in enumerate(line):
        if ch.isalpha():
            continue
        num_with_indices.append([i, ch])
    return num_with_indices
```
This function, `get_numbers_with_indices`, takes a line as input and iterates through each character in the line. For each character that is not alphabetic (using `isalpha()`), it appends a list containing the index and the character to the `num_with_indices` list. The function returns this list.

```python
def get_digits_with_indices(line):
    num_mapping = {
        'one': '1',
        'two' : '2',
        'three': '3',
        'four' : '4',
        'five': '5',
        'six': '6',
        'seven' : '7',
        'eight': '8',
        'nine': '9',
    }
    digits_with_indices = []

    for number in num_mapping:
        for m in re.finditer(number, line):
            digits_with_indices.append([m.start(), num_mapping[number]])
    return digits_with_indices
```
This function, `get_digits_with_indices`, uses a predefined mapping (`num_mapping`) of words to their corresponding digits. It iterates through each word in the mapping and uses `re.finditer` to find all occurrences of that word in the given line. For each match, it appends a list containing the starting index of the match and the corresponding digit to the `digits_with_indices` list. The function returns this list.

```python
def part1():
    total_sum = 0
    for line in lines:
        num_indices = get_numbers_with_indices(line)
        num_indices.sort(key=lambda x: x[0])
        total_sum += int(num_indices[0][1] + num_indices[-1][1])

    print(f'part1: {total_sum}')
```
This function, `part1`, calculates a total sum based on the first and last digits found in each line. It iterates through each line, obtains the indices and characters of non-alphabetic characters using `get_numbers_with_indices`, sorts them by index, and adds the first and last characters converted to integers to the `total_sum`.

```python
def part2():
    total_sum = 0
    for line in lines:
        num_indices = get_numbers_with_indices(line)
        digit_indices = get_digits_with_indices(line)
        all_indices = digit_indices + num_indices

        all_indices.sort(key=lambda x: x[0])

        total_sum += int(all_indices[0][1] + all_indices[-1][1])

    print(f'part2: {total_sum}')
```
This function, `part2`, is similar to `part1`, but it considers both the digits obtained from words and the digits obtained from non-alphabetic characters. It combines the lists of indices and characters, sorts them by index, and adds the first and last characters converted to integers to the `total_sum`.

```python
if __name__ == "__main__":
    part1()
    part2()
```
This block checks if the script is being run as the main program (not imported as a module). If it is the main program, it calls the `part1` and `part2` functions, printing the results.
