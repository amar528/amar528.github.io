from math import degrees, atan

ab = int(input())
bc = int(input())
mbc = round(degrees(atan(ab / bc)))
print(f'{mbc}{chr(176)}')
