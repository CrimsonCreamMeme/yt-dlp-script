import os
thisis=input("Enter URL\n")
cawk=input("Please chose an option:\n1. Download video/stream.\n2. Download MP3.\n3. Stream download (experimental, will not work on streams has disabled back seeking)\n")
match cawk:
    case "1":
        os.system('yt-dlp -f "b" '+thisis)
    case "2":
        os.system('yt-dlp -f "bestaudio" -x --audio-format mp3 --audio-quality 0 '+thisis)
    case "3":
        os.system('yt-dlp --live-from-start -f "b" '+thisis)
