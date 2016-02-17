score=0
message = "I have %s questions correct"
print('1. How many points is a touchdown?')
print" "
print('a. 7')
print('b. 6')
print('c. 3')
print('d. 8')
print" "
a = raw_input('Enter your choice: ')
if a == 'b' or a == '6':
    print('Correct!!')
    score = score+1     
    print(message%score)
    
else:
    print('Nope! Try again!')
    print(message%score)
       
print('2. How long is a football field?')
print" "
print('a. 75 yards')
print('b. 100 yards')
print('c. 120 yards')
print('d. 360 yards')
print" "
b = raw_input('Enter your choice:') 
if b == 'c':
    print('Correct!!')
    score = score+1  
    print(message%score)
    
else:
    print"Nope! Try again!"
    print(message%score)
    	
    
print"3. Who throws the ball?"
print" "
print"a. Running back"
print"b. Quarterback"
print"c. Wide Recivier"
print"d. Linebacker"
print" "
c = raw_input("Enter your choice:")
if c == "b":
    print"Correct!!"
    score = score+1  
    print(message%score)
    
else:
    print"Nope! Try again!"
    print(message%score)
    
print"4. What counts as 2 points?"
print" "
print"a. Safety"
print"b. Field goal"
print"c. Extra point"
print"d. Touchdown"
print" "
d = raw_input('Enter your choice: ')
if d == 'a':
    print('Correct!!')
    score = score+1  
    print(message%score)
    
    
else:
    print('Nope! Try again!')
    print(message%score)
    
print('5. What team plays in Dallas?')
print" "
print('a. Texans')
print('b. Bills')
print('c. Saints')
print('d. Cowboys')
print" "
e = raw_input('Enter your choice: ')
if e == 'd':
    print('Correct!!')
    score = score+1  
    print(message%score)
    if score == 5:
    	print"YAY!:)"
else:
    print('Nope! Try again!')
    print(message%score)