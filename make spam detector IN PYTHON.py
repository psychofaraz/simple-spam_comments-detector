text = input("Enter The Text: \n")

if("make money hear" in text):
	spam = True
elif("buy now" in text):
	spam = True
elif("click this" in text):
	spam = True
elif("subscribe this" in text):
	spam = True
elif("faraz" in text):
		spam = True
elif("join now" in text):
			spam = True
elif("faraz khan pathan" in text):
	spame = True
else:
	spam = False
if(spam):
						print("THIS TEXT IS SPAM")
else:
		print("THIS TEXT IS NOT SPAM")