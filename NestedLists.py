if __name__ == '__main__':
    l = []
    # mins= float('inf')
    # seclow=0
    ans=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        newlist= []
        newlist.append(name)
        newlist.append(score)
        l.append(newlist)
        # if mins>score:
        #     seclow= mins
        #     mins= score
        #     # print(seclow)
        ans.append(score)
        
    ans.sort()
    
    seclow= ans[0] #min element
    
    for i in ans:
        if(i!=seclow):
            seclow=i
            break

    ans=[]
    
    for i in l:
        if(i[1]==seclow):
            ans.append(i[0])
            # print(i[0])
    ans.sort()
    for i in ans:
        print(i)
        
        