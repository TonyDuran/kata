try:
    from raw_input import input
except ImportError:
    pass

def howManyGames(p, d, m, s):
    """
    p: initial price of a game
    d: discount amount
    m: minimum price for a game
    s: how much money you have
    """
    game_count = 0
    while s >= p:
        s = s - p
        game_count += 1
        if p - d >= m:
            p = p - d
        else:
            p = m
    return game_count

if __name__ == '__main__':
    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)
    print(answer)
