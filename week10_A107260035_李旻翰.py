{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "_weel10_A107260035_李旻翰.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP8edKrKSGMa1VFeISlKnxz",
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
        "<a href=\"https://colab.research.google.com/github/minhanl/introduction-to-data-science/blob/master/week10_A107260035_%E6%9D%8E%E6%97%BB%E7%BF%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3VCIHyRC_OGT",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "lucky_num_0 = 7\n",
        "lucky_num_1 = 24\n",
        "lucky_num_2 = 5566\n",
        "lucky_numbers = [7, 24, 5566]"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dE-Dob4t78A7",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "sat = \"Saturday\"\n",
        "sun = \"Sunday\""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1n5eR_2t8AZn",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "weekend = [\"Saturday\", \"Sunday\"]\n",
        "weekdays = [\"Monday\", \"Tuesday\", \"Wednesday\", \"Thursday\", \"Friday\"]"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HMNJ46eB8Cap",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "6681c4a4-651f-43f9-9de9-df14348a1f23"
      },
      "source": [
        "print(type(lucky_numbers))"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'list'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "d140EIqD8HTg",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "c599e982-9a62-4498-ecb6-59a8f3fe4e5c"
      },
      "source": [
        "print(type(weekend))"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'list'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YXGgqPuw8LfK",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "f1365165-30c6-4270-80df-28c9320c0f2a"
      },
      "source": [
        "print(type(weekdays))"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'list'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Uu9WwtVr8Pnd",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "340d2e61-ddac-45a9-f88e-89ad2f299c42"
      },
      "source": [
        "print(len(lucky_numbers))\n",
        "print(len(weekend))\n",
        "print(len(weekdays))"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3\n",
            "2\n",
            "5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BZiHXOSG8TJo",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "f3bf884e-23df-4b1c-b1ac-387945cb3cdf"
      },
      "source": [
        "my_fav_weekday = \"Friday\"\n",
        "print(\"My favorite weekday is {}.\".format(my_fav_weekday))"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "My favorite weekday is Friday.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ddofBMqD8d0l",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "b7bc2728-29cc-494f-8ac6-243af8d42270"
      },
      "source": [
        "print(lucky_numbers)\n",
        "lucky_numbers.append(87)\n",
        "print(lucky_numbers)"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[7, 24, 5566]\n",
            "[7, 24, 5566, 87]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LU7XYHTl8j36",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "f742572d-50c2-4ef8-c414-82d2d68207ed"
      },
      "source": [
        "print(lucky_numbers)\n",
        "lucky_numbers.pop()\n",
        "print(lucky_numbers)"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[7, 24, 5566, 87]\n",
            "[7, 24, 5566]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1xpAcQuT8nfE",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "2b6e6101-1d53-4f50-bcf8-cd04367f2841"
      },
      "source": [
        "my_fav_group = lucky_numbers.pop()\n",
        "print(lucky_numbers)\n",
        "print(my_fav_group)"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[7, 24]\n",
            "5566\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WKJ3R5aK8qlB",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "a31f048d-90f5-4616-8f88-23a861e9c50a"
      },
      "source": [
        "print(weekdays)\n",
        "print(weekend)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']\n",
            "['Saturday', 'Sunday']\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kuvEyK1M8up3",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d648f5ac-8d92-446f-cf91-53b28e38b437"
      },
      "source": [
        "weekdays + weekend"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ozQZHUdI8xTE",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "ed342706-190b-43f9-8285-30e13408dcd2"
      },
      "source": [
        "weekend + weekdays"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IGthI2YD848t",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "39ddf0ee-6035-49c8-93fe-56014f01ce68"
      },
      "source": [
        "print(weekdays[0])\n",
        "print(weekdays[1])\n",
        "print(weekdays[2])\n",
        "print(weekdays[3])\n",
        "print(weekdays[4])"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Monday\n",
            "Tuesday\n",
            "Wednesday\n",
            "Thursday\n",
            "Friday\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RNOgGzIc87tv",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "95dda1c0-c0b5-4485-e798-4ff93db4e461"
      },
      "source": [
        "i = 0\n",
        "while i < 5:\n",
        "    print(weekdays[i])\n",
        "    i += 1"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Monday\n",
            "Tuesday\n",
            "Wednesday\n",
            "Thursday\n",
            "Friday\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TP6pqaqH8-Pg",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "f4b9ed7e-f6f7-45b8-c5e5-be64bbeedf23"
      },
      "source": [
        "i = 0\n",
        "while i < 2:\n",
        "    print(weekend[i])\n",
        "    i += 1"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Saturday\n",
            "Sunday\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vYUno7tp9Cxi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "16e3d22f-df6b-4539-daf6-12d7b00cfbcb"
      },
      "source": [
        "i = 0\n",
        "while i < len(weekend):\n",
        "    print(weekend[i])\n",
        "    i += 1"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Saturday\n",
            "Sunday\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4BEUqVxN9F2A",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "68f97e15-fd3b-4074-a6fa-a5f27a718880"
      },
      "source": [
        "i = 0\n",
        "while i < len(weekdays):\n",
        "    print(weekdays[i])\n",
        "    i += 1"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Monday\n",
            "Tuesday\n",
            "Wednesday\n",
            "Thursday\n",
            "Friday\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CFoljRD29Ic8",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "8dfd7312-b0ae-481e-86df-b55cecaef9e0"
      },
      "source": [
        "print(weekdays[-1])\n",
        "print(weekdays[-2])\n",
        "print(weekdays[-3])\n",
        "print(weekdays[-4])\n",
        "print(weekdays[-5])"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Friday\n",
            "Thursday\n",
            "Wednesday\n",
            "Tuesday\n",
            "Monday\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EOupnml19MMq",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "a6d67aa9-c94b-47ac-aeaf-53a10645bf10"
      },
      "source": [
        "i = -1\n",
        "while i >= -5:\n",
        "    print(weekdays[i])\n",
        "    i -= 1"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Friday\n",
            "Thursday\n",
            "Wednesday\n",
            "Tuesday\n",
            "Monday\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NejMwofT9P0b",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "120ea4af-6f93-487d-a053-27a6091c7169"
      },
      "source": [
        "weekdays"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F4hGorp89R-S",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d984196d-1e6a-48b7-e8ca-0742799669b0"
      },
      "source": [
        "weekdays[0:3:1]"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Monday', 'Tuesday', 'Wednesday']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LyhHNuCD9UWF",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "df1c0d4a-ef91-455d-e694-e8a373609494"
      },
      "source": [
        "weekdays[0:5:2]"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Monday', 'Wednesday', 'Friday']"
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
        "id": "4BBW7ZKR9WyL",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "93d13bab-2bc4-426f-99b5-92ce2eee5990"
      },
      "source": [
        "weekdays[::2]"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Monday', 'Wednesday', 'Friday']"
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