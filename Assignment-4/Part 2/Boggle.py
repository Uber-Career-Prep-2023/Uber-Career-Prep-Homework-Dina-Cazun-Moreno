class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def build_trie(dictionary):
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    return root

def find_valid_words(board, dictionary):
    rows = len(board)
    cols = len(board[0])
    trie_root = build_trie(dictionary)
    valid_words = set()

    def dfs(row, col, node, path):
        if node.is_end_of_word:
            valid_words.add(path)
        visited[row][col] = True
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                    new_char = board[new_row][new_col]
                    if new_char in node.children:
                        dfs(new_row, new_col, node.children[new_char], path + new_char)
        visited[row][col] = False
