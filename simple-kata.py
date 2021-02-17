# 1
# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b.
#
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]

# Solution:
def array_diff(a, b):
    r = []

    for i in a:
        if i not in b:
            r.append(i)
    return r

# or
def list_diff(a, b):
    return [x for x in a if x not in b]



# 2
# Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.
#
# Example:
#
# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

