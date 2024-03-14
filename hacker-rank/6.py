if __name__ == '__main__':
    n = int(input())
    distinct_scores = set(map(int, input().split()))
    sorted_scores = sorted(list(distinct_scores))
    print(sorted_scores[-2])
