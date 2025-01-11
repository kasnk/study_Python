marks=[]

print("Enter number of marks:")
n=int(input())
for _ in range(n):
    marks.append(int(input()))
marks.sort()
print(marks)