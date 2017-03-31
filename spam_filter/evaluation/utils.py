def read_classification_from_file(path):
    file_dict = {}
    try:
        with open(path, encoding="utf-8") as file1:
            for line in file1:
                name = line.split()
                file_dict[name[0]] = name[1]
    except:
        raise EnvironmentError("Wrong dir.")

    return file_dict

def save_classificatin_to_file(path, dict):

    with open(path, mode='w', encoding="utf-8") as file:
        for key in dict.keys():
            string = str(key) + " " + str(dict[key]) + "\n"
            file.write(string)


if __name__ == '__main__':
    dict = read_classification_from_file("emails/!predictionss.txt")

    print(read_classification_from_file("emails/2/!truth.txt"))

