#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class aq:
    def __init__(self,x):
            self.lst=[None]*x
            self.push_index=0 ##this counter will 
                              ##revert to 0 when it becomes self.max 
            self.length=0 ##this will track 
                            ##total number of elements in the Q.
            self.top=0 ##this is the front-most element of the Queue.
            self.max=x ##this will be used 
                        ##to track remainder iterations
    def push(self,num):
        if(self.length==self.max):
            print("You tried to push " + str(num) + " but Queue is full\n")
        else:
            self.length+=1
            self.lst[self.push_index]=num
            self.push_index=int((self.push_index+1)%self.max)
            ##remainder sets push_index to 0 when you reach self.max
    def popq(self):
        if(self.length==0):
            print("Queue is empty\n")
        else:
            self.lst[self.top]=None
            self.length-=1
            self.top=int((self.top+1)%self.max) 
            ###remainder easily sets top to 0 once you reach self.max
    def dispq(self):
        if(self.length==0):
            print("Queue is empty\n")
        else:
            print("Your queue is: \n")
            for i in range (self.length):
                print(self.lst[((self.top+i)%self.max)])
                ##since we begin with top+0, we get top as first element
                
st=aq(7) ## taking 7 as max_size for this example
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(6)
st.push(20)
st.push(31) ##trying to push after 7 pushes
st.popq()
st.popq()
st.popq()
st.popq()
st.popq()
st.popq()
st.popq()
st.popq() ##trying to pop after 7 pops (7 is max size here)
st.push(6)
st.push(5)
st.push(4)
st.push(3)
st.push(2)
st.push(1)
st.dispq()

        
