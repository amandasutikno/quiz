"""
-----------------------------------------------------------------------
Question 1.

Given two int values, return True if one is negative and one is
positive. Except if the parameter "negative" is True, then return True
only if both are negative.
-----------------------------------------------------------------------

"""


def pos_neg(a, b, negative):
    if int(a) < 0 and int(b) < 0:
        return True
    elif int(a) < 0 and int(b) > 0:
        return True
    elif int(a) > 0 and int(b) < 0:
        return True
    else:
        return False


# Expected outputs:

print(pos_neg(1, -1, False))
# True
print(pos_neg(-1, 1, False))
# True
print(pos_neg(-4, -5, True))
# True
print(pos_neg(-2, -5, False))
# False
print(pos_neg(1, 2, False))
# False


"""
-----------------------------------------------------------------------
Question 2.

A year with 366 days is called a leap year. Leap years are necessary to
keep the calendar synchronized with the sun because the earth revolves
around the sun once every 365.25 days. Actually, that figure is not
entirely precise, and for all dates after 1582 the Gregorian correction
applies. Usually years that are divisible by 4 are leap years, for
example 1996. However, years that are divisible by 100 (for example,
1900) are not leap years, but years that are divisible by 400 are leap
years (for example, 2000).
-----------------------------------------------------------------------

"""


def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(leap_year(1900))
# print(leap_year(2016))
# print(leap_year(2017))
# print(leap_year(2000))




"""
-----------------------------------------------------------------------
Question 3:

Write a function with loops that computes the sum of all squares between
1 and n (inclusive).
-----------------------------------------------------------------------

"""


def sum_squares(n):
    s = 0
    for i in range(0,n):
        s = s + i * i
print (s)

# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(sum_squares(1))
# print(sum_squares(100))
