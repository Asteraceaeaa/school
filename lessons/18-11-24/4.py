with open("./files/article.txt") as f, open("./files/updated_article.txt", "w") as res:
    article = f.read().lower()
    res.write(article.replace("старый", "новый"))