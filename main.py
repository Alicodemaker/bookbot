def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        print(text)
        wordcounter = 0
        words = text.split()
        for i in words:
            wordcounter += 1
        print(wordcounter)
    

main()