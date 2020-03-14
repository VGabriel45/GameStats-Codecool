import reports
import printing


def enter_file_name():
    file_name = reports.lists_of_games(input('Enter file name: '))
    return file_name


file_name = enter_file_name()


def check_how_many_games():
    with open('answers.txt', 'a+') as f:
        f.write(str(reports.count_games(file_name)))
        return reports.count_games(file_name)


def year_check():
    year = input('What year do you want to check? ')
    with open('answers.txt', 'a+') as f:
        f.write(str(reports.decide(file_name, year)))
    return reports.decide(file_name, year)


def get_latest_game():
    with open('answers.txt', 'a+') as f:
        f.write(str(reports.get_latest(file_name)))
    return reports.get_latest(file_name)


def count_games_by_genre():
    genre = input('What genre do you want to check? ')
    with open('answers.txt', 'a+') as f:
        f.write(str(reports.count_by_genre(file_name, genre)))
    return reports.count_by_genre(file_name, genre)


def get_line_number_by_title():
    title = input('What title do you want to check? ')
    with open('answers.txt', 'a+') as f:
        f.write(str(reports.get_line_number_by_title(file_name, title)))
    return f'The line number of {title} is {reports.get_line_number_by_title(file_name, title)}'


def sort_titles():
    with open('answers.txt', 'a+') as f:
        f.write(str(reports.sort_abc(file_name)))
    return reports.sort_abc(file_name)


def get_genres():
    with open('answers.txt', 'a+') as f:
        f.write(str(reports.get_genres(file_name)))
    return reports.get_genres(file_name)


def get_top_sold_fps():
    with open('answers.txt', 'a+') as f:
        f.write(str(reports.when_was_top_sold_fps(file_name)))
    return reports.when_was_top_sold_fps(file_name)


def main():
    on = True
    while on:
        printing.menu()
        user_input = input('Choose from above: ')
        if user_input == '1':
            print(check_how_many_games())
            input()
        if user_input == '2':
            print(year_check())
            input()
        if user_input == '3':
            print(get_latest_game())
            input()
        if user_input == '4':
            print(count_games_by_genre())
            input()
        if user_input == '5':
            print(get_line_number_by_title())
            input()
        if user_input == '6':
            print(sort_titles())
            input()
        if user_input == '7':
            print(get_genres())
            input()
        if user_input == '8':
            print(get_top_sold_fps())
            input()
        if user_input == 'quit':
            on = False


if __name__ == '__main__':
    main()
