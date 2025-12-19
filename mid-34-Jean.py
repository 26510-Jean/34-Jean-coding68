{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOFLbZ2w9NJ08UtjHwnFIFO",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/26510-Jean/34-Jean-coding68/blob/main/mid-34-Jean.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "oPg8JvDrzX1V"
      },
      "outputs": [],
      "source": [
        "weight = float(input(\"กรอกน้ำหนัก (kg): \"))\n",
        "height_cm = float(input(\"กรอกส่วนสูง (cm): \"))\n",
        "\n",
        "height_m = height_cm / 100\n",
        "bmi = weight / (height_m **weight)\n",
        "\n",
        "print(\"ค่า BMI ของคุณคือ: {bmi:.2f}\")\n",
        "if bmi >= 25:\n",
        "    print(\"ผลลัพธ์: ควรควบคุมน้ำหนัก\")\n",
        "else:\n",
        "    print(\"ผลลัพธ์: สุขภาพดี\")"
      ]
    }
  ]
}