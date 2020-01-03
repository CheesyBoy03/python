s = str(input('Entered string: '))
def solution(s):
    if s == '':
        s = []
        print(s)
    else:
        s_list = [s[i:i + 2] for i in range(0, len(s), 2)]
        if len(s)%2 == 1:
            last = s_list[-1]
            l = last + '_'
            s_list.pop(-1)
            s_list.append(l)
            
        print(s_list)
solution(s)
