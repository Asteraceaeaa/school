with open("./files/words.txt", "r") as f:
    words = f.read().strip().split(" ")
    wrs = []
    for w in words:
        if w not in wrs:
            wrs.append(w)
    words = ' '.join(words)
    
    for word in wrs:
        print(f"{word} in text: {words.count(word)}")
    print(wrs)