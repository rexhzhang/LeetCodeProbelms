wordlist = ["AAEEiiou"]
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
for item in wordlist:
    X = item
    for letter in vowels:
        if letter in X:
            X = X.replace(letter, '#')

    print (X)