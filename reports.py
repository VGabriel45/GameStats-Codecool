def lists_of_games(file_name):
    with open(file_name) as f:
        mylist = [line.split("\t") for line in f]
    return mylist


def count_games(games_list):
    return len(games_list)


def decide(games_list, year):
    for i in games_list:
        if str(year) in i:
            return True
    else:
        return False


def get_latest(games_list):
    dict = {}
    list_of_years = []
    for i in games_list:
        dict[i[2]] = i[0]
        list_of_years.append(i[2])
        list_of_years.sort()
    latest = list_of_years[-1]
    return dict[latest]


def count_by_genre(games_list, genre):
    count = 0
    for lst in games_list:
        if genre in lst:
            count += 1
    return count


def get_line_number_by_title(games_list, title):
    count = 0
    for lst in games_list:
        count += 1
        if title == lst[0]:
            return count


def sort_abc(games_list):
    sorted_list = []
    for i in games_list:
        sorted_list.append(i[0])
    while True:
        swaped = False
        for i in range(0, len(games_list)-1):
            if sorted_list[i] > sorted_list[i+1]:
                sorted_list[i], sorted_list[i +
                                            1] = sorted_list[i+1], sorted_list[i]
                swaped = True
        if not swaped:
            return sorted_list


def main():
    list_of_games = lists_of_games('game_stat.txt')
    # print(list_of_games)
    # print(count_games(list_of_games))
    # print(decide(list_of_games, 2004))
    # print(get_latest(list_of_games))
    # print(count_by_genre(list_of_games, 'Simulation'))
    # print(get_line_number_by_title(list_of_games, 'Counter-Strike: Condition Zero'))
    # print(sort_abc(list_of_games))


if __name__ == "__main__":
    main()
