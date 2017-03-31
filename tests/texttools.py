def count_rows_and_words(path):
    result = () # pocet radku, pocet slov
    lines = 0
    words = 0
    with open(path, encoding="utf-8") as file:
        for line in file:
            lines += 1
            words += len(line.split())

    result = (lines, words)
    return result

def compute_word_frequencies(path):
    final_dict = {}
    with open(path, encoding='utf-8') as file:
        for words in file:
            words = words.split()

            for word in words:
                if(word in final_dict.keys()):
                    continue
                final_dict[word] = words.count(word)


    return final_dict


if __name__ == '__main__':
    result = compute_word_frequencies('test.txt')
    print(result)