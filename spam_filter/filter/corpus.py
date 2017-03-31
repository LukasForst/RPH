import os.path


class Corpus:

    def __init__(self, dir_path):
        self.dir_path = dir_path

    def emails(self):
        """
        :returns every email in the main directory
        """
        for email in os.listdir(self.dir_path):
            if(email.startswith('!')):  # skipping '!truth.txt' and '!prediction.txt'
                continue
            else:
                yield (email, self.get_body(email))

    def get_body(self, file_name):
        """
        :param file_name: name of the email
        :return: body of the email
        """
        with open(os.path.join(self.dir_path, file_name), encoding='utf-8') as file:
            return file.read()

    def save_conclusion(self, conclusion = {}):
        """
        saving generated dictionary to the txt file
        :param conclusion: updated dictionary
        """
        with open(os.path.join(self.dir_path, '!prediction.txt'), mode='w', encoding='utf-8') as file:
            for key in conclusion.keys():
                file.write( key + " " + conclusion[key] + '\n')

if __name__ == '__main__':
    # Create corpus from a directory
    corpus = Corpus('emails/1/')
    count = 0
    # Go through all emails and print the filename and the message body
    for fname, body in corpus.emails():
        print(fname)
        print(body)
        print('-------------------------')
        count += 1
    print('Finished: ', count, 'files processed.')