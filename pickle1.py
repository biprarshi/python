import pickle

ex={1:"6",2:"3",3:"A"}                                         #dictionary

p = open("Niit.txt","wb")
pickle.dump(ex,p)
p.close()

                                                            # wb:data write mode
                                                            # rb:data load mode

#DATA LOAD:
f = open("Niit.txt","rb")
a = pickle.load(f)
print(a)