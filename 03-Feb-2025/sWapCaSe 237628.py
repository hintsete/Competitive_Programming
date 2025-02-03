# Problem: sWapCaSe - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    res=""
    for ch in s:
        if ch.isupper():
            ch= ch.lower()
            res+=ch
        else:
            ch= ch.upper()
            res+=ch
    return res

if __name__ == '__main__':