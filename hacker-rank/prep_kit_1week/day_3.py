import collections
import string
from itertools import cycle


def find_zig_zag_sequence(a, n):
    a.sort()
    mid = n // 2
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2

    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    return a


def tower_choice(t):
    q = collections.deque()
    q.append(t)

    while q:
        v = q.popleft()

        if v <= 0:
            return None

        if t != v and t % v == 0:
            return v

        q.append(v - 1)

    return None


def choose_tower(towers):
    for i, t in enumerate(towers):
        if t % 2 == 0:
            return i
    return 0


def tower_breakers(number_towers, tower_height):
    towers = [tower_height for _ in range(number_towers)]
    players = (i for i in cycle([1, 2]))
    player = -1

    while towers:
        player = next(players)
        print(f'player {player} towers {towers}')

        tower_idx = choose_tower(towers)
        print(f'chose towers[{tower_idx}] -> {towers[tower_idx]}')

        choice = tower_choice(towers[tower_idx])
        print(f'choice {choice}')

        if choice is None:
            # other player wins
            return next(players)

        towers[tower_idx] -= choice
        print(f'tower is now {towers[tower_idx]}')

        if towers[tower_idx] == 0:
            towers.remove(tower_idx)

    return player


def caesar_cypher(s, k):
    lower_alphabet = string.ascii_lowercase
    k = k % len(lower_alphabet)
    lower_shifted = lower_alphabet[k:] + lower_alphabet[:k]

    upper_alphabet = string.ascii_uppercase
    k = k % len(upper_alphabet)
    upper_shifted = upper_alphabet[k:] + upper_alphabet[:k]

    alphabet = lower_alphabet + upper_alphabet
    shifted = lower_shifted + upper_shifted

    t = s.maketrans(alphabet, shifted)
    return s.translate(t)


def palindrome_index(s):
    start = 0
    end = len(s) - 1

    to_remove = - 1

    while start < end:
        if to_remove == -1 and  s[start] != s[end]:
            if s[start + 1] == s[end]:
                to_remove = start
            elif s[start] == s[end - 1]:
                to_remove = end

        start += 1
        end -= 1

    return to_remove
