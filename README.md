# GetUserAgent - Random/Fake/Spoof Common User Agents

**Table of Contents**
- [GetUserAgent - Random/Fake/Spoof Common User Agents](#getuseragent---randomfakespoof-common-user-agents)
  - [Intro](#intro)
  - [Installation](#installation)
  - [Features](#features)
  - [Use Cases](#use-cases)
  - [Code Examples](#code-examples)
    - [Initialisation](#initialisation)
    - [User-Agents Available](#user-agents-available)
    - [Combination](#combination)
    - [Print Random User Agent From List](#print-random-user-agent-from-list)
    - [Performance / Limiting](#performance--limiting)
    - [Requests Handler](#requests-handler)
  - [To Do](#to-do)
  - [Changes](#changes)
## Intro

This is just a simple python module to produce a random, commonly used user agents each time. It contains 11 lists for a total of 1,100 user agents. You can choose and combine lists depending on your needs.

## Installation

Assumes you have python3 installed.

```
pip install getuseragent
```

## Features

- Get a random user agent of Chrome, Firefox, Safari, Edge, IE, Android, iOS, Windows, Mac, Linux, Desktop, Mobile, Bots, or any combination
- User-Agents from 100 of the most commonly used
- Add requests handler prefix
- Spoofed or fake user agents
- Combine multiple user agent lists

## Use Cases

- Check that your website statistics are identifying browsers correctly
- Handle bots visiting your website
- Making a security system to detect fake user agents?

## Code Examples

### Initialisation

```python
from getuseragent import UserAgent

useragent = UserAgent()

theuseragent = useragent.Random()
print(theuseragent)
```

Example output:

```
Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148
```

### User-Agents Available

Each of the following lists contains 100 commonly used user agents for that software/device/system.

```python
# Firefox
useragent = UserAgent("firefox")

# Chrome
useragent = UserAgent("chrome")

# Safari
useragent = UserAgent("safari")

# Internet Explorer (IE)
useragent = UserAgent("ie")

# Edge
useragent = UserAgent("edge")

# iOS
useragent = UserAgent("ios")

# Android
useragent = UserAgent("android")

# Windows
useragent = UserAgent("windows")

# Mac
useragent = UserAgent("mac")

# Linux
useragent = UserAgent("linux")
```

Sets including multiple lists:

```python
# Desktop (Windows + Mac + Linux)
useragent = UserAgent("desktop")

# Mobile (iOS + Android)
useragent = UserAgent("mobile")

# All (Everything except bots)
useragent = UserAgent()
# or
useragent = UserAgent("all")
```

Bots like web crawlers:

```python
# Bots
useragent = UserAgent("bots")
```

### Combination

You can combine lists and sets together. Use the + sign between list names. Duplicate lists will automatically be removed so there's only 1 of each list at most.

Examples:

```python
# Chrome and Edge and iOS
useragent = UserAgent("chrome+edge+ios")

# Mobile + Firefox
useragent = UserAgent("mobile+firefox")

# All + Bots
useragent = UserAgent("all+bots")

# Print a random user agent based on your selection:
print(useragent.Random())
```

### Print Random User Agent From List

You can print a single random user agent like so:

```python
# Initialise
useragent = UserAgent()

# Get one random user agent
ua = useragent.Random()

# Print user agent
print(ua)
```

### Performance / Limiting

You can limit the total amount of user agents in the list to save memory. The default is no limit, and each list has 100 commonly used user agents.

```python
# Using 3 lists would make the total available user agents 300
useragent = UserAgent("chrome+firefox+ios")

# You can limit the total to, for example, 50:
# (List is randomised before truncating)
useragent = UserAgent("chrome+firefox+ios", total=50)

# You can limit individual lists
# This would give 10 firefox user agents + 10 safari user agents
# The total amount of user agents available would be 20
useragent = UserAgent("firefox+safari", limit=10)

# You can combine limit and total
# This would get 10 user agents for both android and ie, for 20 user agents
# The list would be randomised, then reduced to 15 total available user agents
useragent = UserAgent("android+ie", limit=10, total=15)

# Print a random user agent
print(useragent.Random())
```

### Requests Handler

You can enable the option to return your user agents ready to be used with the requests module.

```python
# Example
import requests
from getuseragent import UserAgent

myuseragent = UserAgent("all", requestsPrefix=True).Random()

# Example Output:
# --
# {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}

page = requests.get("https://google.com", headers=myuseragent)
```

## To Do

- Error handling
- Retrieve updated, most popular user-agents from the internet
- Better performance
- Hot-swappable lists
- Custom list(s)
- Command line arguments
- Improve Readme

## Changes

- 0.0.7 (June 9th, 2021)

```
1. Added individual list limits, which can be used when using one or multiple lists.
For example, if you used:

UserAgent("firefox+ios", limit=5)

It would limit each list to 5 user agents, and two lists, bringing the total user agents 10.

2. Checks if user agent files exist.
3. Checks if user list empty in Random()
```

- 0.0.2 - 0.0.6
  
```
Fixed package errors, spelling mistakes
```

- 0.0.1

```
Initial release
```