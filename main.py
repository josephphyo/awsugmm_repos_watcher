import requests 

response = requests.get("https://api.github.com/orgs/awsugmm/repos")
#print(response.json()[0])
my_repos = response.json()

for repo in my_repos:
    print("Repo Name: {}\nRepo URL: {}\n".format(repo["name"],repo["url"]))