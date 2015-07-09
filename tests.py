#!/usr/bin/python

import unittest2
from mainClass import GitHubAccount, GitHubRepo

class GitHubTest(unittest2.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.usernames = ['animal',
				'FriedSock',
				'NamanJn',
				'usernamedoesnotexist',
				'Naman']

		cls.userAccounts = {}
		for user in cls.usernames:
			cls.userAccounts[user] = GitHubAccount(user)

	def testUserDoesNotExist(self):
		user = self.userAccounts["usernamedoesnotexist"]
		self.assertEqual(None,user.getName() )

	def testUserWithNoRepos(self):
		user = self.userAccounts["animal"]
		self.assertEqual("animal",user.getName() )
		self.assertEqual(None,user.getRepos() )

	def testUserWithRepos(self):
		user = self.userAccounts["NamanJn"]
		self.assertEqual("NamanJn",user.getName() )
		self.assertEqual(4, len(user.getRepos()) )

	def testUserWithReposButNoFavLanguage(self):
		user = self.userAccounts["Naman"]
		self.assertEqual("Naman", user.getName() )
		self.assertEqual(1, len(user.getRepos()) )
		self.assertEqual(None, user.getFavLanguage() )

	def testUserNotExistsAndNoFavLanguage(self):
		user = self.userAccounts["usernamedoesnotexist"]
		self.assertEqual(None, user.getName() )
		self.assertEqual(None, user.getFavLanguage() )

	def testUserWithFavLanguage(self):
		user = self.userAccounts["FriedSock"]
		self.assertEqual("FriedSock", user.getName() )
		self.assertEqual("Clojure", user.getFavLanguage() )

	def testUserWithFavLanguageIgnoreForked(self):
		user = self.userAccounts["FriedSock"]
		self.assertEqual("FriedSock", user.getName() )
		self.assertEqual("Ruby", user.getFavLanguage(ignoreforked=True) )

	def testUserWithFavLanguage(self):
		user = self.userAccounts["FriedSock"]
		self.assertEqual("FriedSock", user.getName() )
		self.assertEqual("Ruby", user.getFavLanguage() )

	@classmethod
	def tearDownClass(cls):
		pass
unittest2.main()
