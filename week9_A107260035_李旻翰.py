{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "week9_A107260035_李旻翰.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOc70YQWB9Sf+x98UQGyi4g",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/minhanl/introduction-to-data-science/blob/master/week9_A107260035_%E6%9D%8E%E6%97%BB%E7%BF%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "td4tsxlI8rJi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "f1e18b3e-86f1-4b7c-edb2-639d73ec597e"
      },
      "source": [
        "x = int(input(\"請輸入起始的整數:\"))\n",
        "y = int(input(\"請輸入終止的整數:\"))\n",
        "i = x # start\n",
        "while i <= y: # stop\n",
        "    # task\n",
        "    if i % 2 == 1:\n",
        "        print(i)\n",
        "    i += 1 # step"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的整數:5\n",
            "請輸入終止的整數:10\n",
            "5\n",
            "7\n",
            "9\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "df2rI0TC8-JE",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "03543704-a10b-4521-921f-703b633e90a1"
      },
      "source": [
        "x = int(input(\"請輸入起始的整數:\"))\n",
        "y = int(input(\"請輸入終止的整數:\"))\n",
        "odd_counter = 0 # 歸零\n",
        "i = x # start\n",
        "while i <= y: # stop\n",
        "    # task\n",
        "    if i % 2 == 1:\n",
        "        #odd_counter = odd_counter + 1 # = NOT ==\n",
        "        odd_counter += 1 # 計數累計\n",
        "    #print(odd_counter)\n",
        "    i += 1 # step\n",
        "print(\"======\")\n",
        "print(odd_counter)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的整數:5\n",
            "請輸入終止的整數:10\n",
            "======\n",
            "3\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jJFDpWeT9I3R",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "132e9f3a-d230-43ca-d186-49e2684497dd"
      },
      "source": [
        "x = int(input(\"請輸入起始的整數:\"))\n",
        "y = int(input(\"請輸入終止的整數:\"))\n",
        "odd_summation = 0 # 歸零\n",
        "i = x # start\n",
        "while i <= y: # stop\n",
        "    # task\n",
        "    if i % 2 == 1:\n",
        "        odd_summation = odd_summation + i # 數值累加\n",
        "    i += 1 # step\n",
        "print(\"======\")\n",
        "print(odd_summation)"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的整數:5\n",
            "請輸入終止的整數:10\n",
            "======\n",
            "21\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WPDtDJ8r9P8I",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 202
        },
        "outputId": "50c4c1b3-85e9-47e7-d1d6-99ae700e67b1"
      },
      "source": [
        "x = int(input(\"請輸入起始的整數:\"))\n",
        "y = int(input(\"請輸入終止的整數:\"))\n",
        "odd_summation = 0 # 歸零\n",
        "odd_counter = 0\n",
        "i = x # start\n",
        "while i <= y: # stop\n",
        "    # task\n",
        "    if i % 2 == 1:\n",
        "        odd_counter += 1 # 計數累計\n",
        "        odd_summation += i # 數值累加\n",
        "        print(\"現在的整數是:{}, 奇數計數為{}個, 總和為{}\".format(i, odd_counter, odd_summation))\n",
        "    else:\n",
        "        print(\"現在的整數是:{}, 奇數計數為{}個, 總和為{}\".format(i, odd_counter, odd_summation))\n",
        "    i += 1 # step\n",
        "print(\"======\")\n",
        "print(odd_counter)\n",
        "print(odd_summation)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的整數:5\n",
            "請輸入終止的整數:10\n",
            "現在的整數是:5, 奇數計數為1個, 總和為5\n",
            "現在的整數是:6, 奇數計數為1個, 總和為5\n",
            "現在的整數是:7, 奇數計數為2個, 總和為12\n",
            "現在的整數是:8, 奇數計數為2個, 總和為12\n",
            "現在的整數是:9, 奇數計數為3個, 總和為21\n",
            "現在的整數是:10, 奇數計數為3個, 總和為21\n",
            "======\n",
            "3\n",
            "21\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XHjBqTNI9bqy",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 353
        },
        "outputId": "5491fb1e-ffef-4420-868b-3fe58b59cc34"
      },
      "source": [
        "x = int(input(\"請輸入一個正整數:\"))\n",
        "i = 1 # start\n",
        "divisor_counter = 0 # 歸零\n",
        "while i <= x: # stop\n",
        "    if x % i == 0:\n",
        "        divisor_counter += 1\n",
        "        print(\"{}可以被{}整除\".format(x, i))\n",
        "        print(\"因數個數目前有{}個\".format(divisor_counter))\n",
        "        print(\"======\")\n",
        "    i += 1 # step\n",
        "print(\"### Answer ###\")\n",
        "print(\"總共執行了{}次迴圈\".format(i - 1))\n",
        "print(\"{}共有{}個因數\".format(x, divisor_counter))\n",
        "if divisor_counter == 2:\n",
        "    print(\"{}是質數\".format(x))\n",
        "else:\n",
        "    print(\"{}不是質數\".format(x))"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數:16\n",
            "16可以被1整除\n",
            "因數個數目前有1個\n",
            "======\n",
            "16可以被2整除\n",
            "因數個數目前有2個\n",
            "======\n",
            "16可以被4整除\n",
            "因數個數目前有3個\n",
            "======\n",
            "16可以被8整除\n",
            "因數個數目前有4個\n",
            "======\n",
            "16可以被16整除\n",
            "因數個數目前有5個\n",
            "======\n",
            "### Answer ###\n",
            "總共執行了16次迴圈\n",
            "16共有5個因數\n",
            "16不是質數\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yVO9gAXd9qdr",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 185
        },
        "outputId": "075ad354-6b5a-43da-9f96-2abb430f1f90"
      },
      "source": [
        "x = int(input(\"請輸入一個正整數:\"))\n",
        "i = 1 # start\n",
        "divisor_counter = 0 # 歸零\n",
        "while i <= x: # stop\n",
        "    if x % i == 0:\n",
        "        divisor_counter += 1\n",
        "        print(\"{}可以被{}整除\".format(x, i))\n",
        "        print(\"因數個數目前有{}個\".format(divisor_counter))\n",
        "        print(\"======\")\n",
        "    i += 1 # step\n",
        "    if divisor_counter > 2:\n",
        "        break\n",
        "print(\"### Answer ###\")\n",
        "print(\"總共執行了{}次迴圈\".format(i - 1))\n",
        "if divisor_counter == 2:\n",
        "    print(\"{}是質數\".format(x))\n",
        "else:\n",
        "    print(\"{}不是質數\".format(x))"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數:11\n",
            "11可以被1整除\n",
            "因數個數目前有1個\n",
            "======\n",
            "11可以被11整除\n",
            "因數個數目前有2個\n",
            "======\n",
            "### Answer ###\n",
            "總共執行了11次迴圈\n",
            "11是質數\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Vaa3YjD_9zYT",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "f666b6bb-2056-4faf-a1aa-173e13b28d06"
      },
      "source": [
        "i = 1 # start\n",
        "while i <= 100: # stop\n",
        "    if i % 15 == 0:\n",
        "        print(\"Fizz Buzz\")\n",
        "    elif i % 3 == 0:\n",
        "        print(\"Fizz\")\n",
        "    elif i % 5 == 0:\n",
        "        print(\"Buzz\")\n",
        "    else:\n",
        "        print(i)\n",
        "    i += 1 # step"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "Fizz\n",
            "4\n",
            "Buzz\n",
            "Fizz\n",
            "7\n",
            "8\n",
            "Fizz\n",
            "Buzz\n",
            "11\n",
            "Fizz\n",
            "13\n",
            "14\n",
            "Fizz Buzz\n",
            "16\n",
            "17\n",
            "Fizz\n",
            "19\n",
            "Buzz\n",
            "Fizz\n",
            "22\n",
            "23\n",
            "Fizz\n",
            "Buzz\n",
            "26\n",
            "Fizz\n",
            "28\n",
            "29\n",
            "Fizz Buzz\n",
            "31\n",
            "32\n",
            "Fizz\n",
            "34\n",
            "Buzz\n",
            "Fizz\n",
            "37\n",
            "38\n",
            "Fizz\n",
            "Buzz\n",
            "41\n",
            "Fizz\n",
            "43\n",
            "44\n",
            "Fizz Buzz\n",
            "46\n",
            "47\n",
            "Fizz\n",
            "49\n",
            "Buzz\n",
            "Fizz\n",
            "52\n",
            "53\n",
            "Fizz\n",
            "Buzz\n",
            "56\n",
            "Fizz\n",
            "58\n",
            "59\n",
            "Fizz Buzz\n",
            "61\n",
            "62\n",
            "Fizz\n",
            "64\n",
            "Buzz\n",
            "Fizz\n",
            "67\n",
            "68\n",
            "Fizz\n",
            "Buzz\n",
            "71\n",
            "Fizz\n",
            "73\n",
            "74\n",
            "Fizz Buzz\n",
            "76\n",
            "77\n",
            "Fizz\n",
            "79\n",
            "Buzz\n",
            "Fizz\n",
            "82\n",
            "83\n",
            "Fizz\n",
            "Buzz\n",
            "86\n",
            "Fizz\n",
            "88\n",
            "89\n",
            "Fizz Buzz\n",
            "91\n",
            "92\n",
            "Fizz\n",
            "94\n",
            "Buzz\n",
            "Fizz\n",
            "97\n",
            "98\n",
            "Fizz\n",
            "Buzz\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}