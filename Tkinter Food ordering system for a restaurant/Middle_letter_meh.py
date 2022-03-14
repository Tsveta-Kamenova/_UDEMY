def middle(word):
    n = len(word)
    mid_odd = int((n-1)/2)
    mid_even = int(n/2)
    word = list(word)
    if n % 2 == 0:
        print(f"{word[mid_even-1]}{word[mid_even]}")
    elif n == 1:
        print(n)
    else:
        print(word[mid_odd])


middle(input())