

def is_palindome(word:str) -> bool:
    # app 1
    # return word == word[::-1]

    # app 2
    # word_len = len(word)
    # for c in range(0, int(word_len/2)):
    #     if word[c] != word[-1*c-1]:
    #         return False
    # return True

    # app 3
    max_len = int(len(word)/2)
    for i, j in zip(word[:max_len], word[max_len:][::-1]):
        if i != j:
            return False
    return True

if __name__ == "__main__":
    for word in ['level', 'civic']:
        print(word, is_palindome(word))