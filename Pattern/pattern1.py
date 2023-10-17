#  ****
#  ****
#  ****
#  ****


# 		No. of rows?? --> N = 4
# 		No. of columns in ith row?? --> N
# 		what to print?? --> *
N = int(input("Enter number of rows for the square pattern : "))

# for iterator_var in sequence:
#     statements(s)

for i in range(0, N):  # 0 se N-1 tak chalega
    # print(i)
    for j in range(0, N):
        print("*", end="")
    print("\r")  # next line after each row
