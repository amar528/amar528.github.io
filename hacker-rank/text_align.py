import sys

# Replace all ______ with rjust, ljust or center.

thickness = int(input())  # This must be an odd number

if (not 0 < thickness < 50) or (thickness % 2 == 0):
    print(f'Invalid value for thickness: {thickness}')
    sys.exit(1)

c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).center(thickness - 1) + c + (c * i).center(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).ljust(thickness * 2) + (c * thickness).rjust(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).ljust(thickness * 2) + (c * thickness).rjust(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).ljust(thickness) + c + (c * (thickness - i - 1)).rjust(thickness)).center(
        thickness * 6))
