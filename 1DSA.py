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
# import pyttsx3
# pyttsx3.speak("h")
# weight_lbs = input("please enter weight in pounds : ")
# weight_kg = int(weight_lbs)*0.45
# print ("kg is ",weight_kg)
# frist = input("enter your frist name :")
# last = input ("enter your last name :")
# full_name = f'{frist} [{last}] is a coder'
# print(full_name)
# X =5 
# X =
# print (X)

#if it's hot it's a hot day drink plenty of water 
#otherwise if it's a cold day wear warm clothes 
#otherwise 
# it's a lovely day 

#price of house is 1m$
# if buyer have a good credit 
#they need to put down 10%
#otherwise 
#they need to put down 20%
#print the down payment  

# price_of_house = 1000000
# buyer_have_a_good_credit = False

# if buyer_have_a_good_credit :
#     down_payment = 0.1*price_of_house

# else :
#      down_payment = 0.2*price_of_house

# print(f"Down payment is :${down_payment}")

# has_high_income = True
# has_goood_credit = False

# if has_high_income or has_goood_credit:
#     print("eligible for loan")

# temperature = 40

# if temperature == 40 :
#     print("its a worm day")
# else :
#     print ("its a normal day")

# name = input("please enter your name :")

# if len(name )<3:
#     print ("name must be above than 3 characters")
# elif len(name)>50 :
#     print ("name cannot be more than 50 characters")
# else :
#     print("Hi",name)
num = int (input ( "please enter weight : "))
units = input("This weight is in (L)bs or (k)g :")

if units.upper() == "L":
    converted = round(num *0.45,3)

    print(f'you are {converted} kilo')
else:
    converted = round(num / 0.45,3)
    print(f"your are {converted} pounds")


