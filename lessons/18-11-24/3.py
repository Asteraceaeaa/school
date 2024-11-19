with open("./files/data.csv", "r") as f, open("./files/column2.txt", "w") as res:
    data = [res.write(x.strip().split(",")[1] + "\n") for x in f.readlines()]
    
    
    