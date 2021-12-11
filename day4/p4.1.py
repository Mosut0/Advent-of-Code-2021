def check_row(card):
    for i in range(0, len(card), 5):
        if card[i:i+5].count("") == 5:
            return True

    return False


def check_column(card):
    for i in range(5):
        column = [card[i], card[i + 5], card[i + 10], card[i + 15], card[i + 20]]
        if column.count("") == 5:
            return True
    return False


def generate_cards(board):
    cards = []
    card = []
    for i in range(len(board)):
        if board[i] == "":
            cards.append(card)
            card = []
            continue
        card.extend(board[i].split())
        if i == len(board) - 1:
            cards.append(card)
    return cards


def giant_squid(file):
    drawn = open(file).read().splitlines()[0].split(',')
    board = open(file).read().splitlines()[2:]
    cards = generate_cards(board)

    winner = -1
    current_drawn = 0
    for i in range(len(drawn)):
        current_drawn = drawn[i]

        for j in range(len(cards)):
            try:
                index = cards[j].index(current_drawn)
            except ValueError:
                continue

            cards[j][index] = ""

            if i >= 4:
                if check_row(cards[j]) or check_column(cards[j]):
                    winner = j
                    break

        if winner > -1:
            break

    sum = 0
    for i in cards[winner]:
        if i == "":
            continue
        sum += int(i)

    print(sum * int(current_drawn))
