# GarminWatchMusicPlaylistGenerator
Numerous models of Garmin watch (fr245m, fr645m, fr265, fr945, fr955 etc.) support importing music and play through bluetooth headphones. But, they **cannot auto sort these songs according to their title (even they can read ID3 tags)** and only displays them as the sequence that user has put them in. 

However, Garmin's computer software (Garmin Express) support using Windows Media Player playlist or itunes playlist to create a .m3u8 file for watch, which gives user **the ability to control the sequence.** So I wrote this little tool to generate a sorted playlist with alphabetical order and also Hanyu Pinyin order to better help users to find their songs. 

## How to run
1. clone the repository or download zip.
2. Enstall requirements:
``pip install -r requirements.txt``
3. Execute``python mainGUI.py``.
4. Or choose the prebuilt file from release.
