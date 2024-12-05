from nltk.corpus import wordnet
def main():
    while True:
        word = input("Which word is it? ")
        o = fetch_meaning(word)
        for line in o:
            print(line)

def fetch_meaning(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        return "0"

    meanings = []
    for synset in synsets:
        definition = synset.definition()
        meanings.append((definition))

    return meanings

if __name__ == "__main__":
    main()