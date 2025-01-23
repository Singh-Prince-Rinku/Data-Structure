import time

start = time.time()

for i in range(1, 1000):
    print(f'{i} i love python ')
    
    
    
# for measuring time that taken by loop to print 1000 Executed 
Measure = time.time() - start
print(f"The time is taken by this program is {Measure} \n")

    
while i<1000:
    print(f'{i} i love python ')
    i+=1
    
print(f"The time is taken by this program is {Measure}")