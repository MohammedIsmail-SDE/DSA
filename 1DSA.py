# 1Q. write a program that will convert celsius value to fahrenheit 
# cell_faharn = int(input("enter clesius :"))
# faharn_temp = 1.8*(cell_faharn)
# result = 32+faharn_temp
# print("faharn_temp :-",result)

#2Q.user will input(2numbers). write a program to swap the numbers 

# a = int(input("enter num:")) 
# b = int(input("enter num:"))
# a,b = b,a
# print (a)
# print (b)

#3Q
# nums = [4,2,5,7]

# nums(len)= 0,1,2,3,4
# nums(len)=0,2,1,3,4 
# print (nums)
#3Q. Complete the function printNumber which takes an integer input from the user and prints it on the screen.

# number = int(input("enter number :"))
# print("enter number is ",number)
# class Solution:
#     def mergeArrays(self, nums1, nums2):
#         """Merge two lists of [id, value] by id, summing values for equal ids and
#         returning a sorted list by id.
#         """
#         i, j = 0, 0
#         res = []
#         while i < len(nums1) and j < len(nums2):
#             id1, val1 = nums1[i]
#             id2, val2 = nums2[j]
#             if id1 == id2:
#                 res.append([id1, val1 + val2])
#                 i += 1
#                 j += 1
#             elif id1 < id2:
#                 res.append([id1, val1])
#                 i += 1
#             else:
#                 res.append([id2, val2])
#                 j += 1
#         # append remaining
#         while i < len(nums1):
#             res.append(nums1[i])
#             i += 1
#         while j < len(nums2):
#             res.append(nums2[j])
#             j += 1
#         return res
import pyttsx3
pyttsx3.speak("zainab")