from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None):
    queryset = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title, movie_description, genres_ids=None,
                 actors_ids=None):
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids is not None:
        new_movie.genres.set(genres_ids)

    if actors_ids is not None:
        new_movie.actors.set(actors_ids)

    return new_movie
