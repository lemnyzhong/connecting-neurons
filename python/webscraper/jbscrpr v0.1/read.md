# JbScrpr v0.1

### A terminal program that scrapes **seek.com** and displays the latest job roles and their employers.

> Firstly, big shouts out to the giants' whose shoulders I stand on:
> ```python
>    import requests
>    from bs4 import BeautifulSoup
>    import webbrowser
>    import os
>    import time
> ```
> for making my life easier.

### Overview of what happens:
> JbScrpr v0.1 is designed to receive user input to perform certain actions such as `scrape`, `print`, `open`, `path` and `quit` (more to be added).
>
> Firstly, user will select `scrape` to load a scraper object with jobs and employers.
> - The program will ask for `keywords` to enter as a search filter, the keywords for types of jobs should be entered in the following style:
>```
>   for example to search for software internship:
>   
>       software-internship-
>
>   The "-" inbetween and at the end of the keywords must be added, otherwise page will return 404 error.
>
>   Note to self:
>   Future versions should screen for 404 and return a error statement.
>```
> - The program will then request for an area keywork to add as a search filter, the keywords for types of areas should be entered in the following style:
>```
>   for example to search for jobs in Sydney:
>   
>       Sydney
>
>   for example to search for jobs in all of NSW:
>
>       All-Sydney-NSW
>```
> - Once these important keywords are established, the program will join the keywords into a `search path` string (web address) and run a `request.get()` with the the `search path` as the parameter.
>
>    