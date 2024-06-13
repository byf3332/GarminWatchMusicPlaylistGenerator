# GarminWatchMusicPlaylistGenerator
Numerous models of Garmin watch (fr245m, fr645m, fr265, fr945, fr955 etc.) support importing music and play through bluetooth headphones. But, they **cannot auto sort these songs according to their title (even they can read ID3 tags)** and only displays them as the sequence that user has put them in. 

However, Garmin's computer software (Garmin Express) support using Windows Media Player playlist or itunes playlist to create a .m3u8 file for watch, which gives user **the ability to control the sequence.** So I wrote this little tool to generate a sorted playlist with alphabetical order and also Hanyu Pinyin order to better help users to find their songs. 

## Notice
**This tool I created fot myself is only tested on my own fr955solar, but should work on other models.**

## How to run
1. Please use python 3.10.11.
2. clone the repository or download zip.
3. Install requirements:
``pip install -r requirements.txt``
4. Execute``python mainGUI.py``.
5. Or just download the prebuilt file from release and run it (Windows version only!).

## How to use
1. Copy the music file back to your PC from your watch or download your music file
2. Place the music files into a directory acting as a library.
3. In the program click "Choose Folder" and select your library folder.
4. Click "Create Playlist" and now you can find your .m3u8 file in the library folder as All.m3u8.
5. Copy back songs and .m3u8 file, and you may use the "Playlist" section on your watch to find the imported playlist.
6. If you want a different name for your playlist, simply rename All.m3u8 to AnotherName.m3u8.
