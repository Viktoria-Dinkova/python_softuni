from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int) -> str:
        if username in User.USERS_NAMES:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie) -> str:
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user = self._find_user(username)
        if not user:
            raise Exception("This user does not exist!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs) -> str:
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = self._find_user(username)
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k, v in kwargs.items():
            setattr(movie, k, v)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie) -> str:
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = self._find_user(username)
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie) -> str:
        user = self._find_user(username)
        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie) -> str or None:
        user = self._find_user(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self) -> str:
        if not self.movies_collection:
            return "No movies found."

        sort_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))
        return '\n'.join(sm.details() for sm in sort_movies)

    def __str__(self):
        result = []

        if not self.users_collection:
            result.append("All users: No users.")
        result.append(f"All users: {', '.join([u.username for u in self.users_collection])}")

        if not self.movies_collection:
            result.append("All movies: No movies.")
        result.append(f"All movies: {', '.join([m.title for m in self.movies_collection])}")


        return '\n'.join(result)



    ############## helper
    def _find_user(self, name) -> User:
        try:
            return next(filter(lambda u: u.username == name, self.users_collection))
        except StopIteration:
            pass
