    """
    Write a function called "movie_organizer" that groups movies by genre.
     The function will receive a different number of arguments, passed as tuples containing two elements: the first one is the movie's name, and the second is the genre for example ("Movie Name", "Genre").
    The function should sort the movies by their genre. Arrange Mary's collection by the number of movies in each genre in descending order.
     If two or more genres have the same number of movies, return them in ascending order (alphabetically) by genre.
    Each genre group should be sorted in ascending order (alphabetically) by the movie's name.
    To help Mary keep track of her movies, add next to each genre the number of movies in the group.
    In the end, return the output as described below.
    Note: Submit only the function in the judge system
    Input
    •	There will be no input from the console, just parameters passed to your function
    Output
    •	The output should look like this:
    "{genre_1} - {number_of_movies_in_the_genre_group}
    * {movie_name_1}
    …
    * {movie_name_n}
    {genre_2} - {number_of_movies_in_the_genre_group}
    * {movie_name_1}
    …
    * {movie_name_n}
    {genre_n} - {number_of_movies_in_the_genre_group}
    * {movie_name_1}
    …
    * {movie_name_n}"
    """
    def movie_organizer(*movies):
        collection = {}
        result = ""
        for movie in movies:
            name = movie[0]
            genre = movie[1]

            if genre not in collection:
                collection[genre] = [name]
            else:
                collection[genre].append(name)

        for k, v in (sorted(collection.items(), key=lambda item: (-len(item[1]), item[0]))):
            result += f"{k} - {len(collection[k])}\n"
            for el in sorted(v):
                result += f"* {el}\n"

        return result


    # print(movie_organizer(
    #     ("The Godfather", "Drama"),
    #     ("The Hangover", "Comedy"),
    #     ("The Shawshank Redemption", "Drama"),
    #     ("The Pursuit of Happiness", "Drama"),
    #     ("The Hangover Part II", "Comedy")))
