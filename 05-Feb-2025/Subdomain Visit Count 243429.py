# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_dict=defaultdict(int)
        for domains in cpdomains:
            domain=domains.split()
            print(domain)
            domain_items=domain[1].split(".")
            n=len(domain_items)
            print(domain_items)
            rep=domain[0]
            for i in range(n):
                
                subdomain=".".join(domain_items[i:n])
                print(subdomain)
            
                my_dict[subdomain]+=int(rep)
            
        print(my_dict)
        output=[]
        for key,value in my_dict.items():
            output.append(str(str(value) +" "+ key))
        return output

        