# Testing
# We can lots of errors- we eant to test to save time and money
# types of test:
# functional tests = unit tests/ integration testing/ user-acceptance testing.
# non -functional performance, scalaibity, usuability. 
# pytest
# pip install pytest

#def func(num):
#    return num * 2

#def test_answer(): # name the test test_.....
#    assert func(6) == 12



def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1 
    return sum 

def test_count_int():
    assert count([1,2,2,4,5,2],2) == 3
    assert count([],2) == 0
    assert count([99, 88, 77, 206, 77], 77) == 2

def test_count_str():
    assert count(["apple", "orange", "apple", "apple"], "apple") == 3
    assert count (["apple", "apple", "orange"], "pear") == 0
    
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def test_fact():
    assert fact(5) == 120
    assert fact(0) == 1
    assert fact(1) == 1


def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels

def test_vowel_count():
    assert vowels("orange") == 3
    assert vowels("PULP") == 1
    assert vowels("ORANGE") == 3
    
    
def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d

def test_list_of_squares():
    assert list_of_squares(2) == {1:1,2:4}    