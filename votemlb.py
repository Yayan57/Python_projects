# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
import webbrowser


website = "https://www.mlb.com/all-mlb/ballot"
votes = ["Freddie Freeman", "Jose Altuve", "Jeremy Pena", "Alex Bregman", "Wilson Contreras", "Yordan Alvarez", "Kyle Tucker",
        "George Springer", "Mike Trout", "Sandy Alcantara", "Christian Javier", "Framber Valdez", "Justin Verlander","Shohei Ohtani", "Ryan Pressly", "Edwin Diaz" ]
form = ["adriangarza115@yahoo.com", "77038"]

driver = webdriver.Chrome()
driver.get(website)
button = driver.find_element_by_id('Google Search')
button.click()

"""
list
open website
make votes
click review picks button
fill out form
   email
   birth date drop down boxes
   zipcode
   Country drop down box
   favorite team drop down box
   click mlb newsletter box
   click i am not a robot
   submit vote

"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

