import re
import instaloader
from yt_dlp import YoutubeDL

def download_youtube(url):
    
    try:
        ydl_opts = {
            "outtmpl": "%(title)s.%(ext)s",   # Saves with video title
            "format": "bestvideo+bestaudio/best"
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(" YouTube video downloaded successfully!")
    except Exception as e:
        print(f" Error: {e}")

def download_instagram(url):
  
    try:
        loader = instaloader.Instaloader()
        post_shortcode = re.search(r"instagram\.com/.*/([^/?]+)", url).group(1)
        post = instaloader.Post.from_shortcode(loader.context, post_shortcode)
        loader.download_post(post, target="InstagramDownloads")
        print(" Instagram reel/video downloaded successfully!")
    except Exception as e:
        print(f" Error: {e}")

def main():
    url = input("Enter YouTube or Instagram video URL: ").strip()

    if "youtube.com" in url or "youtu.be" in url:
        choice = input("This is a YouTube link. Do you want to download it? (y/n): ").lower()
        if choice == "y":
            download_youtube(url)
        else:
            print(" Download cancelled.")
    elif "instagram.com" in url:
        choice = input("This is an Instagram link. Do you want to download it? (y/n): ").lower()
        if choice == "y":
            download_instagram(url)
        else:
            print(" Download cancelled.")
    else:
        print(" Invalid URL! ")

if __name__ == "__main__":
    main()
