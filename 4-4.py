str = input()
count = 0

strArray = []

# 문자열 숫자와 무자 분리
for i in range(0, len(str)):
    if int(ord(str[i])) < 58:
        #숫자
        count += int(str[i])
    else:
        #영어
        strArray.append(str[i])

print(count, strArray)

strSize = []

index = 0


# while index == len(strArray):
#     i = 0
#     for i in range(1, len(strArray)):
#         if i == 1:
#             strSize.append(strArray[0])
#         if int(ord(strSize[index])) >= int(ord(strArray[i])):
#             strSize.insert(0, strArray[index])
#             index += 1
        

for i in range(1, len(strArray)):
    if i == 1:
        strSize.append(strArray[0])
        print(strSize)
    index = 0        
    check = True
    while check:
        print(ord(strSize[index]) >= ord(strArray[i]), ord(strSize[index]) ,ord(strArray[i]) + 1, ord('E'), ord('B') ,strSize[index], strArray[i])
        if ord(strSize[index]) >= ord(strArray[i]):
             strSize.insert(index, strArray[i])
             print('성공', strSize)
             check = False
        else:
            if index >= len(strSize) - 1:
                strSize.append(strArray[i])
            print(strSize[index], strArray[i],'index + 1 = ', index)
            index += 1
            

print(strSize, count)

# lists = ['a']

# for i in range (0, len(lists)):
#     lists.append('a')
#     print(lists)
#     if i == 10:
#         break