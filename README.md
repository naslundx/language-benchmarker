# language-benchmarker
Tool for benchmarking equivalent implementations accross different programming languages.

Implemented in *Python 3* and available under *GPL3 license*. Currently only works on Debian/Ubuntu Linux derivatives.

## How to run
Clone this repo and run `python3 benchmarker.py`.
If you are missing any of the languages on your system, run `sudo ./install_languages.sh`, which will download and setup the runtimes for all supported systems on your machine. Languages already installed will be ignored.

## What it does
At the moment, the language benchmarker runs each test case in each language a fixed number of times, measures the average execution time, and prints them to the console. Upcoming features are:

- Measure average CPU load, min/avg/max RAM usage, I/O usage
- Print to log
- Create good-looking HTML/Markdown reports

## How to contribute
Take a look at the *issues* of this repo to contribute to the core product. Mostly, this project is in need of experts in each respective language who can do the best possible implementations for each language.

Make a fork of this repo and do a pull request, comment and changes are gladly discussed! If you find something you believe is incorrect, create an issue,

## Algorithms implemented
(table of algorithms and languages)
... ... ...

## Expected results
(results on different hardware/OS)
... ... ...
