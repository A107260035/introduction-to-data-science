{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "week8_A107260035_李旻翰.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNrUmCbpW6kS7Kyu/O9YCZJ",
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
        "<a href=\"https://colab.research.google.com/github/minhanl/introduction-to-data-science/blob/master/week8_A107260035_%E6%9D%8E%E6%97%BB%E7%BF%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FQ9uIybk5QZg",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "24ff73ca-6b4d-4ae9-994c-d23fe096c35b"
      },
      "source": [
        "player_height = float(input(\"請輸入球員身高(公尺):\"))\n",
        "player_weight = float(input(\"請輸入球員體重(公斤):\"))\n",
        "player_bmi = player_weight / player_height**2\n",
        "bmi_label = None\n",
        "if player_bmi > 30:\n",
        "    bmi_label = 'Obese'\n",
        "if player_bmi <= 30 and player_bmi > 25:\n",
        "    bmi_label = 'Overweight'\n",
        "if player_bmi <= 25 and player_bmi > 18.5:\n",
        "    bmi_label = 'Normal weight'\n",
        "if player_bmi <= 18.5:\n",
        "    bmi_label = 'Underweight'\n",
        "print(player_bmi)\n",
        "print(bmi_label)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入球員身高(公尺):1.7\n",
            "請輸入球員體重(公斤):52\n",
            "17.99307958477509\n",
            "Underweight\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PHafZal-6M-K",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "f69dee15-dae6-41be-9405-a1c7bf883389"
      },
      "source": [
        "if True:\n",
        "    print(\"First branch\")\n",
        "elif True:\n",
        "    print(\"Second branch\")\n",
        "elif True:\n",
        "    print(\"Third branch\")"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "First branch\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4f2_YcaY6Vlj",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "121913e0-6e84-4774-8dd5-52350c259bc6"
      },
      "source": [
        "user_int = int(input(\"請輸入一個正整數:\"))\n",
        "if user_int % 3 == 0:\n",
        "    print(\"Fizz\")\n",
        "if user_int % 5 == 0:\n",
        "    print(\"Buzz\")"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數:15\n",
            "Fizz\n",
            "Buzz\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2rYDB5W06a4W",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "ecf25d57-38da-497f-a983-82040ae560f1"
      },
      "source": [
        "user_int = int(input(\"請輸入一個正整數:\"))\n",
        "if user_int % 15 == 0:\n",
        "    print(\"Fizz Buzz\")\n",
        "elif user_int % 5 == 0:\n",
        "    print(\"Buzz\")\n",
        "elif user_int % 3 == 0:\n",
        "    print(\"Fizz\")\n",
        "else:\n",
        "    print(user_int)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數:16\n",
            "16\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lQSe1VcW6lgg",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 185
        },
        "outputId": "475fe338-997e-4638-97c5-4df0ac422bef"
      },
      "source": [
        "i = 2\n",
        "while i <= 20:\n",
        "    print(i)\n",
        "    i += 2"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n",
            "14\n",
            "16\n",
            "18\n",
            "20\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2N6l0_AF6p28",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 202
        },
        "outputId": "2dbfbc1e-c589-42ac-ed77-a99e99bd66fc"
      },
      "source": [
        "i = 1\n",
        "while i <= 10:\n",
        "    print(i)\n",
        "    i += 1\n",
        "print(\"While loop is done.\")"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n",
            "While loop is done.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "J3yKfvyg6xdF",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "cf475568-02cd-4b17-9160-276450a2992e"
      },
      "source": [
        "i = 1\n",
        "counter = 0\n",
        "while i <= 10:\n",
        "    counter += 1\n",
        "    i += 1\n",
        "print(counter)"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "10\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "a-kKG5Sd63Z3",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "2804c95a-458a-4352-dc2a-7a75e2245e55"
      },
      "source": [
        "i = 1\n",
        "counter = 0\n",
        "while i <= 10:\n",
        "    if i % 2 == 0:\n",
        "        counter += 1\n",
        "    i += 1\n",
        "print(counter)"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sKebC8P669Mw",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "251ab801-a4a2-441d-8c87-359d69f0ca1d"
      },
      "source": [
        "i = 1\n",
        "summation = 0\n",
        "while i <= 100:\n",
        "    summation += i\n",
        "    i += 1\n",
        "print(summation)"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "5050\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bU_401Cy7O_z",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 252
        },
        "outputId": "a15a7d65-f46b-4d52-933b-20e630a98d35"
      },
      "source": [
        "x = int(input(\"請輸入起始的正整數:\"))\n",
        "y = int(input(\"請輸入終止的正整數\"))\n",
        "i = x\n",
        "while i <= y:\n",
        "    print(i)\n",
        "    i += 1"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的正整數:55\n",
            "請輸入終止的正整數66\n",
            "55\n",
            "56\n",
            "57\n",
            "58\n",
            "59\n",
            "60\n",
            "61\n",
            "62\n",
            "63\n",
            "64\n",
            "65\n",
            "66\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sdQV4gpM7WF_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 252
        },
        "outputId": "6c9ced1a-458c-4eef-e08c-ab85fbdfc842"
      },
      "source": [
        "x = int(input(\"請輸入起始的正整數:\"))\n",
        "y = int(input(\"請輸入終止的正整數\"))\n",
        "i = x\n",
        "while i <= y:\n",
        "    print(i)\n",
        "    i += 1"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的正整數:55\n",
            "請輸入終止的正整數66\n",
            "55\n",
            "56\n",
            "57\n",
            "58\n",
            "59\n",
            "60\n",
            "61\n",
            "62\n",
            "63\n",
            "64\n",
            "65\n",
            "66\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}