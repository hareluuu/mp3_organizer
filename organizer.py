import os


def load_tags(song):

    tags = song.read(128)
    tags = tags.decode("latin-1")

    if tags.startswith("ID3"):
        return tags
    else:
        print("No ID3v2 tags found")


def sanitize_tag(tag):
    for i in tag:
        for j in range(32):
            if chr(j) == i:
                tag = tag.strip(i)
    return tag


def extract_tags(tags):

    title = tags[tags.find("TIT2") + 4:tags.find("TPE1")]
    artist = tags[tags.find("TPE1") + 4: tags.find("TALB")]
    album = tags[tags.find("TALB") + 4: tags.find("TYER")]

    return title, artist, album


os.chdir("/home/haris/Music/Deezloader")

with open("03 - Rihanna - Hard.mp3", "rb") as song:
    tags = load_tags(song)
    title, artist, album = extract_tags(tags)
    title = sanitize_tag(title)
    artist = sanitize_tag(artist)
    album = sanitize_tag(album)

print(artist, "-", title, album)