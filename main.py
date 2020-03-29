import random
l = ['Rock', 'Paper', 'Scissor']

p1_score = 0
p2_score = 0
c1_score = 0
c2_score = 0


def computer1():
    global c1_hand
    l = ['Rock', 'Paper', 'Scissor']
    c1_hand = random.randint(0, 2)

    print("\nComputer 1 choose: ", l[c1_hand])


def computer2():
    global c2_hand
    l = ['Rock', 'Paper', 'Scissor']
    c2_hand = random.randint(0, 2)

    print("\nComputer 2 choose: ", l[c2_hand])


def player1():
    global p1_hand
    p1_hand = int(
        input("Player 1:\n1. Rock\n2. Paper\n3. Scissors\nEnter your choice: "))
    p1_hand -= 1
    print("\nThe player chose: ", l[p1_hand])


def player2():
    global p2_hand
    p2_hand = int(
        input("Player 2: \n1. Rock\n2. Paper\n3. Scissors\nEnter your choice: "))
    p2_hand -= 1
    print("\nThe player chose: ", l[p1_hand])


def pla_com():
    player1()
    computer1()
    global p1_score
    global c1_score
    if (p1_hand == 1 and c1_hand == 0) or (p1_hand == 2 and c1_hand == 1) or (p1_hand == 0 and c1_hand == 2):
        print("\nPlayer 1 won.\n")
        p1_score += 1
    elif (c1_hand == 1 and p1_hand == 0) or (c1_hand == 2 and p1_hand == 1) or (c1_hand == 0 and p1_hand == 2):
        print("\nThe computer won.\n")
        c1_score += 1
    else:
        print("\nDraw\n")


def com_com():
    computer1()
    computer2()
    global c1_score
    global c2_score
    if (c1_hand == 1 and c2_hand == 0) or (c1_hand == 2 and c2_hand == 1) or (c1_hand == 0 and c2_hand == 2):
        print("\nComputer 1 won.\n")
        c1_score += 1
    elif (c2_hand == 1 and c1_hand == 0) or (c2_hand == 2 and c1_hand == 1) or (c2_hand == 0 and c1_hand == 2):
        print("\nComputer 2 won.\n")
        c2_score += 1
    else:
        print("\nDraw\n")


def pla_pla():
    player1()
    player2()
    global p1_score
    global p2_score
    if (p1_hand == 1 and p2_hand == 0) or (p1_hand == 2 and p2_hand == 1) or (p1_hand == 0 and p2_hand == 2):
        print("\nPlayer 1 won.\n")
        p1_score += 1
    elif (p2_hand == 1 and p1_hand == 0) or (p2_hand == 2 and p1_hand == 1) or (p2_hand == 0 and p1_hand == 2):
        print("\nPlayer 2 won.\n")
        p2_score += 1
    else:
        print("\nDraw\n")


choice = int(input("The game of rock Paper Scissor \nMake your choice\n1. Player 1 Vs. Player 2\n2. Player Vs. Computer\n3. Computer Vs. Computer\nYour choice: "))
games = int(input("Enter the number of rounds: "))
times = 0


if choice == 1:
    while times < games:
        print("\nGame", times + 1)
        pla_pla()
        times += 1
elif choice == 2:
    while times < games:
        print("\nGame", times + 1)
        pla_com()
        times += 1
elif choice == 3:
    while times < games:
        print("\nGame", times + 1)
        com_com()
        times += 1


if times == games:

    if choice == 1:
        if p1_score > p2_score:
            print("Player 1 has won the game.")
        elif p1_score < p2_score:
            print("Player 2 has won the game.")
        elif p1_score == p2_score != 0:
            print("It was a draw.")

    if choice == 2:
        if p1_score > c1_score:
            print("Player has won the game.")
        elif p1_score < c1_score:
            print("The computer has won the game.")
        elif p1_score == c1_score != 0:
            print("It was a draw.")

    if choice == 3:
        if c1_score > c2_score:
            print("Cmputer 1 has won the game.")
        elif c1_score < c2_score:
            print("Computer 2 has won the game.")
        elif c1_score == c2_score != 0:
            print("It was a draw.")
