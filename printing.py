def menu():
    with open('answers.txt', 'w+') as f:
        f.write('')
    print('1.How many games are in the file?\n2.Is there a game from a given year\n3.Which is the latest game?\n4.How many games are in the file by genre?')
    print('5.What is the line number of a given title?\n6.Can you give me the alphabetically ordered list of the titles?\n7.Which genres occur in the data file?')
    print('8.What is the release year of the top sold first-person shooter game?')


if __name__ == "__main__":
    menu()
