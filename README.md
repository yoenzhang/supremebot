Working SupremeBot unless otherwise stated. (Current Date: Jan 15, 2020)

Preliminary Notes:
- YOU MUST USE google chrome! (for this current version)
- MAC OS ONLY (for this current version)

As a personal project, since I have always been into clothing and fashion but did not have the money to buy a bot, thus, I decided to make my own. Furthermore, with how unsecure most public bots are, I intended this bought to be installed and used locally, therefore neither me nor anyone else should have access to your private information and accounts.

This project soon evolved into more than just a passion project, as I had a friend come to me asking me to make it intuitive for someone who has no coding experience whatsoever. Thus, I created a front end UI using tkinter, with the backend being run through both beautifulsoup4 and Selenium. I found beautifulsoup4 had a more elegant approach to scraping the individual items, specifically finding and storing data from a website. I used Selenium as it provided the fastest output after being given user input, sending data stored from beautifulsoup4.

How To Use The Bot?

Download all the project files and store them in a location you will have easy access to (eg. Downloads folder).
Make sure you have python3 installed, you can check this by going to your terminal and entering "which python3".
If "usr/bin/python" appears, you do not have python3 installed. Go to https://www.python.org/downloads/ and make sure you download the latest version of python (currently python3).
After installing python3, run the following commands in your terminal:
1) "pip3 install Selenium"
2) "pip3 install requests"
3) "pip3 install bs4"

Go to the three dots in the top right of chrome, press Help -> About Google Chrome. Find the version of chrome that you're using and download the corresponding Chrome Driver at: http://chromedriver.chromium.org/downloads. Move the unzipped file into this project folder.

Next, you want to find where you installed the project files and find the project folder extension, (ex. /User/Downloads/supremeBot/)
Open terminal and type "cd {INSERT YOUR PROJECT FOLDER EXTENSION HERE}" to enter that directory.
Finally, when you want to run the bot, in your terminal enter the following command: "python3 supremebot.py"

A UI should popup, with 4 tabs labelled "Home", "Cart", "Settings", and "Run Bot". Make sure to read each instruction from each tab and run the bot when you are ready! Have fun shopping!

Future Improvements:
1) Captcha Bypass
2) Make cross platform support (Windows/Linux)
3) Potentially faster scripts through other languages (C++, C, etc)
