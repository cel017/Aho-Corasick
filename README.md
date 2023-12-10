# Aho-Corasick
An Implementation of the Aho-Corasick Algorithm for Multiple String Matching [CMPUT-403 Final Project] 

## Algorithm
Aho-Corasick is an algorithm for matching multiple strings within a target string, that functions by pre-processing the pattern strings.

## Big-O
My implementation of the algorithm matches the theoretical runtime bounds.

n = length of target string
m = sum of lengths of pattern strings
z = total number of matches
- **Building the Trie:** O(m)

- **Creating Suffix and Output Links:** O(m)

- **Searching for Patterns:** O(n + z)

## Resources Used
- **Original Paper:**
  - [Aho-Corasick Algorithm](https://dl.acm.org/doi/pdf/10.1145/360825.360855)

- **Wikipedia:**
  - [Wikipedia](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm)

- **Pseudocode:**
  - [Stanford CS166 Lecture Notes](https://web.stanford.edu/class/archive/cs/cs166/cs166.1186/lectures/02/Small02.pdf)

- **Visualization:**
  - [Failure Links Visualization (YouTube)](https://www.youtube.com/watch?v=O7_w001f58c)
  - [Output Links Visualization (YouTube)](https://www.youtube.com/watch?v=OFKxWFew_L0)


## Usage
```python
# Example usage
patterns = ["apple", "banana", "nap"]
target_string = "bananapple"

aho_corasick = AhoCorasick(patterns)
result = aho_corasick.search(target_string)

print(result)
```

## Files Included
- **aho_corasick.py**
  - Complete implementation of the Aho-Corasick algorithm.
  - The AhoCorasick class build an automaton when initialized using the _AutomatonNode class internally.

- **tests_ac.py**
  - File to run tests.
  - Use run_tests() to generate outputs for all input files in the input dir and diff against expected.
  - Use parse_input() to parse input file and generate_expected_file() to create an output file with Aho-Corasick.

- **testcase_generator.py**
  - File for randomly generating input and computing expected output with a naive algorithm.
  - Use generate_input(), parse it (parse_input() from tests_ac.py) and then use generate_output_file() to use a naive search to solve the input.

- **testfiles**
  - This directory has the input files and expected output files.

## Tests
2-10.txt are larger cases. The rest are edge cases and some manually created cases to confirm functionality.

To run all tests, navigate to src folder and:
- All Tests
  ```
  make all
  ```
- Correctness Tests
  ```
  make correct
  ```
- Time Tests
  ```
  make time
  ```

The runtime test shows the time taken for building the automaton and scanning the list for successive powers of 10 for both.

- **Build Automaton**: The time is increasing roughly by a factor of 10 at each iteration of m*(10^i). The relationship is linear and the runtime seems consistent with theory. [Note: Consider deleting the file with m = 10^7. It took 30 seconds to run on my PC]:
  - 1        : 0.00010301600013917778,
  - 10       : 5.76190004721866e-05, 
  - 100      : 0.000337752000632463, 
  - 1000     : 0.0031482329995924374, 
  - 10000    : 0.03523344099994574, 
  - 100000   : 0.37194910800008074, 
  - 1000000  : 3.3667016560002594, 
  - 10000000 : 31.554771600000095

- **Aho-Corasick Search**:
  - 0       : 1.5294999684556387e-05
  - 3       : 1.2361999324639328e-05
  - 136     : 4.386000000522472e-05
  - 1952    : 0.0007336819999181898
  - 24308   : 0.009405938000782044
  - 242314  : 0.09534698099923844
  - 3183013 : 1.9206841590003023

The input files have two lines:
- The first line is a sequence of space separated pattern strings
- The second line is a single target string

Since whitespaces are used as a delimeter here it's not possible to have strings that have whitespaces in them in the inputfiles since they will just get interpreted as two different strings by the program. This is merely a limitation of the input format, and the algorithm itself treats whitespaces like any other character.

## Interpretting the output
The output of the search function in the AhoCorasick class is a defaultdict in which the keys are patterns that appear in the target string, and the values are all of the starting indexes that they appear at {getting the ending index is trivial -> i+len(pattern)}.

The output files have each dictionary item on their own line followed by its values, all space separated.
So, if the actual output is -
```
{"ab": [1, 2], "a": [1]}
```
The output file will look like -
```
a 1
ab 1 2
```
To ensure uniformity, the lines of the output files are sorted Lexicographically. 

## Peculiarities
Whitespaces in input files as mentioned above. Otherwise, there aren't any problems in the main implementation that I'm aware of.
