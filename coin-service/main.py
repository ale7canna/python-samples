#!/bin/python

from PageDownloader import PageDownloader
import time
from datetime import datetime
import os.path

def do_work():
    with open("result/values.csv", "a") as f:
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

        line = f""""{a}";"{b}";"{c}";"{d}";"{e}";\n"""
        f.write(line)

def pre_checks():
    if (not os.path.exists("result/values.csv")):
        with open("result/values.csv", "w") as f:

            a = "Giorno e ora"
            b = "CambiaValute"
            c = "Xe Change"
            d = "Difference"
            e = "Diff Percentage"

            line = f""""{a}";"{b}";"{c}";"{d}";"{e}";\n"""
            f.write(line)

if __name__ == "__main__":
    print ("Daemon starts with his work...")
    pre_checks()
    while True:
        do_work()
        time.sleep(60)
