def knapsack(items, maxweight):
    """
    Solve the knapsack problem by finding the most valuable
    subsequence of `items` subject that weighs no more than
    `maxweight`.

    `items` is a sequence of pairs `(value, weight)`, where `value` is
    a number and `weight` is a non-negative integer.

    `maxweight` is a non-negative integer.

    Return a pair whose first element is the sum of values in the most
    valuable subsequence, and whose second element is the subsequence.

    from knappsack import knapsack
    >>> items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]

    >>> items = [(1, 900), (1, 500), (1, 498), (1, 4)]
    >>> knapsack(items, 15)
    (11, [(2, 1), (6, 4), (1, 1), (2, 2)])
    """

    def memoized(f):
        """ Memoization decorator for functions taking one or more arguments. """
        class memodict(dict):
            def __init__(self, f):
                self.f = f
            def __call__(self, *args):
                return self[args]
            def __missing__(self, key):
                ret = self[key] = self.f(*key)
                return ret
        return memodict(f)

    # Return the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than j.
    @memoized
    def bestvalue(i, j):
        if i == 0: return 0
        value, weight = items[i - 1]
        if weight > j:
            return bestvalue(i - 1, j)
        else:
            return max(bestvalue(i - 1, j),
                       bestvalue(i - 1, j - weight) + value)

    j = maxweight
    result = []
    for i in xrange(len(items), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            result.append(items[i - 1])
            j -= items[i - 1][1]
    result.reverse()
    return bestvalue(len(items), maxweight), result
    #return result
itemset= []
from random import randint
for z in range (1,101):
    a = randint(1,999)
    gg = ()
    gg = (1,a)
    itemset.append(gg)

retval = knapsack(itemset,1000)
print retval
