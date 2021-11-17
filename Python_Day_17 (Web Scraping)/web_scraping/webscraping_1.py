from bs4 import BeautifulSoup
# import requests
# import lxml


with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)

# print(soup.prettify())

# print(soup.a)
# print(soup.p)

# print(soup.select('p'))

# print(soup.find_all(name='a'))
# print(soup.find_all(name='p'))

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.get("class"))
# print(section_heading.getText())
# print(section_heading.name)
print(soup.select(".heading"))

