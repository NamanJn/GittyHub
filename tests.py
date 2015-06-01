#!/usr/bin/python

import unittest2 
from unboxed import GitHubAccount, GitHubRepo

class UserExists(unittest2.TestCase):

	def testUserDoesNotExist(self):
		user = GitHubAccount("usernamedoesnotexist")
		self.assertEqual(None,user.getName())

class UserExistsButNoRepos(unittest2.TestCase):

	def testUserWithNoRepos(self):
		user = GitHubAccount("animal")
		self.assertEqual("animal",user.getName())
		self.assertEqual(None,user.getRepos())

	def testUserWithRepos(self):
		user = GitHubAccount("NamanJn")
		self.assertEqual("NamanJn",user.getName())
		self.assertEqual(6, len(user.getRepos()) )

	def testUserWithReposButNoFavLanguage(self):
		user = GitHubAccount("Naman")
		self.assertEqual("Naman", user.getName() )
		self.assertEqual(1, len(user.getRepos()) )
		self.assertEqual(None, user.getFavLanguage() )

	def testUserNotExistsAndNoFavLanguage(self):
		user = GitHubAccount("usernamedoesnotexist")
		self.assertEqual(None, user.getName() )
		self.assertEqual(None, user.getFavLanguage() )

	def testUserWithFavLanguage(self):
		user = GitHubAccount("usernamedoesnotexist")
		self.assertEqual(None, user.getName() )
		self.assertEqual(None, user.getFavLanguage() )

unittest2.main()

