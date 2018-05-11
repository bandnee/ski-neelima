# Enter your code here. Read input from STDIN. Print output to STDOUT
def TH(ndisk):
    # towerHanoi(ndisk, start,empty_rod,target_rod)
    towerHanoi(ndisk, 'r1', 'r3', 'r2')


def towerHanoi(height, from_pole, to_pole, use_pole):
    if height > 0:
        towerHanoi(height-1,from_pole, use_pole, to_pole)
        moveDisk(height, from_pole, to_pole)
        towerHanoi(height-1, use_pole, to_pole, from_pole)


def moveDisk(disk, fp, tp):
    print("Moving disk no ", disk, "from", fp, "to", tp)


TH(5)