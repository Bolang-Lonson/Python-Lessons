def isanagram(word1, word2):
    word1, word2 = word1.upper(), word2.upper()
    word1, word2 = word1.replace('', ' '), word2.replace('', ' ')
    word1, word2 = word1.split(), word2.split()
    word1.sort()
    word2.sort()
    return word1 == word2


def main():
    print('ANAGRAM'.center(27, '-'))
    while True:
        first = input('First word\n')
        secnd = input('Second word\n')
        if isanagram(first, secnd):
            print('Anagrams')
        else:
            print('Not anagrams')

        loop = int(input('1) Back\n2) Close\n'))
        match loop:
            case 1:
                continue
            case 2:
                break

if __name__ == '__main__':
    main()