import json
from urllib.request import urlopen
api_key = '9e5ea419'  # insert your own API key!!!

print("This program allows you to look up information about a movie. It includes only movies which can be found on IMDB")
print('If you want to look up a movie on its title: Press "T"')
print('If you want to look up a movie on its IMDB ID: Press "I"')

while True:
    search = input("Type T if search for title. Type I if search for ID : ")
    if search == "I":
        title_id = input("Type the ID of the movie you want to know more about: ")

        response = urlopen('http://www.omdbapi.com/?i=' + title_id + '&apikey=' + api_key).read()

        data = json.loads(response)

        print(data)

        again = input("Do you want to look up another movie? yes or no?")
        if again[0] == "y" or "Y":
            print("cool, now try again")
        elif again[0] == "n" or "N":
            print("thx for using the program, goodbye")
            break

    elif search == "T":
        title = input("Type the title of the movie you want to know more about: ")
        title = title.replace(" ", "+")

        response = urlopen('http://www.omdbapi.com/?t=' + title + '&apikey=' + api_key).read()

        data = json.loads(response)

        print(data)

        again = input("Do you want to look up another movie? yes or no?")
        if again[0] == "y" or "Y":
            print("cool, now try again")
        elif again[0] == "n" or "N":
            print("thx for using the program, goodbye")
            break
    else:
        print("Please type in either I or T")




#https://www.youtube.com/watch?v=qUKhgX4D9fE
