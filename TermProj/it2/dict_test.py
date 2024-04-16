wbook = {'title': 'Paradise Lost', 'author': 'John Milton', 'date': 1674}
print(type(book))
print(book['title'])
print(book['author'])
print(book['date'])

print(book.get('title')) # does the same thing as print(book[title])

print(book.get('author'))

print(book.get('date'))


print(book.get('cover_art', 'Key not found, please try again')) #ovewrite what happens when an input is sent

book['title'] = 'Great Gatsby'

book['cover art'] = "blue guy wearing glasses"

print(book['title'])
print(book['cover art'])
print(book)

print(book.keys()) # prints keys
print(book.values()) #print values assocaited with those keys

for i in book.values():#way to print out all values in a dicitonary
    print(i)

book.update({'title': 'Les Miserables', 'author': 'Victor Hugo', 'date': 1862}) #update multiple values at once win a dictionary

print(book)

book = {'title': 'Paradise Lost', 'author': 'John Milton', 'date': 1674, 'title': 'Harry Potter'} #if we overload the the 'title' ID with a second dictioonary definition, it will take te latest submission
print(book)


print(book.items()) #print all items within a dictionary

book = {1: 'Paradise Lost', 2: 'John Milton', 3: 1862} #dictionary doesn't just have to have the keys as strings 
print(book)

book = {True: 'Paradise Lost',  True: 'monkey', False: 'John Milton', 3: 1862} # it could also use booleans
print(book[True]) #prints paradise lost