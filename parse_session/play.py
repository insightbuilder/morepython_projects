import time

print("This is a for loop")

print("****************")
print("Give me number of iteration: ")
itr = int(input())

for idx in range(itr):
    if idx % 2 == 0:
        print("***         ****")
    else:
        print("++++     +++++++")
    time.sleep(1)
print("****************")
