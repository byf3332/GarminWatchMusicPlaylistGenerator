import os
import icu
from tinytag import TinyTag

# function: read title of each song
def read_title(file_path):
    try:
        tag = TinyTag.get(file_path)
        return tag.title if tag.title else "Unknown Title" 
    except Exception as e:
        print(f"Error reading tag of {file_path}! Will use default title for replacement!")
        return "Unknown Title"

# function: scan directory and gengrate path
def scan_directory(directory):
    audio_titles = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".mp3", ".mp2", ".mp1", ".wma", ".wav", ".flac", ".ogg", ".m4a", ".aac", ".alac", ".aiff")):
                file_path = os.path.join(root, file)
                title = read_title(file_path)
                audio_titles.append((title, file_path)) # create relationship between each file and title
    return audio_titles

# function: sort titles of audio files
def sort_titles(audio_titles):
    collator = icu.Collator.createInstance(icu.Locale("zh-CN.UTF-8")) # use chinese environment
    return sorted(audio_titles, key=lambda x: (0 if x[0].isascii() else 1, collator.getSortKey(x[0])))

# function: create m3u8 playlist
def create_m3u8(sorted_titles, root_directory):
    output_file = os.path.join(root_directory, 'All.m3u8')
    with open(output_file, 'w', encoding='utf-8') as f:
        for title, file_path in sorted_titles:
            relative_path = os.path.relpath(file_path, start=root_directory)
            relative_path = relative_path.replace("\\", "/")
            relative_path = "0:/MUSIC/" + relative_path
            relative_path = relative_path.upper()
            f.write(f'{relative_path}\n')
