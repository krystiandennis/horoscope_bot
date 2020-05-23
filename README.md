# Horoscope Bot
This program is a horoscope bot that receives a name, month and date from the user and produces a custom 5-line horoscope. It first determines the user's zodiac sign using the month and date given and then returns an image representing the zodiac sign and displays the user's daily horoscope. 

## List of Functions

1. print_intro()
2. get_dob()
3. get_sign()
4. zodiac_countdown()
5. get_img()
6. get_horoscope()
7. print_outro()

## Requirements

## Installation

## Libraries

```python
from IPython.core.display import HTML # to modify the location of images
import time # to create countdown
from messages import * # messages to create horoscopes
import random # to generate random choices
from PIL import Image               # imaging library
import matplotlib.pyplot as plt # to create visualiztions in python
from matplotlib.pyplot import imshow # to display images using matplotlib
%matplotlib inline # displays images inline
```
