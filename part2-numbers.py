# calculator
# unnecessary z variable - longer way
# x = input("Whats X?")
# y = input("Whats Y?")
# z = int(x)+int(y)
# print(z)

# gets rid oz z variable - cleaner way
# x = int(input("Whats X?"))
# y = int(input("Whats Y?"))
# print(x+y)

# float - number with a decimal (allows decimals, int will not)
# x = float(input("Whats X?"))
# y = float(input("Whats Y?"))
# print(x+y)

# round will round up or down
# print(round(1.4)) #1
# print(round(1.5)) #2

# number formatting - f string (format)
x = int(input("Whats X?"))
y = int(input("Whats Y?"))
z = x+y
print(f"{z:,}")