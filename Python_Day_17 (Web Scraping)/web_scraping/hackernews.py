from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

# print(soup.select(".title"))

# get the first article title

article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
print(article_text)
# print(article_upvote)

# For all
# articles = soup.find_all(name="a", class_="titlelink")
# article_texts = []
# article_links = []
#
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(article_links)
#
#
# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# largest_number = max(article_upvote)
# largest_index = article_upvote.index(largest_number)
# print(article_texts[largest_index])
# print(article_links[largest_index])
#
# # print(article_texts)
# # print(article_links)
# # print(article_upvote)

