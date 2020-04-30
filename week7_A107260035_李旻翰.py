{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "week7_A107260035_李旻翰.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNXdt0XeRVfY7CTFJdQcdUI",
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
        "<a href=\"https://colab.research.google.com/github/minhanl/introduction-to-data-science/blob/master/week7_A107260035_%E6%9D%8E%E6%97%BB%E7%BF%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "40WguwiOw7L9",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "23f785bd-e2a5-48a1-e0ff-23bc57bd1b6a"
      },
      "source": [
        "monthly_income = input(\"請輸入月薪：\") \n",
        "saving_account = input(\"請輸入存款：\")\n",
        "monthly_income = int(monthly_income)\n",
        "saving_account = int(saving_account)\n",
        "ans = \"發信用卡\"\n",
        "if monthly_income > 40000 or saving_account > 500000 :\n",
        "    print(ans)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入月薪：60000\n",
            "請輸入存款：450000\n",
            "發信用卡\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OyUs2W6uxrby",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "2b3cd2d0-fbd4-454b-92ab-e4f94e28cb46"
      },
      "source": [
        "user_int = input(\"請輸入一個正整數：\")\n",
        "user_int = int(user_int)\n",
        "if user_int % 2 == 0 :\n",
        "    print(\"{}是偶數\".format(user_int))\n",
        "else:\n",
        "    print(\"{}是奇數\".format(user_int))"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數：5566\n",
            "5566是偶數\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CBVbuFqTyAjn",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "85bdb4ab-a6bb-4249-d5ec-68fd4ccc301a"
      },
      "source": [
        "user_int = input(\"請輸入一個正整數：\")\n",
        "user_int = int(user_int)\n",
        "if user_int % 2 == 0 :\n",
        "    print(\"{}是偶數\".format(user_int))\n",
        "else:\n",
        "    print(\"{}是奇數\".format(user_int))"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數：7788\n",
            "7788是偶數\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MdQUVYZOyLNE",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "e4c2bce4-373a-45d8-fd6d-42fc7d02bce7"
      },
      "source": [
        "user_int = input(\"請輸入一個正整數：\")\n",
        "user_int = int(user_int)\n",
        "if user_int % 2 == 0 :\n",
        "    print(\"{}是偶數\".format(user_int))\n",
        "else:\n",
        "    print(\"{}是奇數\".format(user_int))"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數：8899\n",
            "8899是奇數\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e2bZHTzgybFh",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "61371c8e-b810-4808-9ad9-a41f4c379004"
      },
      "source": [
        "id_last_digit = input(\"請輸入您身分證字號的尾數：\")\n",
        "id_last_digit= int(id_last_digit)\n",
        "if id_last_digit % 2 ==1 :\n",
        "    print(\"星期一三五日領\")\n",
        "else:\n",
        "    print(\"星期二四六日領\")\n",
        "  "
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入您身分證字號的尾數：9\n",
            "星期一三五日領\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "shlsl-4aypPS",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "b2329138-dfad-498b-9e5f-a5195c090005"
      },
      "source": [
        "id_last_digit = input(\"請輸入您身分證字號的尾數：\")\n",
        "id_last_digit= int(id_last_digit)\n",
        "if id_last_digit % 2 ==1 :\n",
        "    print(\"星期一三五日領\")\n",
        "else:\n",
        "    print(\"星期二四六日領\")\n"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入您身分證字號的尾數：6\n",
            "星期二四六日領\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HdpD0GqPzRBm",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "217acdc3-9428-426e-aeb5-e8a69952933f"
      },
      "source": [
        "input_height = float(input(\"請輸入身高（公分）：\"))\n",
        "input_weight = float(input(\"請輸入體重（公斤）：\"))\n",
        "bmi = input_weight / (input_height*0.01)**2\n",
        "if bmi > 30:\n",
        "    label = \"Obese\"\n",
        "elif bmi > 25:\n",
        "    label = \"Overweight\"\n",
        "elif bmi > 18.5:\n",
        "    label = \"Normal weight\"\n",
        "elif bmi <= 18.5:\n",
        "    label = \"Underweight\"\n",
        "print(label)\n"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入身高（公分）：180\n",
            "請輸入體重（公斤）：79\n",
            "Normal weight\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}