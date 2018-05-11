#given a 2D array, merge intervals

#array = [[1,3],[5,7],[2,4],[6,8]]

#sort the array with the first element
# Array becomes : [[1,3],[2,4],[5,7],[6,8]]
# if the previous end is > this_start
# intervals can be merged , with element
#[prev_start,this_end], repeat this till the end of the 2Darray

def merge_intervals(in_arr):
    s_arr = sorted(in_arr)
    m_arr = [[]]
    for i in range(len(s_arr)-1):
        prev = s_arr[i]
        this = s_arr[i+1]
        if prev[1] > this[0] :
            #merge intervals
            m_tuple = []
            m_tuple.append(prev[0])
            m_tuple.append(this[1])
            m_arr.append(m_tuple)
        else:
            m_arr.append(prev)
    return m_arr





