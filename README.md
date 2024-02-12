# STUDY TRACKER
#### Video Demo: https://youtu.be/rXsXW6QR0dI
#### Description:
##### The project
My final project is a web-based study tracker that keeps track of the time you spent studying (or actually whatever you want to keep track time), so at the end of the day you will know if you studied much, or wasted time doing other things, and also have the records of all your study sessions.
##### Explaining the project pages: Index
On the index page, there is the website title, then you'll see a table tag containing a stopwatch with its title on top named "session time", the time counter in the middle, and three options on the bottom, those are: start to start counting time, pause to pause the count, and stop do reset the stopwatch and save its value.
Below this table tab there is a resume of the time you spent studying on the current day, in hours, minutes and seconds, if you have more than one daily session the these values are going to sum and update each time you start and stop your stopwatch.
Finally on the bottom of the page there's a table tag containing your study records! This table contain two columns, date and time, which are going to show up all study sessions duration and the day that it happened related to the logged in account. In case that the user loads the index page and they're not logged in they're going to be redirected to the login page.
##### Explaining the project pages: Login
The login page is simple and contains a form with a login input, a password input and a "log in" button, below it there's a "Do not have an account?" link which will redirect the user to the register page.
##### Explaining the project pages: Register
The register page is very similar to the login page, with the addition of one more input to verify the password so you can register safely. There's also a "Already have an account?" link that redirects the user to the login page.
##### The project folders and files
The project folder contains a folder called static which contains a styles.css file for all the html pages, below this folder there's a "templates" folder which contains 4 files: index.html, login.html, register.html, that were introducted before, and a layout.html so the other html files can be better designed and optimized.
Outside of these two folders there are only two more files on the project folder, app.py that contains all the code to make everything work, and a database named save.db that contains three sql tables, the first one is named users and stores the users id, username and password hash, the second is a sqlite_sequence table, and the third one is named users_saves and stores the users id, time (the study session time explainined in the description beginning) and day (day when study session happened).
