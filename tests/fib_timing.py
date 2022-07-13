# Fibonnaci sequence

import time
import subprocess
import rust_modules
import somefile

# Fib in python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    

# Call a binary file and save the result in a variable

def call_binary(exe_file):
    return subprocess.check_output(f"{exe_file}", shell=True)


# Return only numbers from a string

def return_number(string):
    return int(string.split()[0])

# Python call

# t0 = time.time()

# a = fib(35)

# t1 = time.time()

# total_time = t1 - t0
# print(f"Fib = {a}. Total time of Python Fib: {total_time}")

# CPP call
t2 = time.time()

b = call_binary("fib_cpp.exe")

t3 = time.time()

total_time_2 = t3 - t2
print(f"Fib = {return_number(b)}. Total time of CPP Fib: {total_time_2}")

# Rust call
t4 = time.time()

c = call_binary("fib_rs.exe")

t5 = time.time()

total_time_3 = t5 - t4
print(f"Fib = {return_number(c)}. Total time of Rust Fib: {total_time_3}")

# Rust module

t6 = time.time()

d = somefile.fib(35)

t7 = time.time()

total_time_4 = t7 - t6
print(f"Fib = {d}. Total time of Rust Module Fib: {total_time_4}")