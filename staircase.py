# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:16:21 2020

@author: SRIKAR REDDDY
"""
 
def num_ways_x_bottom_up(n,x):
    if n==0:return 1
    nums=[0]*(n+1)
    nums[0]=1
    for i in range(1,(n+1)):
        total=0
        for j in x:
            if i-j>=0:
                total+=nums[i-j]
        nums[i]=total
    return nums[n]
    

if __name__ == '__main__':
    n = int(input("Enter the total Steps"))
    x=[]
    m=int(input("Enter the number steps to take:"))
    for i in range(0,m):
        print("Steps to take at a time")
        ele=int(input())
        x.append(ele)
    nof=num_ways_x_bottom_up(n,x)
    print("Number of way {}".format(nof))