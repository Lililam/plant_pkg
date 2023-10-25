#!/usr/bin/env python
# coding: utf-8

# In[30]:


from func import is_prime, generate_primes
import pytest


# In[31]:


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False


# In[35]:


@pytest.mark.parametrize("example, expected",[
    (2, True), # 2 is a prime number
    (7, True), # 7 is a prime number
    (8, False), # 8 is not a prime number
    (9, False), # 9 is not a prime number
    (-1, False), # testing negative number
    (0, False), # testing edge number 0
    (1, False), # testing edge number 1
])
def test_is_prime_param(example, expected):
    result = is_prime(example)
    assert result == expected 


# In[33]:


def test_generate_primes():
    result = generate_primes(10)
    assert result == [2, 3, 5, 7], "Failed for limit = 10"
    
    result = generate_primes(-1)
    assert result == [], "Failed for limit = -1"
    
    result = generate_primes(1)
    assert result == [], "Failed for limit = 1"
    
    result = generate_primes(0)
    assert result == [], "Failed for limit = 0"
    


# In[34]:


def test_prime_integration():
    result = generate_primes(10)
    for i in result:
        assert is_prime(i), f"{i} is not a prime number"


# In[ ]:





# In[ ]:





# In[ ]:




