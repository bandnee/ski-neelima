# Complete the function below.
def levenshteinDistance_recurse(s1, s2):
    return (distance(s1, s2))


def distance(s1, s2):
    if min(len(s1), len(s2)) == 0:
        return max(len(s1), len(s2))

    if s1[0] == s2[0]:
        return distance(s1[1:], s2[1:])
    # insert distance
    id = distance(s1[1:], s2) + 1
    # delete distance
    dd = distance(s1, s2[1:]) + 1
    # replace distance
    rd = distance(s1[1:], s2[1:]) + 1

    return min(min(id, dd), rd)


def levenshteinDistanceMemo(s1, s2):
    # Cache will store all keys with
    # key as "str1,str2"
    cache = {}
    return (distance_memo(s1, s2, cache))


def distance_memo(s1, s2, cache):
    if min(len(s1), len(s2)) == 0:
        return max(len(s1), len(s2))

    if s1[0] == s2[0]:
        return distance(s1[1:], s2[1:], cache)

    id = 0
    dd = 0
    rd = 0
    id_key = _makeKey(s1[1:], s2)
    dd_key = _makeKey(s1, s2[1:])
    rd_key = _makeKey(s1[1:], s2[1:])

    # insert distance
    if id_key in cache.keys():
        id = cache[id_key]
    else:
        id = distance(s1[1:], s2) + 1
        cache[id_key] = id

    # delete distance
    if dd_key in cache.keys():
        dd = cache[dd_key]
    else:
        dd = distance(s1, s2[1:]) + 1
        cache[dd_key] = dd

    # replace distance
    if rd_key in cache.keys():
        rd = cache[rd_key]
    else:
        rd = distance(s1[1:], s2[1:]) + 1
        cache[rd_key] = rd

    return min(min(id, dd), rd)


def distance_dp(s1, s2):
    table = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        table[i][0] = i
    for j in range(len(s2) + 1):
        table[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = min(min(table[i - 1][j], table[i][j - 1]), table[i - 1][j - 1]) + 1
    return (table[i][j])


def _makeKey(s1, s2):
    key = s1 + "," + s2
    return (key)


def levenshteinDistance(s1, s2):
    # Cache will store all keys with
    # key as "str1,str2"
    return (distance_dp(s1, s2))


print(distance_dp('pizza','yolo'))