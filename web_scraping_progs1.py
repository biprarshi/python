# Beautiful Soup is a Python package for parsing HTML and XML
# documents (including having malformed markup, i.e. non-closed
# tags, so named after tag soup). It creates a parse tree for
# parsed pages that can be used to extract data from HTML,
#  which is useful for web scraping.

#  INSTALL->"pip install bs4 requests"

#  -> 1. Folder  (BeautifulShoup)-> code .-> (Enter)-> Vscode
#  -> Html Data required.
#  ->right click view page source
#  -> BeautifulShoup ->bs4 docs->"www.crummy.com"
# go to site -> bs4 docs crummy.com

from bs4 import BeautifulSoup

with open("sample1.html", "r") as f1:
    html_doc1 = f1.read()

# print(html_doc1)
soup1 = BeautifulSoup(html_doc1, 'html.parser')
print(soup1.prettify())
print('='*10)
# print(soup1.title)
# print(soup1.title, type(soup1.title))
# print(soup1.title.string, type(soup1.title.string)) # own object of bs4   <class 'bs4.element.NavigableString'>
# print(soup1.div)
# print(soup1.find_all("div"), type(soup1.find_all("div")))
# print(soup1.find_all("div"))
# print(soup1.find_all("div")[0], type(soup1.find_all("div")[0]))

# for link1 in soup1.find_all("a"):
#     print(link1.get("href"))
#     print(link1.get_text())
# print(type(link1))

# link3 = soup1.find(id="link3")
# print(link3, link3.get("id"), link3.get("href"),
#       link3.get("tamata"), link3.get_text(), sep="\n")

# print(soup1.select("div.italic"))
# print(soup1.select("span#italic"))
# print(soup1.span.get("class"))
# print(soup1.div.get("class"))

# print(soup1.find(id="italic"))
# print(soup1.find(class_="italic")) #class is reserved key word(italic_)
# print(soup1.find_all(class_="italic"))

# for child1 in soup1.find(class_="container").children:
#     print(child1)
# for child1 in soup1.find(contenteditable="false").children:
#     print(child1)

# print("$$$$$$$$$$$$$$$$$$$$$$$moshe################################")
# # PARENT
# i = 0
# for parent1 in soup1.find(class_="box").parent:
#     i = i+1
#     x = parent1
#     print(parent1)
#     if i == 2:
#         # print(i)
#         break

# print(type(x))
# print(soup1.find(class_="box").parent.parent)
# print(soup1.find(class_="box").parent.parent.name)

# Note:Beautiful Soup builds its own object by the data provided by the object(html_docs)

# count1 = soup1.find(class_="container")
# print(count1)
# count1.name = "span"
# count1["class"] = "myclass"
# count1["class"] = "myclass class2"
# count1.string = "My name is Jarvis"
# print(count1)

# # Modification:  To create a file with modification
# ulTag1 = soup1.new_tag("ul")
# liTag1 = soup1.new_tag("li")
# liTag1.string = "\nHome sweet home\n"
# ulTag1.append(liTag1)
# liTag1 = soup1.new_tag("li")
# liTag1.string = "\nTell me about yourself\n"
# ulTag1.append(liTag1)
# soup1.html.body.insert(0, ulTag1)
# with open("sample1_modified1.html", "w") as f:
#     f.write(str(soup1))

# # Finding the Attribute:
# count1 = soup1.find(class_="container")
# print(count1.has_attr("class"))
# print(count1.has_attr("contenteditable"))


# def has_class_not_id1(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")
# results1 = soup1.find_all(has_class_not_id1)
# print(results1)
# for r1 in results1:
#     print(r1, "\n\n")

# def has_content1(tag):
#     return tag.has_attr("content")
# results1 = soup1.find_all(has_content1)
# print(results1)
# for r1 in results1:
#     print(r1)
