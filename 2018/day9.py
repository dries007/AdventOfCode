def day9(player_count, last_score):
    scores = [0 for _ in range(player_count)]
    circle = [0]

    current = 0
    player = 0

    for marble in range(1, last_score + 1):
        if marble % 23 == 0:
            # print("Special marble")
            scores[player] += marble

            current = current - 7
            if current < 0:
                current += len(circle)

            scores[player] += circle[current]
            del circle[current]
        else:
            current = current + 2
            if current > len(circle):
                current -= len(circle)
            circle.insert(current, marble)

        # print("P:", player + 1, "C:", current, "M:", marble, "Circle:", *circle)
        player = (player + 1) % player_count

    # print(scores)
    return max(scores)


if __name__ == '__main__':
    print(day9(9, 25), "->", 32)
    print(day9(10, 1618), "->", 8317)
    print(day9(13, 7999), "->", 146373)
    print(day9(17, 1104), "->", 2764)
    print(day9(21, 6111), "->", 54718)
    print(day9(30, 5807), "->", 37305)
    # 468 players; last marble is worth 71010 points
    print(day9(468, 71010))
    print(day9(468, 71010*100))
