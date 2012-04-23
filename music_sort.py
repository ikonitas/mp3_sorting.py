import os
import shutil
import eyeD3
import sys

unknow_artist_dir = "Unknown Artist"

def find_song_(directory):
    directory = os.path.normpath(directory) + os.sep
    for song in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, song)) or "mp3" not in song:
            pass
        else:
            tag = eyeD3.Tag()
            try:
                if tag.link(os.path.join(directory, song)):
                    if tag.getArtist():
                        if not os.path.exists(directory + tag.getArtist()):
                            os.mkdir(directory + tag.getArtist())
                            shutil.move(song, directory + tag.getArtist())
                        else:
                            try:
                                shutil.move(song, directory + tag.getArtist())
                            except:
                                os.remove(os.path.join(directory, song))

                    else:
                         if not os.path.exists(directory + unknow_artist_dir):
                            os.mkdir(directory + unknow_artist_dir)
                            shutil.move(song, directory + unknow_artist_dir)
                         else:
                            try:
                                shutil.move(song, directory + unknow_artist_dir)
                            except:
                                os.remove(os.path.join(directory, song))
            except:
                pass
            
if __name__ == "__main__":
    directory = sys.argv[1]
    find_song_(directory)
