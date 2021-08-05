
	
def findAndUpdate(x: int,arr: int,second_chance: bool,frames: int)-> bool:	
    for i in range(0,frames):
        if (arr[i] == x):
            # Mark that the page deserves a second chance
            # second_chance[i] = true
            
            # Return 'true', that is there was a hit
            # and so there's no need to replace any page
            return True
	
	# Return 'false' so that a page for replacement is selected
	# as he reuested page doesn't exist in memory
    return False


# Updates the page in memory and returns the pointer
def replaceAndUpdate(x: int,arr: int,
			second_chance: bool,frames: int,pointer:int):
	while True:
		# We found the page to replace
		if not second_chance[pointer]:
			# Replace with new page
			arr[pointer] = x
			
			# Return updated pointer
			return (pointer + 1) % frames
	
		# Mark it 'false' as it got one chance
		# and will be replaced next time unless accessed again
		second_chance[pointer] = False
		
		# Pointer is updated in round robin manner
		pointer = (pointer + 1) % frames

def printHitsAndFaults(reference_string, frames):
    pf = 0
    arr = []
    for s in range(0,frames):
            arr[s] = -1
    
    second_chance = list()
    ref = reference_string.split()
    l = len(ref)

    for i in l:
        if i < l:
            x = int(ref[i])
            if not findAndUpdate(x, arr, second_chance, frames):
                pointer = replaceAndUpdate(x, arr,second_chance, frames, pointer)
                pf +=1



# Driver code
def main():
	# Test 1:
    reference_string = "0 4 1 4 2 4 3 4 2 4 0 4 1 4 2 4 3 4"
    frames = 3
	
	# Output is 9
    printHitsAndFaults(reference_string,frames)
	
	# Test 2:
    reference_string = "2 5 10 1 2 2 6 9 1 2 10 2 6 1 2 1 6 9 5 1"
    frames = 4
	
	# Output is 11
    printHitsAndFaults(reference_string,frames)

main()