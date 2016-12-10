from sys import argv 

script, username = argv
prompt = '>'

print "Hi %r I'm the %r script." %(username, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % username
likes = raw_input(prompt)

print "Where do you live %s?" %username
lives = raw_input(prompt)

print "What kind of comeputer do you have?"
comeputer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live is %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, comeputer)