#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value = ""):
    self.value = value
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
  
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
  
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
     return False
    
  def count_sentences(self):
    sentences = []
    split = self.value.split(" ")
    suffixes = (".", "?", "!")
    for item in split:
      if item.endswith(suffixes):
        sentences.append(item)
    return len(sentences)  