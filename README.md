# Constant of Kaprekar

A program witch makes the Kaprekar's rotine for a number given by the user. 

This number was analysed by the indian mathematician Dattatreya Ramchandra Kaprekar, or D. R. Kaprekar. He noticed that, if you take any 4-digit number, not all being the same (leading zeros are allowed) and obey the following process: 

- Arrange the digits in descending and then in ascending order to get two four-digit numbers, considering leading zeros.
- Subtract the smaller number from the bigger number.
- Go back first to step and repeat.

at some point, the number 6174 will be reached, and happens that this process can't go any further. That means, if you do the rotine again, it will give the same result:

  7641 - 1467 = 6174

There is also a 3-digit version of the Kaprekar's constant, witch is the number 495. For illustrative porpuses:

  954 - 459 = 495
