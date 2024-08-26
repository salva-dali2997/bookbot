def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(f"--- Begin report of {path_to_file} ---")
        wc = word_count(file_contents)
        print(f"{wc} words found in the document")
        print("\n")
        count_dict = char_count(file_contents)
        for count in count_dict:
            print(f"The '{count}' character was found {count_dict[count]} times")
        print("--- End report ---")

def word_count(contents):
    words = contents.split()
    return len(words)

def char_count(contents):
    lower_contents = contents.lower()
    count_dict = {}
    for char in lower_contents:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    if count_dict["\n"]:
        count_dict["\\n"] = count_dict["\n"]
        del count_dict["\n"]
    return count_dict
    
main("books/frankenstein.txt")