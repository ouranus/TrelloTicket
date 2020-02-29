from __future__ import print_function
from pprint import pprint
from github import Github
import os

def main():
	# First create a Github instance:
	# using username and password
	g = Github("ouranus", "balada66")

	# or using an access token
	g = Github("ac44d1f39fea30e606dce90b3532ce6102a7e470")

	# Github Enterprise with custom hostname
	g = Github(base_url="https://github.com/ouranus/TrelloTicket/api/v3", login_or_token="username")

	# Then play with your Github objects:
	for repo in g.get_user().get_repos():
	    pprint(repo.name)

if __name__ == '__main__':
	main()