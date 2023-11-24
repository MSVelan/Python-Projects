from bs4 import BeautifulSoup
import requests, os

response = requests.get("https://www.timeout.com/film/best-movies-of-all-time")
movieWebsite = response.text

soup = BeautifulSoup(movieWebsite, "html.parser")

allMovies = soup.find_all(name="h3", class_="_h3_cuogz_1")
headings = [a.getText(strip=True) for a in allMovies]

headings = headings[:100]

dirName = os.path.dirname(__file__)
fileName = os.path.join(dirName, "allMovies.txt")
with open(fileName,"+w") as file:
    for i in headings:
        file.write(i)
        file.write("\n")