import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
resp = requests.get(URL)
contents = resp.text
soup = BeautifulSoup(contents, "html.parser")
movies = soup.find_all(name="h3", class_="title")


movie_titles = [movie.getText() for movie in movies]
movie_titles.reverse()
# print(movie_titles)

with open("movies.txt", "a+") as file:
    for movie in movie_titles:
        file.write(movie + "\n")