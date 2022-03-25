def film_serializer(film) -> dict:
    return {
        "id": str(film["_id"]),
        "name": film["name"],
        "genre": film["genre"],
        "mark": film["mark"],
        "created_at": film["created_at"],
        "updated_at": film["updated_at"],
        "comments": film["comments"],
    }


def films_serializer(films) -> list:
    return [film_serializer(film) for film in films]
