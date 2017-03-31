import os.path

class Corpus:

    def __init__(self, dir_path):
        self.dir_path = dir_path

    def emails(self):
        for email in os.listdir(self.dir_path):
            if(email.startswith('!')):
                continue
            else:
                body = self.get_body(os.path.join(self.dir_path, email))
                yield (email, body)

    def get_body(self, path):
        with open(path, encoding='utf-8') as file:
            return file.read()


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