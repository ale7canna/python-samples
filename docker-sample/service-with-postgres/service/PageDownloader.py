import requests
import string

class PageDownloader:
    def getPage(self, url):
        self.page = requests.get(url).text

    def getCambiaValuteValue(self):
        pattern = 'Tasso di cambio CHF/EUR <span id="chf_rate">'
        start = str.find(self.page, pattern) + len(pattern)
        self.page = self.page[start:]

        end = str.find(self.page, '</span>')
        self.page = self.page[:end]
        return float(self.page)

    def getXeChangePage(self):
        pattern = "<span class=\'uccResultAmount\'>"
        start = str.find(self.page, pattern) + len(pattern)
        self.page = self.page[start:]

        end = str.find(self.page, "</span>")
        self.page = self.page[:end]
        return float(self.page.replace(',', '.'))
