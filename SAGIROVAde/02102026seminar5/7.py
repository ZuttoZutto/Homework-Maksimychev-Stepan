"""Task 7. Buquoed"""
import string

filename = "SAGIROVAde\\02102026seminar5\\text for 7py.txt"


with open(filename, 'r', encoding='utf-8') as fhand:
    counts = dict()
    for line in fhand:
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

lst = list()
for key, val in counts.items():
    lst.append((val, key))

lst.sort(reverse=True)

print("Топ-10 самых частых слов:")
for count, word in lst[:10]:
    print(f"{word}: {count}")

