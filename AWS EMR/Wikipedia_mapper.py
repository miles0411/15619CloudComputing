#!/usr/bin/python
# Filename: Project1-2_map.py

import re
import sys
import os
import timeit

def main(argv):    

    regexp = re.compile(r"^en "r"(?P<pagetitle>[^a-z].*) "r"(?P<access>[0-9]+) "r"[0-9]+")

    filename = os.environ["map_input_file"]

    date = filename[40:48]

    D ={}

    Start =["Media:",
    "Special:",
    "Talk:",
    "User:",
    "User_talk:",
    "Project:",
    "Project_talk:",
    "File:",
    "File_talk:",
    "MediaWiki:",
    "MediaWiki_talk:",
    "Template:",
    "Template_talk:",
    "Help:",
    "Help_talk:",
    "Category:",
    "Category_talk:",
    "Portal:",
    "Wikipedia:",
    "Wikipedia_talk:"]

    End = [".jpg", ".gif", ".png", ".JPG", ".GIF", ".PNG", ".txt", ".ico"]

    Match = ["404_error/",
    "Main_Page",
    "Hypertext_Transfer_Protocol",
    "Favicon.ico",
    "Search"]

    count = 0
    accesstotal = 0

    for line in sys.stdin:


        if line.startswith("en"):

            if regexp.search(line):
            
                result = regexp.search(line)

                if result != None:
                
                    Pagetitle = result.group('pagetitle')
 
                    NumAccess = result.group('access')           
     
                    for i in Start:
          
                        if Pagetitle.startswith(i):
                            break
                    else:
                        for j in End:
                         
                             if Pagetitle.endswith(j):
                                break
                        else:
                            
                            for l in Match:
                           
                                if Pagetitle == l:
                                    break
                            else:
                            
                                print Pagetitle +'\t'+ date +'\t'+ NumAccess

                       
if __name__ == "__main__":
    main(sys.argv)

    





    
