# ########################################  Miscellaneous functions ####################################################

def rotate_right(arr, l, r):
    """"Rotates array arr right between l and r. r is included."""
    temp = arr[r]
    for i in range(r, l, -1):
        arr[i] = arr[i-1]
    arr[l] = temp


def rotate_left(arr, l, r):
    """"Rotates array arr left between l and r. r is included."""
    temp = arr[l]
    for i in range(l, r):
        arr[i] = arr[i+1]
    arr[r] = temp