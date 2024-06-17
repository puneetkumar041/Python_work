favourite_language='python '
print(favourite_language+'and SQL')
favourite_language.rstrip()
print(favourite_language.rstrip()+'and SQL')

name=" albert einstein "
message=name.title().strip() + ' was a smart man.'
print(message)

nostarch_url='https://nostrach.com'
print(nostarch_url.removeprefix('https://'))

text='JJohn'
print(text.removeprefix('J'))


text='filename.txt'
print(text.removesuffix('.txt'))