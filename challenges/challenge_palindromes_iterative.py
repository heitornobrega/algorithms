def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    word = word.lower()
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True
