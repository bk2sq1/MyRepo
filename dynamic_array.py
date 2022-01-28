#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class dynarr:
    def __init__(self):
        self.lst=[0]*8
        self.top=0
        self.len=0
        print("Default constructor array is : ",self.lst)
    def dpush(self,num):
        if(self.len==len(self.lst)):
            lst2=[0]*(self.len*2)
            for i in range (self.len):
                lst2[i]=self.lst[i]
            self.lst=lst2
            self.lst[self.len]=num
            self.len+=1
            print("Dynamic increase done. New array is : ",self.lst)
        else:
            self.lst[self.len]=num
            self.len+=1
    def dpop(self):
        print("Current length is : ",self.len)
        self.lst[self.len-1]=0
        self.len-=1
        if(self.len==int(len(self.lst)/4)):
            print("Current length is : ",self.len)
            lst2=[0]*(self.len*2)
            for i in range(len(lst2)):
                lst2[i]=self.lst[i]
            self.lst=lst2
            #self.len-=1
            print("Dynamic reduction done. New array is : ",self.lst)
            
    def dshow(self):
        print(self.lst)

darr=dynarr()
darr.dpush(1)
darr.dpush(2)
darr.dpush(3)
darr.dpush(4)
darr.dpush(5)
darr.dpush(6)
darr.dpush(7)
darr.dpush(8)
print("Default size was 8. Currently array has reached limit. Array is : ",darr.lst)
darr.dpush(9)
darr.dpop()
darr.dpop()
darr.dpop()
darr.dpop()
darr.dpop()
darr.dpop()
darr.dpop()
darr.dpop()


            

