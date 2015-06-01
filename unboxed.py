#!/Users/Naman/miniconda/bin/python

# importing standard modules
import re, inspect, os, sys,pdb;

# some boiler plate code.
poing = inspect.getabsfile(inspect.currentframe());
ee = execfile;
selfdir = os.path.dirname(poing);
os.chdir(selfdir);

from collections import Counter
import requests

class GitHubAccount(object):

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

	def getFavLanguage(self):

		if self.name == None or len(self.reposJson) == 0:
			return None

		languageList = []
		repos = self.getRepos()

		for repo in repos:
			language = repo.getLanguage()
			if language != None:
				languageList.append(language)	

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

	def __init__(self, jsonRepo):
		self.repo = jsonRepo
		self.name = self.repo['name']
		self.language = self.repo['language']

	def getName(self):
		return self.name

	def getLanguage(self):
		return self.language

	def __str__(self):
		return "Name: " + self.name + " | Language: " + str(self.language)

	def __repr__(self):
		return "Name: " + self.name + " | Language: " + str(self.language)

