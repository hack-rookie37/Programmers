s = 'abcabcabcabcdededededede'

answer = []

for size in range(1, len(s) // 2 + 1): # 문자열 총 길이의 절반까지 잘라가며 체크
    compressed = ''
    temp = s[:size]
    count = 1
    
    for j in range(size, len(s), size):
        if temp == s[j:size + j]: # temp에 담긴 문자열과 동일하면 count +1
            count += 1
        else:
            if count != 1: # 압축된 것이 존재하므로 압축된 결과 compressed에 넣음
                compressed += str(count) + temp
            else: # 압축된 것이 없으므로 그대로 넣음
                compressed += temp
            
            temp = s[j:size + j]
            count = 1
    
    if count != 1: # 남아있는 문자열 처리
        compressed = compressed + str(count) + temp
    else:
        compressed = compressed + temp
    
    answer.append(len(compressed))
        

print(min(answer))