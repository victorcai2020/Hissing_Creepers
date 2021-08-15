import random as r
import sys

def commands():
    print('Type "play" play a card OR')
    print('Type "draw" to gain card(s).')
    print('Please do not play cards you do not have. It breaks the game.')
    print('Don\'t break the game. You like the game.')

print('')
print('')
print('Welcome to Hissing Creepers, a two player card game stimulation.')
print('Draw, steal and play cards to mitigate your chances of drawing a hissing creeper.')
print('If you draw two hissing creepers or one charged creeper, you lose.')
print('For more advanced instructions, visit this link: https://github.com/victorcai2020/Hissing_Creepers/wiki')
print('It is also good to visit the advanced instructions if you are a beginner.')


draw = ['Animal', 'Wood', 'Stone', 'Iron', 'DIAMOND!!', 'Go caving', 'Go to the Nether', 'Go to the End', 'Villager', 'Bad Omen',
         '!!HISSING CREEPER!!', '!!!!CHARGED HISSING CREEPER!!!!']

h1 = ['Go caving', 'Go to the Nether', 'Go to the End']
Villagercount1 = h1.count('Villager')
h2 = []
Villagercount2 = h2.count('Villager')

while True:
    print('')
    print('Player 1:')
    commands()
    print(h1)
    p1i = input('Choose an action: ')

    if p1i == "draw":
        drawncard1 = r.choice(draw)
        print("You drew a", drawncard1, "card")
        if drawncard1 != '!!!!CHARGED HISSING CREEPER!!!!':
            if h1.count('!!HISSING CREEPER!!') >= 2:
                h1.append(drawncard1)
                print("You have these cards: ", h1)
            else:
                print('You drew two Hissing Creepers, and lost.')
                sys.exit()
        else:
            print('You drew a Charged Hissing Creeper, and lost.')
            sys.exit()

    if p1i == "play":
        print('The recipe book is good for beginners.')
        p1m = input("Do you want to read the recipe book(use yes or no answer)? ")
        if p1m == 'yes':
            print('')
            print('RECIPE BOOK')
            print('')
            print('One animal card, when played, will eliminate ONE Hissing Creeper from your hand.')
            print('One wood card, when played, will make you a wood sword. Requires 4 to \"defuse\" a Hissing Creeper.')
            print('One stone card, when played, will make you a stone sword. Requires 3 to \"defuse\" a Hissing Creeper.')
            print('One iron card, when played, will make you an iron sword. Requires 2 to \"defuse\" a Hissing Creeper.')
            print('One diamond card, when played, will make you a diamond sword. Use to \"defuse\" a Hissing Creeper')
            print('A Villager card, when played, will allow you to make two draws on one turn.')
            print('A go caving card, when played will allow you to make two draws on one turn.')
            print('A go to the nether card, when played, will allow you to make three draws on one turn.')
            print('A go to the end card, when played, will allow you to make four draws on one turn.')
            print('A Bad Omen card, when played, will sacrifice all your Villager cards, but allows you to make three draws'
                  'on one turn')
            print('')

        print('')
        print('Case sensitive. Type the exact name of the card without any exclamation marks')
        print(h1)

        p1p = input("What card do you want to play?")
        if p1p == 'Animal':
            h1.remove('Animal')
            if "!!HISSING CREEPER!!" in h1:
                h1.remove('!!HISSING CREEPER!!')
            else:
                print('That animal that you used for food had no use.')
        if p1p == 'Wood':
            h1.remove('Wood')
            h1.append('Wood sword')
        if p1p == 'Stone':
            h1.remove('Stone')
            h1.append('Stone sword')
        if p1p == 'Iron':
            h1.remove('Iron')
            h1.append('Iron sword')
        if p1p == 'DIAMOND':
            h1.remove('DIAMOND!!')
            h1.append('DIAMOND SWORD!!')
        if p1p == 'Villager':
            for x in range(2):
                drawncard1 = r.choice(draw)
                if drawncard1 != '!!!!CHARGED HISSING CREEPER!!!!':
                    if h1.count('!!HISSING CREEPER!!') >= 2:
                        h1.append(drawncard1)
                        print("You have these cards: ", h1)
                    else:
                        print('You drew two Hissing Creepers, and lost.')
                        sys.exit()
                else:
                    print('You drew a Charged Hissing Creeper, and lost.')
                    sys.exit()
        if p1p == 'Bad Omen':
            h1.remove('Bad Omen')
            print('A raid is coming!')
            for Villagercount1 in h1:
                h1.remove('Villager')
                print('The raid defeated all your villagers.')
            h1.remove('Villager')
            for x in range(3):
                drawncard1 = r.choice(draw)
                print("You drew a", drawncard1, "card")
                if drawncard1 != '!!!!CHARGED HISSING CREEPER!!!!':
                    if h1.count('!!HISSING CREEPER!!') >= 2:
                        h1.append(drawncard1)
                        print("You have these cards: ", h1)
                    else:
                        print('You drew two Hissing Creepers, and lost.')
                        sys.exit()
                else:
                    print('You drew a Charged Hissing Creeper, and lost.')
                    sys.exit()
        if p1p == 'Go caving':
            h1.remove('Go caving')
            print('You went caving')
            for x in range(2):
                drawncard1 = r.choice(draw)
                print("You drew a", drawncard1, "card")
                if drawncard1 != '!!!!CHARGED HISSING CREEPER!!!!':
                    if h1.count('!!HISSING CREEPER!!') >= 2:
                        h1.append(drawncard1)
                        print("You have these cards: ", h1)
                    else:
                        print('You drew two Hissing Creepers, and lost.')
                        sys.exit()
                else:
                    print('You drew a Charged Hissing Creeper, and lost.')
                    sys.exit()
        if p1p == 'Go to the Nether':
            h1.remove('Go to the Nether')
            print('You went to the Nether.')
            for x in range(3):
                drawncard1 = r.choice(draw)
                print("You drew a", drawncard1, "card")
                if drawncard1 != '!!!!CHARGED HISSING CREEPER!!!!':
                    if h1.count('!!HISSING CREEPER!!') <= 2:
                        h1.append(drawncard1)
                        print("You have these cards: ", h1)
                    else:
                        print('You drew two Hissing Creepers, and lost.')
                        sys.exit()
                else:
                    print('You drew a Charged Hissing Creeper, and lost.')
                    sys.exit()
        if p1p == 'Go to the End':
            h1.remove('Go to the End')
            print('You defeated the Ender Dragon!!!! Congratulations!')
            for x in range(4):
                drawncard1 = r.choice(draw)
                print("You drew a", drawncard1, "card")
                if drawncard1 != '!!!!CHARGED HISSING CREEPER!!!!':
                    if h1.count('!!HISSING CREEPER!!') <= 2:
                        h1.append(drawncard1)
                        print("You have these cards: ", h1)
                    else:
                        print('You drew two Hissing Creepers, and lost.')
                        sys.exit()
                else:
                    print('You drew a Charged Hissing Creeper, and lost.')
                    sys.exit()

    print('')
    print('Player 2:')
    commands()
    print(h2)
    p2i = input('Choose an action: ')
    if p2i == "draw":
        drawncard2 = r.choice(draw)
        print("You drew a", drawncard2, "card")
        if drawncard2 != '!!!!CHARGED HISSING CREEPER!!!!':
            if h2.count('!!HISSING CREEPER!!') >= 2:
                h2.append(drawncard2)
                print("You have these cards: ", h2)
            else:
                print('You drew two Hissing Creepers, and lost.')
                sys.exit()
        else:
            print('You drew a Charged Hissing Creeper, and lost.')
            sys.exit()

    if p2i == "play":
        p2m = input("Do you want to read the recipe book(use yes or no answer)? ")
        if p2m == 'yes':
            print('')
            print('RECIPE BOOK')
            print('')
            print('One animal card, when played, will eliminate ONE Hissing Creeper from your hand.')
            print('One wood card, when played, will make you a wood sword. Requires 4 to \"defuse\" a Hissing Creeper.')
            print('One stone card, when played, will bake you a stone sword. Requires 3 to \"defuse\" a Hissing Creeper.')
            print('One iron card, when played, will make you an iron sword. Requires 2 to \"defuse\" a Hissing Creeper.')
            print('One diamond card, when played, will make you a diamond sword. Use to \"defuse\" a Hissing Creeper')
            print('A Villager card, when played, will allow you to make two draws on one turn.')
            print('A go caving card, when played will allow you to make two draws on one turn')
            print('A go to the nether card, when played, will allow you to make three draws on one turn')
            print('A go to the end card, when played, will allow you to make four draws on one turn.')
            print('A Bad Omen card, when played, will sacrifice all your Villager cards, but allows you to make three draws'
                  'on one turn')
            print('')

        p2p = input("What card do you want to play?")
        if p2p == 'Animal':
            h2.remove('Animal')
            if "!!HISSING CREEPER!!" in h2:
                h2.remove('!!HISSING CREEPER!!')
            else:
                print('That animal that you used for food had no use.')
        if p2p == 'Wood':
            h2.remove('Wood')
            h2.append('Wood sword')
        if p2p == 'Stone':
            h2.remove('Stone')
            h2.append('Stone sword')
        if p2p == 'Iron':
            h2.remove('Iron')
            h2.append('Iron sword')
        if p2p == 'DIAMOND':
            h2.remove('DIAMOND!!')
            h2.append('DIAMOND SWORD!!!')
        if p2p == 'Villager':
            for x in range(2):
                drawncard2 = r.choice(draw)
                if drawncard2 != '!!!!CHARGED HISSING CREEPER!!!!':
                    if h2.count('!!HISSING CREEPER!!') >= 2:
                        h2.append(drawncard2)
                        print("You have these cards: ", h2)
                    else:
                        print('You drew two Hissing Creepers, and lost.')
                        sys.exit()
                else:
                    print('You drew a Charged Hissing Creeper, and lost.')
                    sys.exit()
        if p2p == 'Bad Omen':
            h2.remove('Bad Omen')
            print('A raid is coming!')
            for Villagercount2 in h2:
                h2.remove('Villager')
                print('The raid defeated all your villagers.')
            h2.remove('Villager')
            for x in range(3):
                drawncard2 = r.choice(draw)
                print("You drew a", drawncard2, "card")
                if drawncard2 != '!!!!CHARGED HISSING CREEPER!!!!':
                    if h2.count('!!HISSING CREEPER!!') >= 2:
                        h2.append(drawncard2)
                        print("You have these cards: ", h2)
                    else:
                        print('You drew two Hissing Creepers, and lost.')
                        sys.exit()
                else:
                    print('You drew a Charged Hissing Creeper, and lost.')
                    sys.exit()
        if p2p == 'Go caving':
            h2.remove('Go caving')
            print('You went caving')
            for x in range(2):
                drawncard2 = r.choice(draw)
                print("You drew a", drawncard2, "card")
                if drawncard2 != '!!!!CHARGED HISSING CREEPER!!!!':
                    if h2.count('!!HISSING CREEPER!!') >= 2:
                        h2.append(drawncard2)
                        print("You have these cards: ", h2)
                    else:
                        print('You drew two Hissing Creepers, and lost.')
                        sys.exit()
                else:
                    print('You drew a Charged Hissing Creeper, and lost.')
                    sys.exit()
        if p2p == 'Go to the Nether':
            h2.remove('Go to the Nether')
            print('You went to the Nether.')
            for x in range(3):
                drawncard2 = r.choice(draw)
                print("You drew a", drawncard2, "card")
                if drawncard2 != '!!!!CHARGED HISSING CREEPER!!!!':
                    if h2.count('!!HISSING CREEPER!!') <= 2:
                        h2.append(drawncard2)
                        print("You have these cards: ", h2)
                    else:
                        print('You drew two Hissing Creepers, and lost.')
                        sys.exit()
                else:
                    print('You drew a Charged Hissing Creeper, and lost.')
                    sys.exit()
        if p2p == 'Go to the End':
            h2.remove('Go to the End')
            print('You defeated the Ender Dragon!!!! Congratulations!')
            for x in range(4):
                drawncard2 = r.choice(draw)
                print("You drew a", drawncard2, "card")
                if drawncard2 != '!!!!CHARGED HISSING CREEPER!!!!':
                    if h2.count('!!HISSING CREEPER!!') <= 2:
                        h2.append(drawncard2)
                        print("You have these cards: ", h2)
                    else:
                        print('You drew two Hissing Creepers, and lost.')
                        sys.exit()
                else:
                    print('You drew a Charged Hissing Creeper, and lost.')
                    sys.exit()
