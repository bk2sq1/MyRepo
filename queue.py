#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:03:31 2022

@author: aaronvijayan
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class aq:
    def __init__(self,x):
            self.lst=[None]*x
            self.push_index=0
            self.length=0
            self.top=0
            self.max=x
    def push(self,num):
        if(self.length==self.max):
            print("List if full")
        else:
            self.length+=1
            self.lst[self.push_index]=num
            self.push_index=int((self.push_index+1)%self.max)
    def popq(self):
        if(self.length==0):
            print("Queue is empty")
        else:
            self.lst[self.top]=None
            self.length-=1
            self.top=int((self.top+1)%self.max)
    def dispq(self):
        if(self.length==0):
            print("Queue is empty")
        else:
            print("You queue is: ")
            for i in range (self.length):
                print(self.lst[((self.top+i)%self.max)])
st=aq(10)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.dispq()
st.push(5)
st.push(6)
st.popq()
st.popq()
st.popq()
st.popq()
st.push(20)
st.dispq()

        