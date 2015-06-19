#!/usr/bin/python

# importing standard modules
import re, inspect, os, sys, pdb;
from collections import Counter
import requests

class GitHubAccount(object):
	"""
	This class represents a GitHub Account.
	It has 3 main methods.
	1. getName - Returns the name of the account holder
	2. getRepos - Returns a list of repos as Repo class objects.
	3. getFavLanguage - Returns the most used language of the account holder
	"""

	def __init__(self,name):
		response = requests.get("https://api.github.com/users/"+name+"/repos").json()

		if type(response) == dict:
			self.name = None
			self.reposJson = None
		else:
			self.name = name
			self.reposJson = response

		self.repos = None

	def getName(self):
		return self.name

	def getRepos(self):
		# user does not exist or user has no repos.
		if self.name == None or len(self.reposJson) == 0:
			return None

		if self.repos == None:
			repoList = []
			for repo in self.reposJson:
				temp = GitHubRepo(repo)
				repoList.append(temp)

			self.repos = repoList
			return repoList
		else:
			return self.repos

	def getFavLanguage(self,ignoreforked):

		if self.name == None or len(self.reposJson) == 0:
			return None

		repos = self.getRepos()

		if ignoreforked:
			languageList = [repo.language for repo in repos if not repo.forked and repo.language != None ]
		else:
			languageList = [repo.language for repo in repos if repo.language != None ]

		doesExist = Counter(languageList).most_common(1)

		if len(doesExist) == 0:
			return None
		else:
			return doesExist[0][0]

	def __str__(self):
		return "< Account holder: "+str(self.name)+" >"

	def __repr__(self):
		return "< Account holder: "+str(self.name)+" >"

class GitHubRepo(object):
	"""
	This class represents a GitHub repository.
	It has 2 main methods.
	1. getName - Returns the name of the repository.
	1. getLanguage - Returns the name of the main language.
	"""

	def __init__(self, jsonRepo):
		self.repo = jsonRepo
		self.name = self.repo['name']
		self.language = self.repo['language']
		self.forked = self.repo['fork']

	def getName(self):
		return self.name

	def getLanguage(self):
		return self.language

	def __str__(self):
		return "< Name: %s | Language: %s | Forked: %s >" % ( self.name, self.language, self.forked)

	def __repr__(self):
		return "< Name: %s | Language: %s | Forked: %s >" % ( self.name, self.language, self.forked)
