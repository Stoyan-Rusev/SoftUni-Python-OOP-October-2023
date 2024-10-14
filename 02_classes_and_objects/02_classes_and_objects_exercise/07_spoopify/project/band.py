from project.album import Album
from typing import List


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        for current_album in self.albums:
            if current_album == album:
                return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for current_album in self.albums:
            if current_album.name == album_name:
                if not current_album.published:
                    self.albums.remove(current_album)
                    return f"Album {album_name} has been removed."
                elif current_album.published:
                    return "Album has been published. It cannot be removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = [f"Band {self.name}"]
        for current_album in self.albums:
            result.append(f"{current_album.details()}")
        return "\n".join(result)
