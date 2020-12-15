#!/usr/bin/env python

""" ISVS document parser and converter class.

    Original script by Bernhard Mueller, Jeroen Beckers for the MASVS. 
    Updated by Théo Rigas for the ISVS.

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

    """

import os
import re
import json
from xml.sax.saxutils import escape
import csv

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class ISVS:
    """ Creates requirements list out of markdown files. """
    requirements = []

    def __init__(self, lang):

        target = "../{}".format(lang)

        for file in os.listdir(target):

            if re.match("V\d{1,}", file):
                for line in open(os.path.join(target, file)):
                    # group 1: (\d\.\d+\.*\d*) ID 
                    # group 2:  (.*?) Description
                    # group 3 : (.*?) L1
                    # group 4 : (.*?) L2
                    # group 5 : (.*?) L3
                    regex = re.compile(r'\*\*(\d\.\d+\.*\d*)\*\*\s\|\s{0,1}(.*?)\s{0,1}\|\s{0,1}(.*?)\s{0,1}\|\s{0,1}(.*?)\s{0,1}\|(\s{0,1}(.*?)\s{0,1}\|)?')
                    # Add if needed in the future
                    # if lang=="fa" :
                    #    line=line.decode('utf-8')
                    match = re.search(regex, line)

                    if match:
                        req = {}

                        req['ID'] = match.group(1).strip()
                        req['Description'] = match.group(2).strip()
                        #req['category'] = match.group(2).replace(u"\u2011", "-")
                        req['L1'] = len(match.group(3).strip()) > 0
                        req['L2'] = len(match.group(4).strip()) > 0
                        # [:-1] removes the last "|" from the match
                        req['L3'] = len(match.group(5)[:-1].strip()) > 0

                        self.requirements.append(req)

        # Since we are not yet using V01,V02 etc.  but V1,V2 etc., the requirements files are not 
        # being read in order, so requirements are not sorted. This sorts them.
        # NOTE: remove if chapter titles get normalized in the future.
        self.requirements = sorted(self.requirements, key = lambda req:self.sort_helper(req["ID"]))
                   

    def sort_helper(self,req_id):
        """ Helps with requirement id sorting (see comment above) """
        req_id = req_id.split(".")
        req_id = [int(i) for i in req_id]
        return tuple(req_id)

    def to_json(self):
        """ Returns a JSON-formatted string """
        return json.dumps(self.requirements)

    def to_xml(self):
        ''' Returns XML '''
        xml = '<requirements>'

        for r in self.requirements:
            xml += "<requirement ID='{}' L1='{}' L2='{}' L3='{}'>{}</requirement>\n".format(r['ID'], int(r['L1']), int(r['L2']), int(r['L3']), escape(r['Description']))
        
        xml += '</requirements>'
        return xml

    def to_csv(self):
        ''' Returns CSV '''
        si = StringIO()

        writer = csv.DictWriter(si, ['ID', 'Description', 'L1', 'L2', 'L3'], extrasaction='ignore')
        writer.writeheader()
        writer.writerows(self.requirements)

        return si.getvalue()

def main():
    test = ISVS("en")
    print(test.to_xml())

if __name__ == '__main__':
    main()
