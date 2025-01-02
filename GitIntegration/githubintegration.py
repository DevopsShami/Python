# Get pull request Information report using Python . 

# Use Request Model, Import this model
# API , Url to make acces the github api request,
# JSON -> Dictionory, Python cant read this 
# Print the required things.

# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

# URL to fetch pull requests from the GitHub API
url = f"https://api.github.com/repos/kubernetes/kubernetes/pulls"

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url)

# Only if the response in successfull 

if response.status_code == 200:
    pull_requests = response.json()

# Create empty dictionary to store the pull request data and their count 

pr_creators = {}


# Iterate through each pull request and extract the creators name 
for pull in pull_requests:
    creators = pull['user']['login']
    if creators  in pr_creators:
        pr_creators[creators] += 1
    else:
     pr_creators[creators] = 1 

#  # Display the dictionary of PR creators and their counts
print("PR Creators and the count ")

for creator,count in pr_creators.items():
   print(f"{creator}:{count} PR(s)")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")