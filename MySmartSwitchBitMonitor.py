number = int(input("Enter a number: "))

print("\nBinary Value:", bin(number))

count = 0
temp = number

while temp > 0:
    count += temp & 1
    temp >>= 1

print("Total ON Switches:", count)

print("\nSwitch Status:")
for i in range(8):
    mask = 1 << i

    if number & mask:
        print("Switch", i, ": ON")
    else:
        print("Switch", i, ": OFF")