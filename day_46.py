# Create a DataFrame
import pandas as pd

data = [
    [2009, "Brothers", "Drama"],
    [2002, "Spider-Man", "Sci-Fi"],
    [2009, "WatchMen", "Drama"],
    [2010, "Inception", "Sci-Fi"],
    [2009, "Avatar", "Fantasy"],
]

df_movies = pd.DataFrame(data, columns=["Year", "Title", "Genre"])
print(df_movies)


# Extra Challenge: Website Data with Pandas
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(URL)
# print(response.status_code) # confirm 200, OK

# table content in <table class="wikitable">
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("table", {"class": "wikitable"})
# print(result)

df_python = pd.read_html(str(result)) # returns a list of 1 element
df_python = pd.DataFrame(df_python[0])
df_python = df_python[["Type", "Mutability"]] # clean up the table
print(df_python)
