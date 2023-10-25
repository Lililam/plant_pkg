#!/usr/bin/env python
# coding: utf-8

# In[1]:


from func import is_prime, generate_primes
import pytest


# In[7]:


@pytest.mark.parametrize("example, expectation",[
    (10, [2, 3, 5, 7]),
    (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    (3,[2, 3]), # edge case
    (1, []), # edge case
    (0, []), # edge case
    (-1, [])]) # edge case
def test_generate_primes_parameterized(example, expectation):
    result = generate_primes(example)
    assert result == expectation, f"Failed from {example}."


# In[8]:


@pytest.fixture
def prime_numbers():
    return generate_primes(50)
def test_prime_using_fixture(prime_numbers):
    for i in prime_numbers:
        assert is_prime(i), f"{i} is not a prime number"
def test_generate_primes_with_fixture(prime_numbers):
    result = generate_primes(50) 
    assert result == prime_numbers[:50], "Failed for limit = 50"
    assert result[0] == 2, "Unexpected first prime"
    assert result[-1] == 47, "Unexpected last prime"


# In[ ]:




