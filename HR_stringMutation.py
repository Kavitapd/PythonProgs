def mutate_string(string, position, character):
    list_ch=list(string)
    if position<= len(list_ch):
        list_ch[position]=character
    string=''.join(list_ch)
    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    new_str= mutate_string(s, int(i), c)
    print(new_str)