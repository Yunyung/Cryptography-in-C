# -*- coding: utf-8 -*-
def keyword_examination(keyword):
    if (len(keyword) > 25):
        print("keyword length cann't bigger than 25!")
        return False
    else:
        isRepeat, ch = isContainRepeatedChar(keyword)
        if (isRepeat):
            print("The character " + ch + " is repeat!")
            return False
    return True

def isContainRepeatedChar(k_str):
    dic = {}   # Create empty dict
    # Traverse each characters in string 
    # in lower case order 
    for ch in k_str:
        # If character is already present 
        # in dict, return char
        if ch in dic:
            return True, ch
        else:
            dic[ch] = 1
    return False, '\0'
        
def build_playfair_matrix(keyword):
    Matrix = []
    for i in keyword.lower():
        Matrix.append(i)
        
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    
    for i in alphabet:
        if i not in Matrix:
            Matrix.append(i)
    
    # break to two dimension array 5*5
    keyMatrix = []
    for i in range(5):
        keyMatrix.append('')
    
    keyMatrix[0] = Matrix[0:5]
    keyMatrix[1] = Matrix[5:10]
    keyMatrix[2] = Matrix[10:15]
    keyMatrix[3] = Matrix[15:20]
    keyMatrix[4] = Matrix[20:25]
    return keyMatrix
    
def find_position_in_keyMatrix(keyMatrix, m):
    if m == 'j':
        m = 'i'
    x = y = 0
    for i in range(5):
        for j in range(5):
            if keyMatrix[i][j] == m:
               x = i
               y = j
    return x, y

def E_traslateOriginMessage(originMessage):
    message = []
    
    for m in originMessage:
        message.append(m)
    
    #Delet space    
    for unused in range(len(originMessage)):
        if " " in message:
            message.remove(" ")
            

    #If both letters are the same, add an 'x' after the first letter.
    for i in range(int(len(message) / 2)):   # 只需要執行 floor(m / 2)次一定剛好完成
        if message[2 * i] == message[2 * i + 1]:
            message.insert(2 * i + 1, 'x')
    
    #If message len is odd, add an "x" at the end
    if len(message) % 2 == 1:
        message.append("x")
    
    return message

def encryption(keyword, message):
    print("\n.............encrypting..........")
    keyMatrix = build_playfair_matrix(keyword)
    newMessage = E_traslateOriginMessage(message.lower())

    cipher = []
    for i in range(int(len(newMessage) / 2)):
        m1_x, m1_y = find_position_in_keyMatrix(keyMatrix, newMessage[2 * i])
        m2_x, m2_y = find_position_in_keyMatrix(keyMatrix, newMessage[(2 * i) + 1])
        if m1_x == m2_x:
            # same row
            cipher.append(keyMatrix[m1_x][(m1_y + 1) % 5])
            cipher.append(keyMatrix[m1_x][(m2_y + 1) % 5])
        elif m1_y == m2_y:
            # same column
            cipher.append(keyMatrix[(m1_x + 1) % 5][m1_y])
            cipher.append(keyMatrix[(m2_x + 1) % 5][m1_y])
        else:
            # diff row and column
            cipher.append(keyMatrix[m1_x][m2_y])
            cipher.append(keyMatrix[m2_x][m1_y])
    return cipher
          
def decryption(keyword, ciphertext):
    print("\n............decrypt............")
    keyMatrix = build_playfair_matrix(keyword)
    plaintext = []
    
    for i in range(int(len(ciphertext) / 2)):
        m1_x, m1_y = find_position_in_keyMatrix(keyMatrix, ciphertext[2 * i])
        m2_x, m2_y = find_position_in_keyMatrix(keyMatrix, ciphertext[(2 * i) + 1])
        if m1_x == m2_x:
            # same row
            plaintext.append(keyMatrix[m1_x][(m1_y - 1) % 5])
            plaintext.append(keyMatrix[m1_x][(m2_y - 1) % 5])
        elif m1_y == m2_y:
            # same column
            plaintext.append(keyMatrix[(m1_x - 1) % 5][m1_y])
            plaintext.append(keyMatrix[(m2_x - 1) % 5][m1_y])
        else:
            # diff row and column
            plaintext.append(keyMatrix[m1_x][m2_y])
            plaintext.append(keyMatrix[m2_x][m1_y])
    
    
    count_x = 0
    # 刪掉多餘的x, 先檢查x在哪,再檢查此x前後是否一樣  
    for i in range(1, int(len(plaintext) - 1), 1): #檢查index 1 ~ n-2是否為x
        if (plaintext[i] == 'x'):
            if (plaintext[i - 1] == plaintext[i + 1]):
                count_x = count_x + 1
    for i in range(count_x):
        plaintext.remove('x')
    
    
    # 刪掉最尾端的x  
    if plaintext[len(plaintext) - 1] == 'x':
        plaintext.pop()
    return plaintext
    
    
    

# 功能選擇
user_select_function = input("function list: [1]encryption, [2]decryption : ")
# 輸入keyword
keyword = input("Enter your keyword : ")
while (not keyword_examination(keyword)):
    print("The keyword is wrong format")
    keyword = input("Reenter your keyword : ")

# 讀取檔案
file_name = input("Input your file name(ex->p1.txt) : ")
with open(file_name) as file_Obj:
    message = file_Obj.read()

# 加密
if (user_select_function == "1"):
    cipher = encryption(keyword, message)
    cipher_string = ''.join(cipher)  # 串列轉成string
    print("Ciphertext -> " + cipher_string)

    # 將 cipher 寫入檔案
    fn = 'c1.txt'
    with open(fn, 'w') as file_Obj:
        file_Obj.write(cipher_string)
    print("Already write ciphertext to 'c1.txt' file!")
# 解密 
elif (user_select_function == "2"):
    plaintext = decryption(keyword, message)
    plaintext_string = ''.join(plaintext)  # 串列轉成string
    print("plaintext -> " + plaintext_string)
    
    # 將 plaintext 寫入檔案
    fn = 'p.txt'
    with open(fn, 'w') as file_Obj:
        file_Obj.write(plaintext_string)
    print("Already write ciphertext to 'plaintext.txt' file!")
    
