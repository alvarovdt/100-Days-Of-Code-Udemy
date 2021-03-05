import requests
from bs4 import BeautifulSoup

URL = "https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h1", class_="list-item__title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

index = 1
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{index}) {movie}\n")
        index=index+1