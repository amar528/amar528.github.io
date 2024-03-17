vowels = ['A', 'E', 'I', "O", 'U']


def is_vowel(s):
    return s in vowels


def minion_game(s):
    # Stuart uses consonants to make words
    # Kevin uses vowels to make words
    # 1 point for each occurrence of a substring
    # the game ends when all substrings have been found
    # BANANA

    n = len(s)
    stuart_score = kevin_score = 0

    for i, c in enumerate(s):
        v = n - i

        if is_vowel(c):
            kevin_score += v
        else:
            stuart_score += v

    if stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    elif kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')
    else:
        print('Draw')


if __name__ == '__main__':
    minion_game(input())
