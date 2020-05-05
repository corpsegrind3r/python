# playing around with a list of snowboards

snowboards = ['Burton', 'K2 Praying Mantis', 'Never Summer Proto Type Two', 'Lib Tech Orca']				# my snowboards

print("MY SNOWBOARDS\n")
for snowboard in snowboards:
	print(snowboard)

print("The last board I bought is a " + snowboards[-1])
print("My first snowboard was a " + snowboards[0].title())

snowboards.append('Lib Tech Orca')			# I'd like to add a longer Orca
snowboards.insert(2,'Rossignal Templar')	# I forgot about this forgettable board
del snowboards[2]							# Let's forget about that Rossignal
snowboards.remove('Burton')					# No longer in my possession

print("Cool",snowboards[1])