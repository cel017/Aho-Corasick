from typing import List
from collections import defaultdict, deque

class _AutomatonNode:
    def __init__(self):
        self.children = defaultdict(_AutomatonNode)
        # /failure link; gets iniialized to root
        self.suffix_link = None
        # /dict links
        self.output_link = None
        # id of pattern leaf node is in
        self.pattern_id = -1
    
    def is_leaf(self):
        return self.pattern_id != -1

class AhoCorasick:
    def __init__(self, patterns : List[str]):
        self.root = _AutomatonNode()
        self.patterns = patterns
        # build automaton
        self._create_trie()
        self._create_suffix_and_output()

    def _create_trie(self):
        for i, pattern in enumerate(self.patterns):
            node = self.root
            for char in pattern:
                node = node.children[char]
            node.pattern_id = i

    def _create_suffix_and_output(self):
        queue = deque()
        for child in self.root.children.values():
            child.suffix_link = self.root
            queue.append(child)

        # BFS
        while queue:
            node = queue.popleft()

            for char, child in node.children.items():
                queue.append(child)

                # follow suffix links until a match is found
                x = node.suffix_link
                while x is not None and char not in x.children:
                    x = x.suffix_link

                # set the suffix link for the current child
                if x is None:
                    child.suffix_link = self.root
                else:
                    child.suffix_link = x.children[char]

                # set the output link for the current child
                if child.suffix_link.is_leaf():
                    child.output_link = child.suffix_link
                else:
                    child.output_link = child.suffix_link.output_link

    def search(self, search_str: str) -> dict[str, List[int]] :
        """
        Search for patterns in the given search string and return a dictionary
        mapping each pattern to a list of starting indexes where it occurs.

        Parameters:
        search_str (str) -> Target string to find matches in.

        Returns:
        dict[str, List[int]] -> {Pattern: Start indexes of matches in target}
        """
        result = defaultdict(list)
        node = self.root

        for i, char in enumerate(search_str):
            # follow suffix links till char is found (or root)
            while char not in node.children:
                if node == self.root:
                    break
                node = node.suffix_link
            
            if char not in node.children:
                continue
            
            # check current node
            node = node.children[char]
            if node.is_leaf():
                pattern = self.patterns[node.pattern_id]              
                result[pattern].append(i-len(pattern)+1)
    
            # follow output links
            output_node = node.output_link
            while output_node is not None:
                pattern = self.patterns[output_node.pattern_id]              
                result[pattern].append((i-len(pattern)+1)) 
                output_node = output_node.output_link

        return result

if __name__ == '__main__':
    
    '''
    Example Usage:
    
    Patterns = abc, bc, bca
    Search String = aabca
    
    a(abc)a : 1
    aa(bc)a : 2
    aa(bca) : 2
    xyz -> no match

    Output = {'abc': [1], 'bc': [2], 'bca': [2]}
    '''
    patterns = ["abc", "bc", "bca", "xyz"]
    ac = AhoCorasick(patterns)
    matches = ac.search("aabca")
    for k, v in matches.items():
        print(f"{k}: {v}")
