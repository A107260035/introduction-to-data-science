{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "week4_A107260035_李旻翰.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPcBsgJuKhheStf1Wbqi0dy",
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
        "<a href=\"https://colab.research.google.com/github/minhanl/introduction-to-data-science/blob/master/week4_A107260035_%E6%9D%8E%E6%97%BB%E7%BF%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1CkcOT6r3N5G",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "e42a6db3-e38f-4f0b-8284-b3a99ba40a6f"
      },
      "source": [
        "current_Celsius = 25\n",
        "Fahrenheit = current_Celsius*9/5+32\n",
        "print(Fahrenheit)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "77.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "z_eZfgPm4dk9",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "0e55340f-8c02-4b31-ec88-af320fe104d7"
      },
      "source": [
        "current_Fahrenheit = 77\n",
        "Celsius = (Fahrenheit-32)*5/9\n",
        "print(Celsius)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "25.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iCLmlL3L41bn",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "238e71cb-65f7-4a37-dd8a-9e5edc3aea94"
      },
      "source": [
        "shaq_weight = 147\n",
        "shaq_height = 216\n",
        "shaq_bmi = shaq_weight/(shaq_height/100)**2\n",
        "print(shaq_bmi)"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "31.507201646090532\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lfgKeXLJ458T",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "be8104bf-067d-46e3-fdf5-ca7c5996b1d8"
      },
      "source": [
        "ross_said = \"\"\"Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring.\"\"\"\n",
        "print(ross_said)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RGU-8cPU4-Sg",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "d1e9db39-a548-4fff-a04d-1bfa8c50b418"
      },
      "source": [
        "city = input(\"請輸入城市: \" )\n",
        "weather = input(\"請輸入天氣: \" )\n",
        "print(\"我在{}，天氣{}\".format(city, weather))"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入城市: 台北\n",
            "請輸入天氣: 陰天\n",
            "我在台北，天氣陰天\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XovO8OMI5OMj",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "cdf5a814-3fce-4c4f-c264-4ee3558761e6"
      },
      "source": [
        "name = input(\"請輸入姓名: \")\n",
        "shaq_height = eval(input(\"請輸入身高: \"))\n",
        "shaq_weight = eval(input(\"請輸入體重: \"))\n",
        "shaq_bmi = shaq_weight/(shaq_height/100)**2\n",
        "print(\"{}的身體質量指數為：{:.2f}\".format(name,shaq_bmi)) \n",
        "print(\"{}是否過重：{}\".format(name,shaq_bmi > 30))"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入姓名: shaq\n",
            "請輸入身高: 216\n",
            "請輸入體重: 147\n",
            "shaq的身體質量指數為：31.51\n",
            "shaq是否過重：True\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}