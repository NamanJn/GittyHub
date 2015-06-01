#!/Users/Naman/miniconda/bin/python

# importing standard modules
import re, inspect, os, sys;

# some boiler plate code.
poing = inspect.getabsfile(inspect.currentframe());
ee = execfile;
selfdir = os.path.dirname(poing);
os.chdir(selfdir);

from unboxed import GitHubAccount, GitHubRepo

if len(sys.argv) <= 1:
	        print "Please enter a username as an argument."
		sys.exit()

GitHubName = sys.argv[1]

a = GitHubAccount(GitHubName)

if a.getName() == None:
	print "Username does not exist"

elif a.getRepos() == None:
	print "User does not have any repos."

elif a.getFavLanguage() == None:
	print "User has no favourite language."
	
else:
	print "Favourite language is " + a.getFavLanguage()

sys.exit()

