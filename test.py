

coord = [1, 2, 6]


match coord[0], coord[1]:
    case [range(0, 3), range(0, 3)]:
        print("zone 1")
    case [range(0, 3), range(3, 6)]:
        print("zone 2")
    case [range(0, 3), range(6, 9)]:
        print('zone 2')
    case _:
        print("case _")

