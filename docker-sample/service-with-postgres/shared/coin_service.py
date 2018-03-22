#!/bin/python

from shared.PageDownloader import PageDownloader
from datetime import datetime

class CoinService:
    def get_change(self):

        pd = PageDownloader()
        pd.getPage("https://cambiavalute.ch/?accepted=true")
        cvv = pd.getCambiaValuteValue()

        pd.getPage("http://www.xe.com/it/currencyconverter/convert/?From=CHF&To=EUR")
        xev = pd.getXeChangePage()

        diff = xev - cvv;
        diffPerc = 100 * diff / xev;

        a = datetime.now().isoformat(timespec="seconds")
        b = cvv
        c = xev
        d = diff
        e = diffPerc
        return (a, b, c, d, e)

