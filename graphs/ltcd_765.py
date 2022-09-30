'''
LeetCode - problem 765
'''

    def minSwapsCouples(self, row):
        x=row
        indecies={x[i]:i for i in range(len(x))}
        swap=0

        for i in range (0,len(x),2):
            a=x[i]
            b=x[i+1]
            if ((a%2==0 and b==a+1)or (b%2==0 and a==b+1)):
                continue
            if a%2==0:
                target=a+1
            else:
                target=a-1
            target_index=indecies[target]
            b_index=i+1

            x[target_index],x[b_index]= x[b_index],x[target_index]
            indecies[target]=b_index
            indecies[b]=target_index

            swap +=1
        return (swap)
