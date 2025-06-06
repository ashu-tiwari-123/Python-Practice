a="ashu"
b='ashu'
c='''ashu'''
d="""ashu"""

#length of string
print(len(a))

#slicing
slice1 = a[1:3]
print(slice1)

#negative indexing
slice2 = a[-3:-1]
print(slice2)
slice3 = a[-1:-3]
print(slice3)  # This will return an empty string because the start index is greater than the end index in negative slicing