﻿# dashboard-slide

## A simple way to slide through multiple URLs

I use to create dashboards to our company and recently felt a need to automate navigation through different **Observability** dashboard tools, like Dynatrace, Grafana, PowerBI, Splunk, Kibana, etc...
Some of them asks for authentication, so I wrote a little function to make it too.
I chose Python because it's easy. Selenium is supported, and it's a fantastic framework to manipulate browsers for test and it has all that I need!
My OS nowadays is Windows 10/11 and the browser is Google Chrome, you'll have to adjust the code if your setup is different.

### how to run
download last version of [ChromeDriver](https://chromedriver.chromium.org/downloads) and put it on PATH system environment variable.
I have created some others system environment variables to my users/passwords. Maybe you don't need it.
```
pip install selenium
```
Edit the `urls` dict inside **dashboard.py** with your own URL, adjust the time to wait in constants and _voilà_!

That's it, I hope this helps someone someday.

--
WeeBee, 2023-09-14
