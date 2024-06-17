def word_count_function(split_document):
    word_count = {}

    for word in split_document:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


if __name__ == "__main__":
    file_path = "./Module 01/Week 02/P1_data.txt"

    with open(file_path, 'r') as f:
        document = f.read()

    split_document = document.lower().split()

    print(",\n".join(f"{word}: {count}" for word,
          count in word_count_function(split_document).items()))
