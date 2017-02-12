## (Personal project) webauto

Automate web page using selenium webdriver and Python

### Author
* Quinn Song


### Python
* 2.7

### Tools
* Selenium 3.0.2
* Firebug 2.0.18
* FirePath 0.9.7.1.1 By Pierre Tholence
* Python unittest

### Website
* [This awesome website](http://way2automation.com) is designed for Testing Selenium / QTP scripts

### Test Cases:
* Simple one: Open up the page, and then quit :)
* Fun one: Follow the "Alert" at the bottom:
   1. Open up the url -> Assert the page title
   2. WebDriverWait (timeout: 10s) until Alert link clickable;
   3. Sleep 5s for new tab window;
   4. Switch to new window;
   5. Assert new window title;
   6. Sleep 5s for new alert pop up;
   7. Assert alert pop up;
   8. Assert alert text "REGISTRATION FORM"
   9. Fill out Registration Form:
   10. Once registratin successful, try the login using username/password


### 2017.02.12