# def reverse_list(ll):
#     """Reverses a linked list
#     Args:
#         ll: linked list
#     Returns:
#         linked list in reversed form
#     """
#     # put your function implementation here
#     return ll
def reverseArray(setOfNumbers):
    reversedNumbers=setOfNumbers[::-1]
    return reversedNumbers
setOfNumbers = input("enter set of numbers ")
print("revresing your numbers: "+reverseArray(setOfNumbers))    