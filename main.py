all_users = {}
all_albums = {}

def add_user(username: str, age: int, city: str, albums: list, all_users: dict) -> None:
    all_users[username] = {
        "age": age,
        "city": city,
        "albums": albums
    }

def add_album(name: str, artist: str, genre: str, tracks: int, all_albums: dict) -> None:
    all_albums[name] = {
        "artist": artist,
        "genre": genre,
        "tracks": tracks
    }

def query_user_artist(username: str, artist: str, all_users: dict, all_albums: dict) -> int:
    total = 0
    if username in all_users:
        for album_name in all_users[username]["albums"]:
            if album_name in all_albums and all_albums[album_name]["artist"] == artist:
                total += all_albums[album_name]["tracks"]
    return total

def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    total = 0
    if username in all_users:
        for album_name in all_users[username]["albums"]:
            if album_name in all_albums and all_albums[album_name]["genre"] == genre:
                total += all_albums[album_name]["tracks"]
    return total

def query_age_artist(age: int, artist: str, all_users: dict, all_albums: dict) -> int:
    total = 0
    for user_info in all_users.values():
        if user_info["age"] == age:
            for album_name in user_info["albums"]:
                if album_name in all_albums and all_albums[album_name]["artist"] == artist:
                    total += all_albums[album_name]["tracks"]
    return total

def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    total = 0
    for user_info in all_users.values():
        if user_info["age"] == age:
            for album_name in user_info["albums"]:
                if album_name in all_albums and all_albums[album_name]["genre"] == genre:
                    total += all_albums[album_name]["tracks"]
    return total

def query_city_artist(city: str, artist: str, all_users: dict, all_albums: dict) -> int:
    total = 0
    for user_info in all_users.values():
        if user_info["city"] == city:
            for album_name in user_info["albums"]:
                if album_name in all_albums and all_albums[album_name]["artist"] == artist:
                    total += all_albums[album_name]["tracks"]
    return total

def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    total = 0
    for user_info in all_users.values():
        if user_info["city"] == city:
            for album_name in user_info["albums"]:
                if album_name in all_albums and all_albums[album_name]["genre"] == genre:
                    total += all_albums[album_name]["tracks"]
    return total
