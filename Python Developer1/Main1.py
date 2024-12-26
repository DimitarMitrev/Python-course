def broj_bukvi(word):

    count = 0

    for char in word:
        count += 1

    return count

word = input("Vnesi zbor: ")

count = broj_bukvi(word)

print(count)
