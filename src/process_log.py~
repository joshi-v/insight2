#!/usr/bin/env python

import sys
import argparse
import os
from collections import Counter

class AnalyzeLog(object):
    
    def __init__(self, logfilepath,hostsfilepath,hoursfilepath,resourcesfilepath,blockedfilepath):
        self.logfilepath = logfilepath
        self.hostsfilepath = hostsfilepath
        self.hoursfilepath = hoursfilepath
        self.resourcesfilepath = resourcesfilepath
        self.blockedfilepath = blockedfilepath
        self.top_hosts_counter = Counter()
        self.top_resources_counter = Counter()
        self._parse_log_file()
           
    def _parse_log_file(self):           
        with open(self.logfilepath) as f:
            for line in f:
                line = line.split()
                self.top_hosts_counter.update([line[0]])
                if line[-1] == '-':
                    self.top_resources_counter.update({line[-4]:0})
                else:
                    self.top_resources_counter.update({line[-4]:int(line[-1])})                                    
        with open(self.hostsfilepath,"w") as f:
            for key, val in self.top_hosts_counter.most_common(10):
                f.write(key + ',' + str(val) + os.linesep)

        with open(self.resourcesfilepath,"w") as f:
            for key, val in self.top_resources_counter.most_common(10):
                f.write(key + ',' + str(val) + os.linesep)
        
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Parse log file")
	parser.add_argument("logfilepath", help="path of logfile to be parsed")
	parser.add_argument("hostsfilepath", help="path of hosts.txt")
	parser.add_argument("hoursfilepath", help="path of hours.txt")
	parser.add_argument("resourcesfilepath", help="path of resources.txt")
	parser.add_argument("blockedfilepath", help="path of blocked.txt")
	args = parser.parse_args()
	obj = AnalyzeLog(args.logfilepath, args.hostsfilepath, args.hoursfilepath, args.resourcesfilepath, args.blockedfilepath)
