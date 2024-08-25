from collections import defaultdict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    character_counts = get_character_counts(text)
    counts_for_sorting = [{"name": name, "num": freq} for name, freq in character_counts.items() if name.isalpha()]
    counts_for_sorting.sort(reverse=True, key=sort_on)
    for count in counts_for_sorting:
        print(f"The letter {count["name"]} appears {count["num"]} times!")

def sort_on(dict):
    return dict["num"]

def get_character_counts(s):
    character_counts = defaultdict(int)
    lowered_string = s.lower()
    for c in lowered_string:
        character_counts[c]+=1
    
    return character_counts

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()