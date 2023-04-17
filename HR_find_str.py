#s=input()
#sub_s=input()

def count_substring(s, sub_s):
    count=0
    subStrPosition = -1
    for i in range(0,len(s)):
        if i > subStrPosition:
            subStrPosition = s.find(sub_s, i , len(s))
            if subStrPosition > 0:
                count+=1   
    
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    