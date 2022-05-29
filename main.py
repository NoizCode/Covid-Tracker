from bs4 import BeautifulSoup
import requests
import os
import platform

if platform.system() == "Windows":
    clear = "cls"

clear = "clear"

total_deaths = []
countries = []
cases = []
new_cases = []
cases_per_country = {}

os.system("clear")
def chooseMode():
    print("\033[4mCovid Tracker!\033[0m")
    
    while True:
        mode = int(input("Choose mode: show_all(1), Search_Country(2), Quit(3)" ))
        if mode == 1 or mode == 2 or mode == 3:
            break
        else:
            print("Invalid Mode...")
    if mode == 1:
        os.system(clear)
        show_all()
    elif mode == 2:
        os.system(clear)
        search()

def get_case():
    global country_name, countries, cases
    global all_cases
    global cases_per_country

    html_text = requests.get("https://www.worldometers.info/coronavirus/").text
    soup = BeautifulSoup(html_text, "lxml")
    table = soup.find("table", id="main_table_countries_today") 
    table_body = table.find("tbody") 
    
    rows = table_body.find_all("tr")
    for row in rows:
        cols = row.find_all('td')
        for col in cols:
            if col.find("a", class_="mt_a") in col:
                country_name = col.find("a", class_="mt_a").text
                countries.append(country_name)
                continue
        
        for td in row.find_all("td")[2]:
            all_cases = td.text
            cases.append(all_cases)
            continue
        
        # Currently not working properly

        #for col1 in row.find_all("td")[4]:
            #all_deaths = col1.text
            #total_deaths.append(all_deaths)

def create_dict():
    global countries, cases, cases_per_country

    for i in range(len(countries)):
        cases_per_country[countries[i]] = cases[i]    

    return cases_per_country

def search():
    country = input("Search by country: ")
    
    if(country[0].islower()):
        country = country.capitalize()

    for key,value in cases_per_country.items():
        if key == country:
            print(f"\n{key} : {value}")
            print("\n")

    chooseMode()
            
def show_all():
    for key,value in cases_per_country.items():
        print( key, ":", value)
        dash = len(key) + len(value)
        print("-" * (dash + 3))
    print("\n")
    chooseMode()

get_case()
create_dict()
chooseMode()
