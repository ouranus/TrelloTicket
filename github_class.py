from __future__ import print_function
from pprint import pprint
from github import Github
import os

def main():
	g = Github("b3114722a808b3ddffd8e79a8167d4da6ffe66dd ")
	for repo in g.get_user().get_repos():
	    pprint(repo.name)

if __name__ == '__main__':
	main()