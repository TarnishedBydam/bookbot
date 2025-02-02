def main():
    number = 0
    letters = {}
    with open("books/frankenstein.txt", encoding="utf-8") as f:
        file_contents = f.read()
        
        words = file_contents.split()
        number += len(words)

        for char in file_contents:
            lower = char.lower()
            if lower.isalpha():  
                letters[lower] = letters.get(lower, 0) + 1
    
    print(f"Number of words: {number}")
    
    for ch in sorted(letters.keys()):
        print(f"The '{ch}' character was found {letters[ch]} times")

if __name__ == "__main__":
    main()
