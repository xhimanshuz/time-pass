from sys import argv
source, name = argv
promt = '> '
print("Hi, %s Welcome" % name)
print("So, Do you do like this?")
like=raw_input(promt)
print("Where do you live?")
live=raw_input(promt)
print("Which Vechile do you prefer?");
vechile=raw_input(promt)
print("What's your age?")
age=int(raw_input(promt))
likes = {"yes":"Do","no":"Don't"}
print(""" This File name is %r 
 Your name is %r and you %r Like this fucking game
 You living out in %r and You Drive %r just you prove
 You are still fucking %d old Virgin have nothing to do!
""" %(source, name, likes[like], live, vechile, age))
