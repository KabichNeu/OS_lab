size = int(input("Enter the size of the queue: "))
 
def FCFS(arr, head):
 
    seek_count = 0
    distance, cur_track = 0, 0
    print("Distance is:")
    for i in range(size):
        cur_track = arr[i]
 
        # calculate absolute distance
        distance = abs(cur_track - head)
        print(distance)
 
        # increase the total count
        seek_count += distance
 
        # accessed track is now new head
        head = cur_track
     
    print("Total number of seek operations = ",
                                   seek_count)
 
    # Seek sequence would be the same
    # as request array sequence
    print("Seek Sequence is")
 
    for i in range(size):
        print(arr[i])
     
# Driver code

arr = []
for i in range(size):
    val = int(input("Enter the disk requests: "))
    arr.append(val)
head = int(input("Enter the head value: "))
print("  ")
print("Solution:")
print("  ")

print("Initial position of head:", head)
print("  ")
FCFS(arr, head)
 