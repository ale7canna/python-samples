import module as asd
from PageDownloader import PageDownloader

if __name__ == "__main__":
    t = asd.myadd(1, 2, 3)
    print (t)

    pd = PageDownloader()
    pd.getPage("https://cambiavalute.ch/?accepted=true")
    print (pd.getCambiaValuteValue())

    pd.getPage("http://www.xe.com/it/currencyconverter/convert/?From=CHF&To=EUR")
    print (pd.getXeChangePage())
