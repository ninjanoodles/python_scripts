from sys import argv

script, user_name = argv 
prompt = '> '

print "Hi %, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you me %?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about like me.
You live in %r. Not sure where that is.
And you a %r computer. Nice.
""" % (likes, lives computer)