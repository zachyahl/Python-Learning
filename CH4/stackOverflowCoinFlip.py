numberOfStreaks = 0
flip = []
H_streak = 0 #counters
T_streak = 0

for _ in range(20):
    
    if random.randint(0, 1) == 0: # Flip is HEAD
        flip.append('H') # Add a HEAD
        
        H_streak += 1 # Change the counters
        T_streak = 0
    
    else:
        flip.append('T') #Add Tail 

        T_streak += 1 #Change counters
        H_streak = 0
    
    # If there is a streak we count it and reset the H/T counters
    if T_streak + H_streak == 3:
        numberOfStreaks += 1
        T_streak, H_streak = 0, 0

print(flip)
print(numberOfStreaks)