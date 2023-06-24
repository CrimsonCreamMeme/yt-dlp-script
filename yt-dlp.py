import os
url=input("Enter URL\n")
choice=input("Please chose an option:\n1. Download video/stream.\n2. Download MP3.\n3. Stream download (experimental, will not work on streams has disabled back seeking)\n")
match choice:
    case "1":
        os.system('yt-dlp -f "b" --embed-metadata '+url)
    case "2":
        os.system('yt-dlp -f "bestaudio" -x --audio-format mp3 --audio-quality 0 --embed-metadata '+url)
    case "3":
        os.system('yt-dlp --live-from-start -f "b" --embed-metadata '+url)
