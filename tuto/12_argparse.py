#!python

import argparse
import sys

#parser = argparse.ArgumentParser(description='Process some integers.')
#parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
#parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')
#
#args = parser.parse_args()
#print(args.accumulate(args.integers))

#transpose=False

parser = argparse.ArgumentParser(description='Translate SPICE3 raw data into CSV file format')
parser.add_argument('-t', 
                    action='store_true',
                    dest='t',
                    help='transpose data'
                    )

parser.add_argument('-o', 
                    default='out.csv',
                    dest='outfile',
                    help='output CSV filename (default is out.csv)',
                    type=str 
                    )

parser.add_argument('inputfile', 
                    help='input raw file (mandatory)',
                    type=str 
                    )

args=parser.parse_args()

print(args)
print(args.t)
print(args.outfile)
print(args.inputfile)
