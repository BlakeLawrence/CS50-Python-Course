# ask user for their name
name = input("whats your name? ")

# say hello to user using concatenation
print("hello, " + name)

# say hello to user using simple comma (this method creates a space automatically)
print("hello,",name)

# say hello to user using an f string (format string)
print(f"hello, {name}")

# we can clear white space on a string using the strip method. C;ears white space on left and right of variable.
print("strip:","hello,",name.strip())

# capitilize string
print("capitilize:","hello,",name.capitalize())

# capitilize using title (same as a boom or movie title)
print("title:","hello,",name.title())

# strip and title using chaining
print("chaining:","hello,",name.strip().title())

# for cleaner code, add string methods to the input to minimize lines of code
friend = input("Whats your best friends name and surname?").strip().title()

# printing user input
print(f"your best friend is {friend}")

# we can use split method like javascript to split a string into an array of characters or words.
# print array of 2 words made of suers name
print(name.split(" "))
# store first name and second name into variables and print firstName
firstName, lastName = name.split(" ")
print(f"you rock {firstName}")