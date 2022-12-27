BDSM Checklist
==============

https://bdsmchecklist.github.io/checklist/simple.html

How to modify
-------------

Edit the HTML template in [templates/checklist.html](templates/checklist.html), the CSS in [global.css](global.css), and the Javascript in [logic.js](logic.js). The [Makefile](Makefile) will run [make_html.py](make_html.py) to create static HTML files in [build/](build/). The Python code has the list of activities in it.

To build the static HTML run
```
make
```
To push the built HTML to gh-pages run
```
make commit
```
