import sys

def commands():
    print('type "play" play a card OR')
    print('type "draw" to end your turn, and you gain cards depending on your situation.')

print('Welcome to Hissing Creepers, a two player card game stimulation.')
print('Draw, steal and play cards to mitigate your chances of drawing a hissing creeper.')
print('If you draw two hissing creepers or one charged creeper, you lose.')
print('It is day.')

while True:
    print('')
    print('Player 1:')
    commands()
    p1i = input('Choose an action: ')

    print('')
    print('Player 2:')
    commands()
    p2i = input('Choose an action: ')