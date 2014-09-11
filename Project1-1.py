
#!/usr/bin/env python
# Filename: Project1-1.py

import re
import os
import codecs
import timeit

from collections import OrderedDict


start = timeit.default_timer()

#dateregexp= re.compile("201407[0-3][0-9]")

unregexp= re.compile(r".* "r".* "r"(?P<unfilteredaccess>[0-9]+) "r"[0-9]+")

regexp = re.compile(r"^en "r"(?P<pagetitle>[^a-z].*) "r"(?P<access>[0-9]+) "r"[0-9]+")

f = codecs.open('/Users/Preston/Desktop/pagecounts-20140701-000000')
#f = open('/Users/Preston/Desktop/pagecounts-20140701-000000')

#date = os.environ['map_input_file'].substring(dateregexp)

date = "20140701"


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

for line in f.readlines():

    count = count+1

    if unregexp.search(line): #have to specifiy this line for further step!!!!!!!#

        original = unregexp.search(line)

        originalAccess = int(original.group('unfilteredaccess'))

        accesstotal = originalAccess + accesstotal

    if regexp.search(line):
        
        result = regexp.search(line)

        if result != None:
            
            Pagetitle = result.group('pagetitle')

            NumAccess = int(result.group('access'))            
 
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
                        
                        D[Pagetitle+"-"+ date] = NumAccess

print("filtering finished")
print("before: "+ str(count))
print("before, totalAccess: " + str(accesstotal))
print("after: " + str(len(D)))

stop = timeit.default_timer()

print (stop-start)

fwrite = codecs.open('/Users/Preston/Desktop/result1.txt', 'w', encoding='latin1')
#fwrite = codecs.open('/Users/Preston/Desktop/result.txt', 'w', encoding='ISO-8859-1')
fwrite = open('/Users/Preston/Desktop/result1.txt', 'w')

for word in sorted(D, key=D.get, reverse=True):

    fwrite.write(word +' '+ str(D[word]) +'\n')
                       
f.close()

    





    
