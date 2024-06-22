# Teachers class progs and notes

from bs4 import BeautifulSoup

with open("sample1.html", "r") as f:
    html_doc = f.read()
# print(html_doc)
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)
# print(soup.prettify())
# print(soup.title)
# print(soup.title,type(soup.title))
# print(soup.title.string,type(soup.title.string)) # own object of bs4
# print(soup.div)
# print(soup.find_all("div")[1])   # use index
# print(type(soup.find_all("div")[1]))

# for link in soup.find_all("a"):
#     print(link.get("href"))
#     print(link.get_text())


# s=soup.find(id="link3")
# print(s)


s = soup.find(id="link3")
# print(s.get("href"))
# print(soup.select("div.italic"))
# print(soup.select("span#italic"))
# print(soup.span.get("class"))

# print(soup.find(id="italic"))
# print(soup.find(class_="italic")) #class is reserved key word(italic_)

# print(soup.find_all(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)


# PARENT

# i=0
# for parent in soup.find(class_="box").parent:
#     i +=1
#     print(parent)
#     # if(i==2):
#     #     break


# Note:Beautiful Soup builds its own object by the data provided by the
# object(html_docs)

count = soup.find(class_="container")
# print(count)

# count.name="span"
# print(count)

# count["class"]="myclass"
# count["class "]="myclass class2"
# print(count)

count.string = "My name is Jarvice"
print(count)

# Modification:  To create a file with modification

ulTag = soup.new_tag("ul")

liTag = soup.new_tag("li")
liTag.string = "\n Home sweet home \n"
ulTag.append(liTag)

liTag = soup.new_tag("li")
liTag.string = "\n tell me About your self \n"
ulTag.append(liTag)

soup.html.body.insert(0, ulTag)
with open("modified30.html", "w") as f:
    f.write(str(soup))


# Finding the Attribute:

# count=soup.find(class_="container")
# print(count.has_attr("class"))       #id/class
# print(count.has_attr("contenteditable"))


# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")
# results=soup.find_all(has_class_but_not_id)
# print(results)

# for result in results:
# print(result,"\n\n")

# def has_content(tag):
#     return tag.has_attr("content")
# results=soup.find_all(has_content)               # finding the content
# # print(results)
# for result in results:
#     print(result,"\n\n")
