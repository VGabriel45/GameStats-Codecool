import reports


def enter_file_name():
    file_name = reports.lists_of_games(input('Enter file name: '))
    return file_name


file_name = enter_file_name()


def check_how_many_games():
    print('How many games are in the file?')
    return reports.count_games(file_name)


def year_check():
    year = input('What year do you want to check? ')
    return reports.decide(file_name, year)


def get_latest_game():
    print('Which is the latest game?')
    return reports.get_latest(file_name)


def count_games_by_genre():
    genre = input('What genre do you want to check? ')
    return reports.count_by_genre(file_name, genre)


def get_line_number_by_title():
    title = input('What title do you want to check? ')
    return f'The line number of {title} is {reports.get_line_number_by_title(file_name, title)}'


def sort_titles():
    print('Can you give me the alphabetically ordered list of the titles?')
    return reports.sort_abc(file_name)


def get_genres():
    print('Which genres occur in the data file? ')
    return reports.get_genres(file_name)


def get_top_sold_fps():
    print('What is the release year of the top sold first-person shooter game? ')
    return reports.when_was_top_sold_fps(file_name)


def main():
    print(check_how_many_games())
    print(year_check())
    print(get_latest_game())
    print(count_games_by_genre())
    print(get_line_number_by_title())
    print(sort_titles())
    print(get_genres())
    print(get_top_sold_fps())


if __name__ == "__main__":
    main()
