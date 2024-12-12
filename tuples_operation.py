number = [25,14,56,48,39,50]

fruits = ['Mango','Apple','Grapes','Banana']

#print(len(fruits))

x = ("apples","banana","cherry")
y = list(x)
y.append("orange")
thistuple = tuple(y)
#print(thistuple)

x = ("apples","banana","cherry")
y = list(x)
y[1] = 'kiwi'
x = tuple(y)

#print(x)

nums = (45,25,14,(56,48,39),21,34,50,35)

#print(nums[3][1])

print(nums[4:7])
