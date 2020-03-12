def lists_of_games(file_name):
    with open(file_name) as f:
        mylist = [line.split("\t") for line in f]
    return mylist


list_of_games = lists_of_games('game_stat.txt')


def count_games(games_list):
    return len(games_list)

    # count = 0
    # with open(games_list) as f:
    #     for i in f:
    #         count += 1
    # return count


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
    raise ValueError("Game not found")


def sort_abc(games_list):
    sorted_list = []
    for i in games_list:
        if i[0] not in sorted_list:
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


def get_genres(games_list):
    unique_sorted_list = []
    for i in games_list:
        if i[3] not in unique_sorted_list:
            unique_sorted_list.append(i[3])
    return sorted(unique_sorted_list)


def when_was_top_sold_fps(games_list):
    copies_sold = 0
    for i in games_list:
        i[1] = float(i[1])
        if i[1] > copies_sold and i[3] == 'First-person shooter':
            copies_sold = i[1]
            release_year = i[2]
    if release_year:
        return release_year
    else:
        raise ValueError("No Such Year")
