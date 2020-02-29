from __future__ import print_function
from pprint import pprint
from github import Github
import os

def main():
	# First create a Github instance:
	# using username and password
	g = Github("g-gibosky", "Systr@setop2019")

	# or using an access token
	g = Github("access_token")

	# Github Enterprise with custom hostname
	g = Github(base_url="https://github.com/g-gibosky/Trello-Ticket/api/v3", login_or_token="access_token")

	pprint(g)

	# Then play with your Github objects:
	for repo in g.get_user().get_repos():
	    pprint(repo.name)

if __name__ == '__main__':
	main()