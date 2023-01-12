#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 12:01:26 2023

@author: boladipo
"""

def Calculator(A, B, C):
  """
  This program allows the usage of knowledge of python variable, strings, operations, expressions, conditional statemenets,
  containers and for loops and functions design and create a fully fuctional calculator that meets the following specifications:


  . Receivers input for values and type of operation to be excuted
  . Checks that user input is valid type of operation requested
  . Executes operation and outputs the result to the screen
  . Capable of doing the following
      . Multiplication
      . Division
      . Substitution
      . Addition
      . Reminder
  
  """


  if C == "*":
    print("A multiply by B is :", A * B)

  elif C == "/":
    print("A divided by B is :", A / B)
  
  elif C == "-":
    print("B subtracted from A is :", A - B)

  elif C == "+":
    print("A added to B is :", A + B)
  elif C == "%":
    print("A modulus B gives a reminder of :", A%B)

A = float(input("Enter the first Number :"))
B = float(input("Enter the second number :"))
C = input("Enter the operations you want to perform e.g(*, /, -, +, %) :")

Calculator(A, B, C)

