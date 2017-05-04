word = str(raw_input("Please Enter a word: "))
if len(word)>0 and word.isaplha():
	Original = word.lower()
	#print Original
	First_letter = Original[0]
	#print First_letter
	L = len(Original)
	#print L
	Slice = Original[1:len(Original)]
		#print Slice
		Capital = Slice[0].upper()
		Slice = Slice[1:len(Slice)]
		New_word = Capital + Slice + First_letter + "pyg"
		print New_word
	else:
		print "Please Try again"
