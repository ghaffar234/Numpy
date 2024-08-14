def cal_from_word():
    word = "i"
    with open("ghaffar.txt" , "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("word is a found")
        else:
            print("word is not found ")


cal_from_word()