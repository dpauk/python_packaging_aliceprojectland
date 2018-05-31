from wordcount import WC


def replace_words(words):
    with open(words, 'r') as input:
        with open('new_alice.txt', 'w') as output:
            for line in input:
                line = line.rstrip()
                newline = line.replace("Alice", "Paddington")
                output.write(newline)


if __name__ == '__main__':
    replace_words('alice.txt')
    alice = WC('alice.txt')
    new_alice = WC('new_alice.txt')
    print("Old wordcount: ", alice.word_count())
    print("WC __name__: ", WC.__name__)
    print("New wordcount: ", new_alice.word_count())
    print("replace __name__: ", __name__)
