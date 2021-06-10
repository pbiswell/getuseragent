#
# This is a list of examples to get random user agents
#

# Import the package
from getuseragent import UserAgent

#
# Individual lists of user agents
# --
# These are lists of user agents specific to a platform, device, or operating system
# Each list contains 100 commonly used user agents
#

# Firefox
# Print a random user agent of Firefox
# Example output:
#
# Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0
useragent = UserAgent("firefox")
randUseragent = useragent.Random()
print(randUseragent)

# Chrome
# Print a random user agent of Chrome
# Example output:
#
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
useragent = UserAgent("chrome")
randUseragent = useragent.Random()
print(randUseragent)

# Safari
# Print a random user agent of Safari
# Example output:
#
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15
useragent = UserAgent("safari")
randUseragent = useragent.Random()
print(randUseragent)

# Internet Explorer (IE)
# Print a random user agent of IE
# Example output:
#
# Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322)
useragent = UserAgent("ie")
randUseragent = useragent.Random()
print(randUseragent)

# Edge
# Print a random user agent of Edge
# Example output:
#
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45
useragent = UserAgent("edge")
randUseragent = useragent.Random()
print(randUseragent)

# iOS
# Print a random user agent of iOS
# Example output:
#
# Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1
useragent = UserAgent("ios")
randUseragent = useragent.Random()
print(randUseragent)

# Android
# Print a random user agent of Android
# Example output:
#
# Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36
useragent = UserAgent("android")
randUseragent = useragent.Random()
print(randUseragent)

# Windows
# Print a random user agent of Windows
# Example output:
#
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063
useragent = UserAgent("windows")
randUseragent = useragent.Random()
print(randUseragent)

# Mac
# Print a random user agent of Mac
# Example output:
#
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7
useragent = UserAgent("mac")
randUseragent = useragent.Random()
print(randUseragent)

# Linux
# Print a random user agent of Linux
# Example output:
#
# Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0
useragent = UserAgent("linux")
randUseragent = useragent.Random()
print(randUseragent)

#
# Sets of user agents
# These are multiple lists from above attached together
# 
# Available sets:
# Desktop (Windows + Mac + Linux)
# Mobile (Android + iOS)
# All (Firefox + Safari + Chrome + Edge + IE + iOS + Android)
# 

# Desktop (Windows + Mac + Linux)
# Print a random user agent in the Desktop set
useragent = UserAgent("desktop")
randUseragent = useragent.Random()
print(randUseragent)

# Mobile (iOS + Android)
# Print a random user agent in the Mobile set
useragent = UserAgent("mobile")
randUseragent = useragent.Random()
print(randUseragent)

# All (Everything except bots)
# Print a random user agent in the All set
useragent = UserAgent()
randUseragent = useragent.Random()
print(randUseragent)
# or
useragent = UserAgent("all")
randUseragent = useragent.Random()
print(randUseragent)

#
# Bots
# These are user agents for bots, like search engine crawlers
#

# Bots
# Print a random user agent in the bots list
useragent = UserAgent("bots")
randUseragent = useragent.Random()
print(randUseragent)