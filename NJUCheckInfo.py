#coding: utf-8
import http.client
from html.parser import HTMLParser

def checkNum(stdNo):
    conn = http.client.HTTPConnection('114.212.253.8:8080')
    conn.request('GET', 'http://114.212.253.8:8080/SportWeb/gym/gymExercise/gymExercise_query_result_2.jsp?xh=%d' % (stdNo))
    r1 = conn.getresponse()
    s = r1.read().decode("utf-8")
    parser = getCheckTime()
    parser.feed(s)
    liOut = parser.close()
    if stdNo == 131190003: print(liOut)
    return liOut

class getCheckTime(HTMLParser):

    liCheckTime = []
    thisCheck = []

    inTD = False
    beginData = False
    realData = False

    def __init__(self):
        HTMLParser.__init__(self)
        self.liCheckTime = []
        self.thisCheck = []

    def handle_starttag(self, tag, attrs):
        #if tag == "tr":
        #    print(attrs)
        if tag == "tr" and (('bgcolor', '#FFFFFF') in attrs or ('bgcolor', '#F1F6FE') in attrs):
            #print(attrs)
            self.realData = True
        if tag == "tr" and (('bgcolor', '#FFFFFF') in attrs or ('bgcolor', '#F1F6FE') in attrs) == False:
            self.realData = False
        if tag == "td" and self.beginData:
            self.inTD = True
    def handle_endtag(self, tag):
        #if tag == "tr":
            #print(str(self.realData) + str(len(self.thisCheck)))
        if tag == "form" and self.realData and len(self.thisCheck) != 0:
            self.liCheckTime.append(tuple(self.thisCheck))
            self.thisCheck = []
        if tag == "td":
            self.inTD = False
    def handle_data(self, data):
        if data == "备注":
            self.beginData = True
        if self.inTD == True:
            self.thisCheck.append(data.strip())
    
    def close(self):
        HTMLParser.close(self)
        return self.liCheckTime

for i in range(131190001, 131190150):
    print("%d - %d" % (i, len(checkNum(i))))
