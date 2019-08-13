{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<strong>Name:</strong> pi.py<br>\n",
    "<strong>Purpose:</strong> Get the value of Pi to n number of decimal places<br>\n",
    "<strong>Author:</strong> Jaspreet Singh<br>\n",
    "<strong>Algorithm:</strong> Chudnovsky Algorithm<br>\n",
    "\n",
    "<strong>Module Dependencies:</strong><br>\n",
    "Math provides fast square rooting<br>\n",
    "Decimal gives the Decimal data type which is much better than Float<br>\n",
    "sys is needed to set the depth for recursion.<br>\n",
    "unicodedata for print the symbol PI<br>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math, sys\n",
    "from decimal import *\n",
    "import unicodedata\n",
    "\n",
    "getcontext().rounding = ROUND_FLOOR\n",
    "sys.setrecursionlimit(100000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def factorial(n):\n",
    "    '''\n",
    "    Returns the factorial of number using recursion\n",
    "    \n",
    "    Parameters:\n",
    "        n -- Number whose factorial is required\n",
    "    '''\n",
    "    if not n:\n",
    "        return 1\n",
    "    return n*factorial(n-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def iterate(k):\n",
    "    '''\n",
    "    Returns the sum of the iterations as per the Chudnovsky Algorithm\n",
    "    k iterations give us k-1 digit places of pi, so, we need k+1 iterations for \n",
    "    k digit places of pi\n",
    "    \n",
    "    Parameters:\n",
    "        k -- Number of digits places upto which we want the value of pi  \n",
    "    '''\n",
    "    k = k+1\n",
    "    getcontext().prec = k\n",
    "    \n",
    "    sum=0\n",
    "    for k in range(k):\n",
    "        first = factorial(6*k)*(13591409+545140134*k)\n",
    "        down = factorial(3*k)*(factorial(k))**3*(640320**(3*k))\n",
    "        sum += first/down\n",
    "        \n",
    "    return Decimal(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def pi(k):\n",
    "    '''\n",
    "    Returns the value of pi upto k digits using Chudnovsky Algorithm\n",
    "    \n",
    "    Parameters:\n",
    "        k -- Number of digits places upto which we want the value of pi\n",
    "    '''\n",
    "    \n",
    "    iterSum = iterate(k)\n",
    "    up = 426880*math.sqrt(10005)\n",
    "    pi = Decimal(up) / iterSum\n",
    "    \n",
    "    return pi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Decimal('3.14159265')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pi(8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def shell():\n",
    "    '''\n",
    "    Console function to create the interactive shell\n",
    "    Runs only when the main script is called directly\n",
    "    \n",
    "    No parameters or return value\n",
    "    '''\n",
    "    print('=================================')\n",
    "    print('             ' + unicodedata.lookup('GREEK SMALL LETTER PI') + ' calculator')\n",
    "    print('=================================')\n",
    "    \n",
    "    while True:\n",
    "        try:\n",
    "            k = int(input('Enter the number of decimal places upto which the value of pi should be calculated or enter 0 for exit:'))\n",
    "        except:\n",
    "            print('Something went wrong :(')\n",
    "            continue\n",
    "        else:\n",
    "            if k == 0:\n",
    "                break\n",
    "    \n",
    "        print('==>',end = ' ')\n",
    "        print(pi(k))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=================================\n",
      "             π calculator\n",
      "=================================\n",
      "Enter the number of decimal places upto which the value of pi should be calculated or enter 0 for exit:8\n",
      "==> 3.14159265\n",
      "Enter the number of decimal places upto which the value of pi should be calculated or enter 0 for exit:5\n",
      "==> 3.14159\n",
      "Enter the number of decimal places upto which the value of pi should be calculated or enter 0 for exit:6\n",
      "==> 3.141593\n",
      "Enter the number of decimal places upto which the value of pi should be calculated or enter 0 for exit:2\n",
      "==> 3.14\n",
      "Enter the number of decimal places upto which the value of pi should be calculated or enter 0 for exit:as\n",
      "Something went wrong :(\n",
      "Enter the number of decimal places upto which the value of pi should be calculated or enter 0 for exit:54\n",
      "==> 3.141592653589674961834447252393636744528901830383122710\n",
      "Enter the number of decimal places upto which the value of pi should be calculated or enter 0 for exit:0\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    shell()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Pi Calculator. In the shell below Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit\n",
      ">>> 8\n",
      "3.14159265\n",
      ">>> "
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Name: pi.py\n",
    "Purpose: Get the value of Pi to n number of decimal places\n",
    "Author: Pradipta (geekpradd)\n",
    "Algorithm: Chudnovsky Algorithm\n",
    "License: MIT\n",
    "Module Dependencies:\n",
    "Math provides fast square rooting\n",
    "Decimal gives the Decimal data type which is much better than Float\n",
    "sys is needed to set the depth for recursion.\n",
    "\"\"\"\n",
    "from __future__ import print_function\n",
    "import math, sys\n",
    "from decimal import *\n",
    "getcontext().rounding = ROUND_FLOOR\n",
    "sys.setrecursionlimit(100000)\n",
    "\n",
    "python2 = sys.version_info[0] == 2\n",
    "if python2:\n",
    "\tinput = raw_input\n",
    "\n",
    "def factorial(n):\n",
    "\t\"\"\"\n",
    "\tReturn the Factorial of a number using recursion\n",
    "\tParameters:\n",
    "\tn -- Number to get factorial of\n",
    "\t\"\"\"\n",
    "\tif not n:\n",
    "\t\treturn 1\n",
    "\treturn n*factorial(n-1)\n",
    "\n",
    "\n",
    "def getIteratedValue(k):\n",
    "\t\"\"\"\n",
    "\tReturn the Iterations as given in the Chudnovsky Algorithm.\n",
    "\tk iterations gives k-1 decimal places.. Since we need k decimal places\n",
    "\tmake iterations equal to k+1\n",
    "\t\n",
    "\tParameters:\n",
    "\tk  -- Number of Decimal Digits to get\n",
    "\t\"\"\"\n",
    "\tk = k+1\n",
    "\tgetcontext().prec = k\n",
    "\tsum=0\n",
    "\tfor k in range(k):\n",
    "\t\tfirst = factorial(6*k)*(13591409+545140134*k)\n",
    "\t\tdown = factorial(3*k)*(factorial(k))**3*(640320**(3*k))\n",
    "\t\tsum += first/down \n",
    "\treturn Decimal(sum) \n",
    "\n",
    "def getValueOfPi(k):\n",
    "\t\"\"\"\n",
    "\tReturns the calculated value of Pi using the iterated value of the loop\n",
    "\tand some division as given in the Chudnovsky Algorithm\n",
    "\tParameters:\n",
    "\tk -- Number of Decimal Digits upto which the value of Pi should be calculated\n",
    "\t\"\"\"\n",
    "\titer = getIteratedValue(k)\n",
    "\tup = 426880*math.sqrt(10005)\n",
    "\tpi = Decimal(up)/iter \n",
    "\t\n",
    "\treturn pi\n",
    "\n",
    "def shell():\n",
    "\t\"\"\"\n",
    "\tConsole Function to create the interactive Shell.\n",
    "\tRuns only when __name__ == __main__ that is when the script is being called directly\n",
    "\tNo return value and Parameters\n",
    "\t\"\"\"\n",
    "\tprint (\"Welcome to Pi Calculator. In the shell below Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit\")\n",
    "\n",
    "\twhile True:\n",
    "\t\tprint (\">>> \", end='')\n",
    "\t\tentry = input()\n",
    "\t\tif entry == \"quit\":\n",
    "\t\t\tbreak\n",
    "\t\tif not entry.isdigit():\n",
    "\t\t\tprint (\"You did not enter a number. Try again\")\n",
    "\t\telse:\n",
    "\t\t\tprint (getValueOfPi(int(entry)))\n",
    "\n",
    "if __name__=='__main__':\n",
    "\tshell()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
