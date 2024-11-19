alph = [chr(letter) for letter in range(ord("а"),ord("я") + 1)]
print(alph)
with open("./files/secret.txt") as f, open("decrypted_secret.txt", "w") as decr:
    secret = f.read().strip()

    for i in secret:
        if i.lower() not in alph:
            decr.
    