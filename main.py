import urllib.request
import random


def display_guess(guess: str, real: str):
    # 0 = = match, 1 = there, 2 = not there
    final_display = [None, None, None, None, None]
    history = set()

    for i in range(len(guess)):
        if guess[i] == real[i]:
            final_display[i] = (guess[i], 0)
            history.add(guess[i])

    for i in range(len(guess)):
        if guess[i] in real and guess[i] not in history:
            final_display[i] = (guess[i], 1)
        elif final_display[i] is None:
            final_display[i] = (guess[i], 2)

    print('+---+---+---+---+---+')
    for i, c in final_display:
        if c == 0:
            print(f'|*{i}*', end='')
        elif c == 1:
            print(f'|~{i}~', end='')
        elif c == 2:
            print(f'| {i} ', end='')

    print('|')

    print('+---+---+---+---+---+')
    return all(c == 0 for i, c in final_display)


def take_input(num: int):
    while True:
        x = input(f'Guess #{num}: ')

        if len(x) == 5 and x.isalpha():
            return x
        else:
            print('INVALID INPUT')


def bug_test():
    bug_testing = input('BUGTESTING? Y/N: ')
    while True:
        if bug_testing.lower() == 'y':
            print(word_to_guess)
            break
        elif bug_testing.lower() == 'n':
            break
        else:
            print('INVALID')


def random_word():
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    request = urllib.request.urlopen(url)
    data = request.read().decode('utf-8')

    raw_list = data.split('\n')
    filtered_list = [x for x in raw_list if len(x) == 5]
    return random.choice(filtered_list)


if __name__ == '__main__':

    word_to_guess = random_word()

    bug_test()

    for num in range(6):
        guess = take_input(num + 1)
        x = display_guess(guess, word_to_guess)
        if x is True:
            print('You Win!')
            break
    else:
        print('You Lose')
        print('The Word Was: ' + word_to_guess)
