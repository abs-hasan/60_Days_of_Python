from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
res =  requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

movies_100 = soup.find_all(name = "h3", class_="title")


movie_titles = [movie.getText() for movie in movies_100]

#to reverse
movies = movie_titles[::-1]
# for n in range(len(movie_titles) - 1, -1, -1):
#     print(movie_titles[n])

with open("movie.txt", mode = "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")