{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "3300c6f1-b704-4861-bf13-e57f7f7a15da",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            " Scalar Academy\n"
          ]
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Hello Scalar Academy\n"
          ]
        }
      ],
      "source": [
        "def main():\n",
        "    x = input()\n",
        "    print(\"Hello \" + x)\n",
        "    return 0\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "id": "a65afd62",
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "5\n",
            "-1\n",
            "6\n",
            "0\n",
            "0.6666666666666666\n",
            "2\n",
            "8\n"
          ]
        }
      ],
      "source": [
        "def main():\n",
        "    A = int(input())\n",
        "    B = int(input())\n",
        "    print(A+B)\n",
        "    print(A-B)\n",
        "    print(A*B)\n",
        "    print(A//B) # int div\n",
        "    print(A/B)  # float div\n",
        "    print(A%B)\n",
        "    print(A**B)\n",
        "    return 0\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "9a483002",
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Yess it is even\n"
          ]
        }
      ],
      "source": [
        "def odd_even(x) :\n",
        "    x = x%2\n",
        "    if x == 0 :\n",
        "        print(\"Yess it is even\")\n",
        "    else :\n",
        "        print(\"Nope it is odd\")\n",
        "\n",
        "odd_even(12)\n",
        "print(\"--- IGNORE ---\")"
      ]
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
      "version": "3.13.7"
    },
    "widgets": {
      "application/vnd.jupyter.widget-state+json": {
        "state": {},
        "version_major": 2,
        "version_minor": 0
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
