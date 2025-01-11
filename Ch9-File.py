# # Open the file in read mode
f = open("this.txt", "r")
# # Read its contents
text = f.read()
# # Print its conten
print(text)

s=open("this.txt","a")
t=s.write("\nYou can do it!!")
print(t)