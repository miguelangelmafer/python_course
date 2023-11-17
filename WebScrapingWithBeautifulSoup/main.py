import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.encoding = "utf-8"

all_html = response.text
soup = BeautifulSoup(all_html, "html.parser")
all_films = soup.findAll(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_films]

reverse_movie_titles = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for film in reverse_movie_titles:
        file.write(f"{film}\n")
