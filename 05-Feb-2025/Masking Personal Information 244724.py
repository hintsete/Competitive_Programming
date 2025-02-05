# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        # if s is a string
        if "@" in s:
            
            name,domain=s.lower().split("@")
            # print(name[0])
            # for ch in name[0]:
            masked_name=""
            
            masked_name=name[0]+"*****"+name[-1]
            masked_email=masked_name+"@"+domain
                
            return masked_email
        
        masked_pno=[ch for ch in s if ch.isdigit() ]
        masked_pno="".join(masked_pno)
        last_four=masked_pno[-4:]
        masked=""
        if len(masked_pno)==10:
            return "***-***-"+last_four

        elif len(masked_pno)==11:
            return "+*-***-***-"+last_four

        elif len(masked_pno)==12:
            return "+**-***-***-"+last_four
        elif len(masked_pno)==13:
            return "+***-***-***-"+last_four