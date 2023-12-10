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

## Tests
To run all tests, navigate to src folder and:
- All Tests
  ```
  make all
  ```
  
