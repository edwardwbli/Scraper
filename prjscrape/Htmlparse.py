def search (self, queryStr):
    queryStry = urllib2.quote(queryStr)
    url = 'https://www.google.com.tw/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=%s' % queryStry
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    result = self.extractSearchResults(html)

search('ROSI')
