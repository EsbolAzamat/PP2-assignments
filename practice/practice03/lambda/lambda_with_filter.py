numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


words = ["cat", "elephant", "dog", "giraffe"]

long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)
