def count_chars(string):
    count_dict = {}
    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict


if __name__ == "__main__":
    string1 = 'Happiness'
    print(count_chars(string1))

    string2 = 'smiles'
    print(count_chars(string2))
