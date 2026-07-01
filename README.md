# Music Query System

A lightweight Python system for managing users, albums, and music queries.

## Features
- Add users (age, city, albums)
- Add albums (artist, genre, tracks)
- Query track totals by user, age, or city based on artist or genre

## Example
```python
add_user("erfan", 25, "Tehran", ["Album1"], all_users)
add_album("Album1", "ArtistA", "Pop", 12, all_albums)
print(query_user_artist("erfan", "ArtistA", all_users, all_albums))
```
