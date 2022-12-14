import json
import requests

def getRepoCommits(userID):
    out = {}
    response = requests.get("https://api.github.com/users/" + userID + "/repos", timeout=5)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        for repo in json_data:
            repo_name = repo.get("name")
            commit_response = requests.get("https://api.github.com/repos/" + userID + "/" + repo_name + "/commits", timeout=5)
            if commit_response.status_code == 200:
                commit_data = json.loads(commit_response.text)
                out[repo_name] = len(commit_data)
    return out
