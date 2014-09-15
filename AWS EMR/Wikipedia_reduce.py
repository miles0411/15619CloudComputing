#!/usr/bin/python
# Filename: Project1-2_map.py

import re
import sys
import os

def main(argv):

    T = {}
    d = {}
    current_title = None
    current_date = None
    date = None
    current_count = 0
    word = None

    # input comes from STDIN
    for line in sys.stdin:
        
        # parse the input we got from mapper.py
        title, date, count = line.strip().split('\t')
        
        try:
            count = (int)(count)
            
        except ValueError:
            
            continue


        if current_title == title:
            
            if date in d:

                tmp =  d[date] 
                
                d[date]= count + tmp  #same date
                    
            else:
                
                d[date] =  count #acumulate date
                current_date = date
                
        else:
            
            if current_title:

                concatenation = ""
 
                for eachDate, subtotal in dict.items(d):

                    eachDatesubTotal = eachDate +":"+ (str)(subtotal) + '\t'

                    concatenation += eachDatesubTotal

                if sum(d.values())>100000:
                    
                    print (str)(sum(d.values()))+ '\t'+ current_title + '\t' + concatenation

                d = {}
                            
            d[date] = count
            current_count = count
            current_date = date
            current_title = title


    if current_title:

            concatenation = ""

            for eachDate, subtotal in dict.items(d):

                eachDatesubTotal = eachDate +":"+ (str)(subtotal) + '\t'

                concatenation += eachDatesubTotal

            if sum(d.values())>100000:
                
                print (str)(sum(d.values()))+ '\t'+ current_title + '\t' + concatenation           


if __name__ == "__main__":
    main(sys.argv)
