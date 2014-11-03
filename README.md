LED-blaster
================

Driving LED with step time and cie1931.

Requires the <a href="https://github.com/sarfata/pi-blaster">pi-blaster daemon</a>.

Install the pi-blaster daemon - (<a href="https://github.com/sarfata/pi-blaster#how-to-build-and-install">instructions</a>).

Usable pins:

      GPIO number   Pin in P1 header
          4              P1-7
          17             P1-11
          18             P1-12
          21             P1-13 (only for model A/B)
          27             P1-13 (only for model B+)
          22             P1-15
          23             P1-16
          24             P1-18
          25             P1-22


Usage: python ledblaster.py "<gpio> <time(s)> <from(0-100)> <to(0-100)>"

For greater fluency this script uses 1000(max) steps for pi-blaster. The resulting total time in seconds is equal to ((steps*10)-1)*time.
