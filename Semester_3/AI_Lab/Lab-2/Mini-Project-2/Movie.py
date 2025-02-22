# MiniProject 2:
# In particular we're going to finding the average budget of the films in our data set, and we're going to identify high budget films that exceed the average budget we calculate.

# The brief
# Below you'll find a list which contains the relevant data about a selection of movies. Each item in the list is a tuple containing a movie name and movie budget in that order:

# movies = [
#     ("Eternal Sunshine of the Spotless Mind", 20000000),
#     ("Memento", 9000000),
#     ("Requiem for a Dream", 4500000),
#     ("Pirates of the Caribbean: On Stranger Tides", 379000000),
#     ("Avengers: Age of Ultron", 365000000),
#     ("Avengers: Endgame", 356000000),
#     ("Incredibles 2", 200000000)
# ]
# For this project, your program should do the following:

# Calculate the average budget of all movies in the data set.
# Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
# Print out how many movies spent more than the average you calculated.
# If you want a little extra challenge, allow users to add more movies to the data set before running the calculations.

# You can do this by asking the user how many movies they want to add, which will allow you to use a for loop and range to repeat some code a given number of times. Inside the for loop, you can write some code that takes in some user input and appends a movie tuple containing the collected data to the movie list.

class movies:
    def __init__(self):
        self.movies = [
            ("Eternal Sunshine of the Spotless Mind", 20000000),
            ("Memento", 9000000),
            ("Requiem for a Dream", 4500000),
            ("Pirates of the Caribbean: On Stranger Tides", 379000000),
            ("Avengers: Age of Ultron", 365000000),
            ("Avengers: Endgame", 356000000),
            ("Incredibles 2", 200000000)
        ]
    
    def add_movie(self):
        n = int(input("\nHow many movies do you want to add? "))
        for i in range(n):
            name = input("\nEnter the name of the movie: ")
            budget = int(input("\nEnter the budget of the movie: "))
            self.movies.append((name, budget))
            i += 1

    
    def average_budget(self):
        total = 0
        avg = sum(movie[1] for movie in self.movies) / len(self.movies)
        return (f"{format(avg, ".2f")}")
    
    def higest_budget(self):
        avg = self.average_budget()
        count = 0
        for movie in self.movies:
            if movie[1] > avg:
                count += 1
        print(f"\n{count} movies had higher budget than average.")
    
    def display_movies(self):
        for movie in self.movies:
            print(f"{movie[0]}: {movie[1]}\n")
movies = movies()
def main():
    while True:
        print(f"\n----------Menu----------\n")
        print(f"1. Add movie")
        print(f"2. Calculate average budget")
        print(f"3. Display movies")
        print(f"4. Display high budget movies")
        print(f"5. Exit")
        try:
            user_input = int(input("Enter the number: "))
            if user_input == 1:
                movies.add_movie()
            elif user_input == 2:
                print(f"\nThe average budget is {movies.average_budget()}")
            elif user_input == 3:
                movies.display_movies()
            elif user_input == 4:
                movies.higest_budget()
            elif user_input == 5:
                break
            else:
                print("Invalid input.")
        except ValueError:
            print(f"Enter a numaric value.")
main()