def main():
    print("--- Begin Report of books/frankenstein.txt ---")
    with open("./books/frankenstein.txt") as f:
        frank = f.read()
        print(count_words(frank),"words found in the document\n")
        count = char_count(frank)
        sort_count = dict(sorted(count.items(), key=lambda item: item[1],reverse=True))
        for char in sort_count:
            if char.isalpha():
                print(f"The '{char}' character was found {sort_count[char]} times")
    print("--- End Report ---")

def count_words(text):
    """Takes in a text and returns the count of words

    Args:
        text (str): text to be counted

    Returns:
        (int): count of the total number of words in the text separated by " "
    """
    words = text.split()
    return len(words)

def char_count(text):
    """Returs the character count in a string

    Args:
        text (str): text to have character distribution determined

    Returns:
        dict of str->int: dictionary containing characters as keys and their count as values
    """
    ret = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in ret:
            ret[char] = ret[char]+1
        else:
            ret[char] = 1
    return ret

if __name__ == '__main__':
    main()