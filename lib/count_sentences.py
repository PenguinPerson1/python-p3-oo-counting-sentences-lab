#!/usr/bin/env python3
import re

class MyString:
  def __init__(self,value=''):
    self.value=value

  def is_sentence(self):
    return self.value[-1]=="."
  
  def is_question(self):
    return self.value[-1]=="?"
  
  def is_exclamation(self):
    return self.value[-1]=="!"

  def count_sentences(self):
    if len(self.value) == 0:
      return 0
    split_string=re.split('[.?!] ',self.value)
    count = len(split_string)-1
    if self.is_sentence() or self.is_question() or self.is_exclamation():
      count=count+1
    return count

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self,value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")
