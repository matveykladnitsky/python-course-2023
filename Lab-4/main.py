from enum import Enum

START_POINT = 15
EMPTY_INVENTORY_SLOT = ''


class Item(Enum):
    RIFLE = 'в'
    PISTOL = 'п'
    AMMO = 'б'
    AID = 'а'
    INHALER = 'и'
    KNIFE = 'н'
    AXE = 'т'
    AMULET = 'о'
    FLASK = 'ф'
    ANTIDOT = 'д'
    FOOD = 'к'
    CROSSBOW = 'р'


INVENTORY = ((3, 25, Item.RIFLE), (2, 15, Item.PISTOL), (2, 15, Item.AMMO),
             (2, 20, Item.AID), (1, 5, Item.INHALER), (1, 15, Item.KNIFE),
             (3, 20, Item.AXE), (1, 25, Item.AMULET), (1, 15, Item.FLASK),
             (1, 10, Item.ANTIDOT), (2, 20, Item.FOOD), (2, 20, Item.CROSSBOW))


def arrange_inventory(INVENTORY, A):
    backpack = []
    n = len(INVENTORY)

    V = [[0 for _ in range(A + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif INVENTORY[i - 1][0] <= a:
                V[i][a] = max(INVENTORY[i - 1][1] + V[i - 1]
                              [a - INVENTORY[i - 1][0]], V[i - 1][a])
            else:
                V[i][a] = V[i - 1][a]

    result = V[n][A]
    a = A

    for i in range(len(INVENTORY), 0, -1):
        if result <= 0:
            break
        if result == V[i - 1][a]:
            continue
        else:
            backpack.append(i)
            a -= INVENTORY[i - 1][0]
            result -= INVENTORY[i - 1][1]

    return backpack


def init_inventory(X, Y):
    return [[EMPTY_INVENTORY_SLOT for _ in range(Y)] for _ in range(X)]


def count_points(INVENTORY):
    return sum(item[1] for item in INVENTORY)


def complete_task(grid):
    slots = init_inventory(grid[0], grid[1])

    x = 0
    y = 0

    points = 0

    for n in arrange_inventory(INVENTORY, 9):
        points += INVENTORY[n - 1][1]

        for _ in range(INVENTORY[n - 1][0]):
            slots[x][y] = INVENTORY[n - 1][2]
            y = (y + 1) % 3
            x += (y == 0)

    for i in slots:
        print(i)

    result = count_points(INVENTORY)
    answer = START_POINT - result + 2 * points

    print(f'points: {answer}')


complete_task([3, 3])
