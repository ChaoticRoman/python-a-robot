# Vizualizace spolehlivosti

Máte k dispozici datový soubor [data.txt](data.txt) (i skript [generate_data.py](generate_data.py),
který tato data vygeneroval. Tato data tvoří sekvence dvojic
* čas v [ISO 8601 formátu](https://en.wikipedia.org/wiki/ISO_8601) a
* 0 nebo 1 symbolizující nějaký sledovaný systém funkční (1) nebo nefunkční (0).

Vaším úkolem je vizualizovat procentuální "uptime" jak v celém měsící, tak v jednotlivých dnech.

Program by neměl dezinformovat a měl by i indikovat zda pro daný den nejsou data dostupná,
či 100 % nebo 0 % pochází z jediného vzorku pro daný den.

Možné zdroje inspirace:
* https://matplotlib.org/examples/pylab_examples/plotfile_demo.html
* https://matplotlib.org/examples/pylab_examples/bar_stacked.html


