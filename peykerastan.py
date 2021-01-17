#"Peyke Rastan" Group
#"Fanavard" competition
#99/10/28
#"basteh bandy behine" program
#-----------------------------------------
n= int (input('n=number of objects'))
m= int (input('m=number of boxes'))
k= int (input('k=size of boxes'))

osize=[]                                 #object size
for j in range(1,n+1):
 print('enter the sizes of',j,'th object')
 a=int(input())

 #-------------------------------------- for omitting invalid objects
 while a>k or a<=0:                         
        print('This size of objects is invalid (between 1 and box size)')
        print('enter the sizes of',j,'th object')
        a=int(input())

 osize.append(a)                        #Put objects size in one list

#---------------------------------------Packing obj
obj=n-1
for i in range(1,m+1):                  #Checking the number of required boxes
 space=k                                #New box
 
 for x in range(obj,-1,-1):             #Check packing from the last object
   
   if space-osize[x]>=0:                #Checking the empty space in every box
     space=space-osize[x]               #Calculating the empty space in every box
     obj=obj-1                          #The number of remaining objects
    
   else:
       break                            #There is no space, go to the next box
#---------------------------------------output=The most packed objects
output=n-1-obj                          
print('For initial values:','n=',n,'m=',m,'k=',k)
print('The number of packed objects=',output)

input('Press enter to exit')

