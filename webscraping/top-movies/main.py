import json
import requests
from bs4 import BeautifulSoup


url = "https://www.empireonline.com/movies/features/best-movies-2/"

soup = BeautifulSoup(requests.get(url).content, "html.parser")
data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])

# with open("soupjson.json", "w") as f:
#     f.write(json.dumps(data, indent=4))


def find_articles(data):
    if isinstance(data, dict):
        for k, v in data.items():
            if k.startswith("ImageMeta:"):
                yield v["titleText"]
            else:
                yield from find_articles(v)
    elif isinstance(data, list):
        for i in data:
            yield from find_articles(i)

with open("top movies.txt", "w") as f:
    for a in find_articles(data):
        f.write(f"{a}\n")



























# articles = soup.find_all(name="a", class_="titlelink")

# titles = [title.text for title in articles]
# urls = [url.get("href") for url in articles]
# votes = [int(vote.text.split(" ")[0]) if vote != "" else 0 for vote in soup.find_all(name="span", class_="score")]


# dict = [{'article': title, 'url': url, 'votes': vote} for title,url,vote in zip(titles,urls,votes)]

# # highest = 0
# # for each in dict:
# #     if int(each["votes"]) > highest:
# #         highest = int(each["votes"])
# #         top_article = each
# # print(top_article)
# # 
# largest_num = max((votes))
# index = votes.index(largest_num)
# # print(titles[index], urls[index], votes[index],votes[0])     
# print(titles[0], urls[0], votes[0])
# print(len(titles), len(urls), len(votes))
# print(votes)








# with open("website.html", encoding='utf-8', errors='ignore') as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all(name="a")

# anchor_tags_text = [tag.getText() for tag in all_anchor_tags]
# anchor_urls = [tag.get("href") for tag in all_anchor_tags]
# print(anchor_tags_text, anchor_urls)


# heading = soup.find(name="h1", id="name").string
# print(heading)

# section_heading = soup.find(name="h3", class_="heading").text
# print(section_heading)

# company_url = soup.select_one(selector="p em a")
# print(company_url)