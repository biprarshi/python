import requests

url1 = "https://timesofindia.indiatimes.com/india/delhi"

# TEXT
# reqs1 = requests.get(url1)
# print(reqs1.text)

#  To save in file :
# def fetch_n_save1(url2, path1):
#     reqs1 = requests.get(url2)
#     with open(path1, "w") as fobj1:
#         fobj1.write(reqs1.text)
#         print(reqs1.text)
# fetch_n_save1(url1, "download_tatar.html")

# JSON
reqs1 = requests.get(url1)
print(reqs1.json)
