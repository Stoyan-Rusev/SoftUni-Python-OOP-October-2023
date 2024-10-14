from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page in self.photos:
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return (f"{label} photo added successfully "
                        f"on page {self.photos.index(page) + 1} slot {page.index(label) + 1}")
        return f"No more free slots"

    def display(self):
        separator = 11 * '-' + '\n'
        result = separator
        for page in self.photos:
            result += ' '.join(['[]' for _ in page]) + '\n'
            result += separator
        return result

# album_one = PhotoAlbum(4)
# print(album_one.add_photo('Summer'))
# print(album_one.add_photo('Winter'))
# print(album_one.add_photo('Autumn'))
# print(album_one.add_photo('Spring'))
# print(album_one.add_photo('New Year'))
# print(album_one.display())
# print()
#
# album_two = PhotoAlbum.from_photos_count(4)
# print(album_two.add_photo('Something'))
# print(album_two.add_photo('Something'))
# print(album_two.add_photo('Something'))
# print(album_two.add_photo('Something'))
# print(album_two.add_photo('Something'))
# print(album_two.display())


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
