""" Positive integer except sum of two abundant numbers """
# import time module
import time


# create a class
class PositiveIntegers:
    # define a method and pass parameters
    def except_sum_abundant(self, till_num):
        j = 1
        # define empty list for calc and abundant number and append
        abundant_numbers = []
        # while loop for hold a value for checking
        while j < till_num:
            i = 2
            lst = []
            # nested while loop for factor value less than of held number
            while i < j:
                # if condition finding factor
                if j % i == 0:
                    lst.append(i)
                i += 1
            # sum the list for checking whether its abundant or not
            num_1 = sum(lst)
            # if condition for checking abundant number
            if num_1 > j:
                abundant_numbers.append(j)
            j += 1

        print("Abundant numbers are ", abundant_numbers)
        time.sleep(0.5)
        n = 0
        # define empty list for sum of two abundant numbers
        new = []
        # while loop for hold a number in list
        while n < len(abundant_numbers):
            m = 1
            # nested while loop for loop the list except outer while loop
            while m < len(abundant_numbers):
                # if condition for avoid same abundant addition
                if abundant_numbers[n] != abundant_numbers[m]:
                    k = abundant_numbers[n] + abundant_numbers[m]
                    new.append(k)
                m += 1
            n += 1

        # define empty list for avoid duplicate numbers
        unique = []
        for k in new:
            # if condition for avoid duplicate numbers
            if k not in unique:
                unique.append(k)

        print("Sum of abundant numbers are ", unique)
        time.sleep(0.5)
        # define empty list for append positive integer except sum of two abundant numbers
        except_sum_of_abundant_numbers = []
        for o in range(1, till_num+1):
            if o not in unique:
                except_sum_of_abundant_numbers.append(o)

        print("Positive integers except sum of two abundant numbers ", except_sum_of_abundant_numbers)
        time.sleep(0.5)
        print("Sum of all positive numbers except sum of two abundant numbers :", sum(except_sum_of_abundant_numbers))


# create an object for the class
pos_int = PositiveIntegers()
# call the method and pass the argument using created object
pos_int.except_sum_abundant(40)
