from random import choice, seed
from datetime import datetime
seed(datetime.now())

var = ('rock', 'paper', 'scissors')


def rock_paper_scissors():
    """Play rock-paper-scissors game against computer."""
    computer_choice = choice(var)
    human_choice = ''

    while human_choice not in var:
        print('What is your choice? (rock, paper or scissors)')
        human_choice = input()

    print('Clovek zvolil {} a pocitac zvolil {}'.format(human_choice, computer_choice))
    print(eval_rps(computer_choice, human_choice))


def eval_rps(computer_choice, human_choice):
    """"Evaluate who wins rock-paper-scissors fight."""
    if computer_choice == human_choice:
        return 'plichta'
    elif (computer_choice == 'rock' and human_choice == 'scissors') \
            or (computer_choice == 'paper' and human_choice == 'rock') \
            or (computer_choice == 'scissors' and human_choice == 'paper'):
        return 'vyhra pocitace'
    else:
        return 'vyhra cloveka'


while True:
    rock_paper_scissors()

