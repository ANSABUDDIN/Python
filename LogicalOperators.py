# # 0 0
# print(0 & 0)
# print(0 | 0)
# print(0 ^ 0)

# # 0 1

# print(0 & 1)
# print(0 | 1)
# print(0 ^ 1)

# # 1 0

# print(1 & 0)
# print(1 | 0)
# print(1 ^ 0)

# # 1  1

# print(1 & 1)
# print(1 | 1)
# print(0 ^ 1)

Persentage = int(input("Enter The Persentage: -  "))

if Persentage >= 60:
    print(Persentage,"%" " First Division")
elif Persentage >= 48:
    print(Persentage,"%" " Second Division")
elif Persentage >= 35:
    print(Persentage,"%" " Third Division")
else:
    print(Persentage,"%", " Need To Work Hard")
