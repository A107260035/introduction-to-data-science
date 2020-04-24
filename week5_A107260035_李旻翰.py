{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "week5_A107260035_李旻翰.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMXVLszcW8ZOXRacKikFYD+",
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
        "<a href=\"https://colab.research.google.com/github/minhanl/introduction-to-data-science/blob/master/week5_A107260035_%E6%9D%8E%E6%97%BB%E7%BF%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DA_9hDO96zfM",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "c0d4a82a-0d91-4105-c6b3-9472b95976cc"
      },
      "source": [
        "print(False) # off\n",
        "print(True) # on"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "False\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YYSE_Wet7Hwf",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "d0e1a9c6-2e88-4907-9a35-96b6a91c91de"
      },
      "source": [
        "print(7.7 > 8)\n",
        "print(7.7 > 7)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "False\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V06xSxBy7Mzu",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "dcf2ae00-ce29-4319-a63f-9f1450c391db"
      },
      "source": [
        "print(type(False))\n",
        "print(type(True))"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'bool'>\n",
            "<class 'bool'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "17l23_AI7Qr2",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "95f2975d-6996-4255-b8ef-eadf4fd40a0d"
      },
      "source": [
        "print(type(7.7 > 8))\n",
        "print(type(7.7 > 7))"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'bool'>\n",
            "<class 'bool'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Igf9NGG27Zh4",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "a8a203b1-e6ba-4321-dfb3-3c4914a29771"
      },
      "source": [
        "print(7.7 == 8)\n",
        "print(7.7 != 8)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "False\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DWWmvgh47kIp",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d9aa4219-efb9-448b-9e74-dadc21e227e2"
      },
      "source": [
        "id_last_digit = 7\n",
        "id_last_digit % 2 != 0"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QUuglMk77poq",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "9cb8e459-293a-4d1b-dcc7-7b0524689602"
      },
      "source": [
        "print(not True)\n",
        "print(not False)"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "False\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nQewnFTV7u4y",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "0532158f-4a4d-4684-8b8b-7e74b9ade27b"
      },
      "source": [
        "print(not 7.7 != 8)\n",
        "print(not 7.7 == 8)"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "False\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wwKr6mQ6701S",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "1e07f9f6-d148-446f-f5e6-9179e7064df8"
      },
      "source": [
        "print(5566.00 == 5566)\n",
        "print(type(5566.00))\n",
        "print(type(5566))"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "True\n",
            "<class 'float'>\n",
            "<class 'int'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "M7JLDVAY77Iy",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "b4a70a55-1926-4c8a-a648-cf611f2456b9"
      },
      "source": [
        "print(156 < 120) # False\n",
        "print(7.7 > 7) # True"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "False\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RmdR-f_c7-ks",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "67b9afbc-3de8-4a43-b84c-54f32fddd6c8"
      },
      "source": [
        "print(156 < 120 and 7.7 > 7)\n",
        "print(156 < 120 or 7.7 > 7)"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "False\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "spmpGJfX8EWX",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "72dbbb53-7aba-407d-bad2-22a024d6a625"
      },
      "source": [
        "city = input(\"請輸入您所在的城市：\")\n",
        "weather = input(\"請輸入現在的天氣：\")\n",
        "print(\"我在{}，天氣{}\".format(city, weather))"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入您所在的城市：台北\n",
            "請輸入現在的天氣：陰天\n",
            "我在台北，天氣陰天\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yRMjbnWJ8OMt",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "e0f6fead-93c8-4a8e-ff92-0065762b7e40"
      },
      "source": [
        "city = input(\"請輸入您所在的城市：\")\n",
        "weather = input(\"請輸入現在的天氣：\")\n",
        "tempc = input(\"請輸入現在的攝氏氣溫：\")\n",
        "tempc = int(tempc)\n",
        "tempf = tempc*9/5 + 32\n",
        "\n",
        "print(\"我在{}，天氣{}，攝氏{}度，華氏{}度\".format(city, weather, tempc, tempf))"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入您所在的城市：台北\n",
            "請輸入現在的天氣：陰天\n",
            "請輸入現在的攝氏氣溫：15\n",
            "我在台北，天氣陰天，攝氏15度，華氏59.0度\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FuZOwjBL8Wml",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "fa297e8a-1436-48e7-c7a8-cdf743c75291"
      },
      "source": [
        "id_last_digit = input(\"請輸入您身分證字號的尾數：\")\n",
        "id_last_digit = int(id_last_digit)\n",
        "print(id_last_digit)\n",
        "print(type(id_last_digit))\n",
        "modulo = id_last_digit % 2\n",
        "ans = modulo == 1\n",
        "print(ans)"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入您身分證字號的尾數：6\n",
            "6\n",
            "<class 'int'>\n",
            "False\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Az-VRCti8gl3",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "c4da6a96-6d45-4452-90bb-f7faf84df266"
      },
      "source": [
        "print(float('5566'))\n",
        "print(int('5566'))"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "5566.0\n",
            "5566\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kyLO9Ace8iwY",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "3cf4743b-e9ac-4587-d064-b30aced810c6"
      },
      "source": [
        "print(int(False))\n",
        "print(int(True))"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0\n",
            "1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nPMuNAGZ8pTr",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "3affd9e0-08c2-4b7d-cd6b-5c848273db0c"
      },
      "source": [
        "print(float(False))\n",
        "print(float(True))"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0.0\n",
            "1.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tfbaN7RB8t68",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "a249ab97-7859-49f7-872b-63ab56731e15"
      },
      "source": [
        "print(bool(0))\n",
        "print(bool(1))\n",
        "print(bool(5566))\n",
        "print(bool(55.66))"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "False\n",
            "True\n",
            "True\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BK4HnGkv8xpK",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "ee3e449a-5d36-4f62-e4bf-3f12b4da56ee"
      },
      "source": [
        "print(bool('False'))\n",
        "print(bool('True'))"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "True\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HiERK6qI800h",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 151
        },
        "outputId": "54acdf84-0a84-41fe-87ad-78c0e6eea412"
      },
      "source": [
        "help(bin)"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Help on built-in function bin in module builtins:\n",
            "\n",
            "bin(number, /)\n",
            "    Return the binary representation of an integer.\n",
            "    \n",
            "    >>> bin(2796202)\n",
            "    '0b1010101010101010101010'\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sYI6mgww86JR",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "7249a702-d5f8-4ce4-e787-e096d8a80d32"
      },
      "source": [
        "help(ord)"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Help on built-in function ord in module builtins:\n",
            "\n",
            "ord(c, /)\n",
            "    Return the Unicode code point for a one-character string.\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gfaAw6dE89TA",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "2d2c9241-a703-406e-a601-9e821f2a6a08"
      },
      "source": [
        "ord('A')"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "65"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Hyxj-fz29D6z",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "38e486ae-f6c3-458a-d5d3-d5cdaecd6b8a"
      },
      "source": [
        "bin(ord('A'))"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'0b1000001'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    }
  ]
}