#concatenate

name="Eric"
print("Hello "+name+", would you like to learn some Python today?”")


#name case
name="eric"
print(name.lower())
print(name.upper())
print(name.title())

#famous quote
name="albert einstein"
print(name.title()+' once said, “A person who never made a mistake never tried anything new.”')


#famous quote with variable
message=name.title()+' once said, “A person who never made a mistake never tried anything new.”'
print(message)

#famous quote with variable and whitespace
name=" albert einstein "
message=name.title().strip() + ' once said, “A person who never made a mistake never tried anything new.”'
print(message)


name ="Eric"
message='Hello,'+name.title()+' would you like to learn some Python today?”'
print(message)
print(name.lower())
print(name.upper())

print("Languages:\n\tJava\n\tC++")


filename='python_notes.txt'
print(filename.removesuffix('.txt'))


