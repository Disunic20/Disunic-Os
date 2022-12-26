from instascrape import Reel
import time

# session id
SESSIONID = "13569786190%3A3lDXayJmdifKEN%3A16%3AAYeOi2ysmlL79OesdL8wgw_3U0ofzbPzCUlPC-tukg"

# Header with session id
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
	Safari/537.36 Edg/79.0.309.43",
	"cookie": f'sessionid={SESSIONID};'
}

# Passing Instagram reel link as argument in Reel Module
insta_reel = Reel(
	'https://www.instagram.com/reel/Ck7ijnLJ2aO/?utm_source=ig_web_copy_link')

# Using scrape function and passing the headers
insta_reel.scrape(headers=headers)

# Giving path where we want to download reel to the
# download function
insta_reel.download(fp=f".\\Desktop\\reel{int(time.time())}.mp4")

# printing success Message
print('Downloaded Successfully.')
