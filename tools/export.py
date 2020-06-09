#!/usr/bin/env python

''' Tool for converting the MASVS requirements to various formats.

    Usage: ./export.py [--format <csv/xml/json>] [--lang <en>] [--out <outfile>]

    By Bernhard Mueller, updated by Jeroen Beckers & Théo Rigas.

    Copyright (c) 2020 OWASP Foundation

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    '''

import argparse
from isvs import ISVS

parser = argparse.ArgumentParser(description='Export the ISVS requirements. Default language is en.')
parser.add_argument('-f', '--format', choices=['json', 'xml', 'csv'], required=True, help="Desired output format")
parser.add_argument('-l', '--lang', choices=['en'], default='en', help="Document language")
parser.add_argument("-o", "--out", required=False, help="Name of output file (optional)",)

args = parser.parse_args()

doc = ISVS(args.lang)
out_format = args.format
result = None

if out_format == "csv":
    result = doc.to_csv()
elif out_format == "xml":
    result = doc.to_xml()
else:
    result = doc.to_json()

if args.out: 
    # save to file
    filename = "{}.{}".format(args.out,out_format)
    with open(filename,"w") as out_file:
        out_file.write(result)
else:
    print(result)



