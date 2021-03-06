#!/usr/bin/env python

import sys
import argparse
from collections import Counter

class AnalyzeLog(object):
    
    def __init__(self, logfilepath):
        self.logfilepath = logfilepath
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
        f = open("                    
        print self.top_hosts_counter.most_common(10)         
        print self.top_resources_counter.most_common(10)
            
        
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Parse log file")
	parser.add_argument("logfilepath", help="path of logfile to be parsed")
	args = parser.parse_args()
	print args
	obj = AnalyzeLog(args.logfilepath)
