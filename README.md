# Postfix-and-Prefix-Calculator
In this lab, you'll use stacks and queues to implement a simple calculator.

Parsing standard (infix) mathematical notation can be difficult, so you'll work with two other notations instead: prefix and postfix. These are a lot easier for computers (and programmers) to deal with, and a lot of the earliest calculators used postfix notation as an input format. Some people even prefer this, and you can still find calculators that support it today.

Your calculator will operate in two steps. The first step is to take user input (a big string) and break it into meaningful pieces: these pieces are called tokens, and this process is called tokenization. The second step is to perform the operations described by the tokens and determine the result. This is called evaluation.

During evaluation, it's useful to treat the input as a queue of tokens. You'll use Python's built-in deque type (short for double-ended queue) as your token queue; import deque from the collections module to access it. To use a deque like a regular queue, call append() to push and popleft() to pop.
