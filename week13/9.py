# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Zf9FALuFGoo31qbOvUDqhRIEi_petyq
"""

def is_prime(x):
  """
  Retuen True if x is a prime, or return False
  """
  divisors = []
  for i in range(1, x+1):
    if x % i ==0:
      divisors.append(i)
  n_divisors = len(divisors)
  return n_divisors == 2