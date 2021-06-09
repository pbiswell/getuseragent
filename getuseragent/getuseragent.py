"""
Name: GetUserAgents
Author: Paul Biswell
Version: 0.0.7
Link: https://github.com/pbiswell/getuseragent
"""
import random
from getuseragent import retrieve
import logging

version = "0.0.7"

class UserAgent:
    def __init__(self, ua="all", limit=0, total=0, requestsPrefix=False):
        self.ua = ua
        self.limit = limit
        self.total = total
        self.requestsPrefix = requestsPrefix
        self.list = []
        self.version = version
        self.Setup()

    def Format(self, ua):
        """ Returns formatted user agent for requests handler if specified. """
        if self.requestsPrefix == True:
            ua = {"User-Agent": ua}
        return ua
        
    def Setup(self):
        """ Creates user agent list based on your choices. Default is all user agents except bots. """
        if self.ua:
            self.list = retrieve.GetList(self.ua.split('+'), limit=self.limit)
        else:
            self.list = retrieve.GetList(limit=self.limit)
        if self.total > 0:
            random.shuffle(self.list)
            self.list = self.list[0:self.total]
            
    def Random(self):
        """ Returns random user agent based on your chosen settings """
        if len(self.list) > 0:
            return self.Format(random.choice(self.list))
        else:
            logging.error("User agents list empty")
            return