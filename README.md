# portal-shitter
A complex script that combines brute forcing and scraping into one script which streamlines obtaining every possible combination of username and password for the Okaloosa County Parent Portal website. Since the website has no further protection of any kind, ironically all passwords are the last for digits of the username, it is relatively easy to crack. The only downside is the speed of their website, a request can only be sent around every half second and processes around the same time but with multithreading located in something.py we can thread multiple processes at once. With the method I have used I specify each thread to run 1 million combinations so that 7 threads can together brute force 7 million combinations in 1/7th of the time!

## Results
All the results of the script go to the assets/matches.txt file. This file will be created if no file is found along with the parent directory

## Output
All the output from the script such as status, errors, and any other console text will output to the console. This can be changed easily by setting the settings.conf file in the main directory.

## settings.conf
This has not yet been implemented
