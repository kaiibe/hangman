def create_hanger() -> list:
    hanger_list = [[" " for i in range(7)] for j in range(7)]

    hanger_list[0][2] = "+"
    hanger_list[0][3] = '-'
    hanger_list[0][4] = '-'
    hanger_list[0][5] = '+'
    hanger_list[1][2] = "|"

    hanger_list[1][5] = "|"
    hanger_list[2][5] = '|'
    hanger_list[3][5] = '|'
    hanger_list[4][5] = '|'
    hanger_list[5][5] = '|'

    hanger_list[6][0] = "="
    hanger_list[6][1] = '='
    hanger_list[6][2] = '='
    hanger_list[6][3] = '='
    hanger_list[6][4] = '='
    hanger_list[6][5] = '='
    hanger_list[6][6] = '='

    return hanger_list


def hang_it(hanger_list: list, number_of_tries) -> list:

    match number_of_tries:
        case 6:
            hanger_list[2][2] = "O"
        case 5:
            hanger_list[3][2] = "|"
        case 4:
            hanger_list[3][1] = "/"
        case 3:
            hanger_list[3][3] = '\x5c'
        case 2:
            hanger_list[4][2] = "|"
        case 1:
            hanger_list[5][1] = "/"
        case 0:
            hanger_list[5][3] = '\x5c'

    return hanger_list


def print_hanger(hanger) -> None:
    for row in hanger:
        print(''.join(row))
    print()
