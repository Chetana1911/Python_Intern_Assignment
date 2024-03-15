# Python_Intern_Assignment

# ✔ Requirements
1. Python 3.12.2
2. pip install pymongo==4.6.2 - MongoDB Python Driver
3. MongoDB 7.0 - Database Server
4. (Optional)MongoDB Compass 1.16.3 - To view database

# ✨ Here are some steps for scraping data from books web pages using BeautifulSoup in Python:
1. Import the libraries : pip install beautifulsoup4 & pip install urllib3
2. Read the HTML link using urllib
3. Parse the link using BeautifulSoup
4. Extract the tag that contains all the products of the webpage

# ✨ Scraping and Inserting to DB
1. With the Json data all the required data is stored into Dictionary format.
2. Extracted all the course data using loops and stored as list.
3. Mongodb Altas is used as DB here, with pymongo library mongodb is connected to python.
4. Database and collections created via python and the list of dictionaries is uploaded using collection.insert_many method.
5. Created an app.py to initialize
6. Python_Intern_Assignment/README.md at main · Adarsh7697/Python_Intern_Assignment 
