# Dont-close-kiosk-site
Year 2015, beginning in the development world, another simple script that was solved quick and easy.

- [Dont-close-kiosk-site](#dont-close-kiosk-site)
- [Problem description](#problem-description)
- [Restrictions](#restrictions)
- [Solution](#solution)

# Problem description
There was a situation with some computers equipment that worked as information access points.
- The computer equipment had Windows 7
- The information system ran in Google Chrome
- The organization did not want to spend money on software to encapsulate the information system.
As a note, it was difficult to navigate to another site since it was programmed as a single page application and navigating to another site used to be *almost* impossible.

# Restrictions
The Google Chrome browser had to be always in "kiosk" mode (more [here](https://superuser.com/questions/716426/running-latest-chrome-for-windows-in-kiosk-mode)), it is not allowed to use another application, than web browser with the internal information site.

# Solution
A batch file which starts with the os system, and monitored that the browser always it's open. Also the script file kills the explorer process to avoid the open of another application by the user.
