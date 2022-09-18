comment=input("Ebter:")
if("money make fast " in comment):
    spam= True
elif("subscribe now"in comment):
    spam= True
elif("click here"in comment):
    spam= True
elif("buy now"in comment):
    spam= True       
else:
    spam= False
if(spam):
    print("this is spam")
else:
    print("no spam")    