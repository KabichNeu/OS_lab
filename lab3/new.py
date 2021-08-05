
def findAndUpdate(x, ref_frames, second_chance, frames):
    for i in range(frames):
        if(ref_frames[i]==x):
            second_chance[i] =True
            return True;
    return False

def replaceAndUpdate(x, ref_frames, second_chance, frames, pointer):
    while True:
        if not second_chance[pointer]:
            ref_frames[pointer] = x
            return ((pointer+1)%frames)
        second_chance[pointer]=False
        pointer = (pointer+1)%frames

def printHitsAndFaults( ref_string, frames):
    pointer, pf =0,0
    ref_frames = [-1 for i in range(frames)]
    second_chance = [False for i in range(frames)]
    ref_string_list = ref_string.split()
    length = len(ref_string_list)
    for i in range(length):
        x = int(ref_string_list[i])
        if not findAndUpdate(x, ref_frames, second_chance, frames):
            pointer = replaceAndUpdate(x, ref_frames, second_chance, frames, pointer)
            pf+=1

    print(f'Total page faults: {pf}')


def main():
    ref_string = input("Enter the reference string:\t")
    frames= input("Enter number of frames: \t")
    printHitsAndFaults(ref_string, int(frames))

main()