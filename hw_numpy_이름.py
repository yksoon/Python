{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. random.randint()를 사용하여 array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])를 출력하세요."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. np.random.rand()를 이용해서 5개의 난수를 생성하고 형변환을 통해서 0보다 큰 정수로 출력하세요."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. arange, zeros, ones를 이용해서 1차원 배열, 2차원 배열(3,3) 을 각각 생성하세요."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2 3 4 5 6 7 8]\n",
      "[[0 0 0]\n",
      " [0 0 0]\n",
      " [0 0 0]]\n",
      "(3, 3)\n",
      "[[1 1 1]\n",
      " [1 1 1]\n",
      " [1 1 1]]\n",
      "(3, 3)\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "list1 = np.arange(9)\n",
    "print(list1)\n",
    "list2 = np.zeros((3,3), dtype=\"int32\")\n",
    "print(list2)\n",
    "print(list2.shape)\n",
    "list3 = np.ones((3,3), dtype=\"int32\")\n",
    "print(list3)\n",
    "print(list3.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. np.random.randint()를 활용 (4,3) 배열 mt1 을 생성하세요"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5 5 1]\n",
      " [4 1 2]\n",
      " [8 1 1]\n",
      " [1 9 4]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "mt1 = np.random.randint(1,10, size=(4,3))\n",
    "print(mt1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. mt1을 2x6 행렬로 변환 mt2로 출력하세요."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5 5 1 4 1 2]\n",
      " [8 1 1 1 9 4]]\n"
     ]
    }
   ],
   "source": [
    "mt2 = mt1.reshape(2,6)\n",
    "print(mt2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. mt2를 1차원 배열로 변환 후 mt3로 출력하세요."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5 5 1 4 1 2 8 1 1 1 9 4]\n"
     ]
    }
   ],
   "source": [
    "mt3 = mt2.reshape(-1)\n",
    "print(mt3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. arange() 함수를 이용해서  0 ~ 29 정수 배열을 생성하고 2 X 5 X 3 3차원 배열로 변환하세요. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 0  1  2]\n",
      "  [ 3  4  5]\n",
      "  [ 6  7  8]\n",
      "  [ 9 10 11]\n",
      "  [12 13 14]]\n",
      "\n",
      " [[15 16 17]\n",
      "  [18 19 20]\n",
      "  [21 22 23]\n",
      "  [24 25 26]\n",
      "  [27 28 29]]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "array1 = np.arange(30)\n",
    "array3d = array1.reshape((2,5,3))\n",
    "print(array3d)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. 1 ~ 12 연속된 정수 배열을 생성하고 2 X 3 X 2 3차원 배열로 변환 후 list로 출력하세요. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 1  2]\n",
      "  [ 3  4]\n",
      "  [ 5  6]]\n",
      "\n",
      " [[ 7  8]\n",
      "  [ 9 10]\n",
      "  [11 12]]]\n"
     ]
    }
   ],
   "source": [
    "array2 = np.arange(1, 13)\n",
    "array3d2 = array2.reshape((2,3,2))\n",
    "print(array3d2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. 0 ~ 29 연속 정수 배열을 생성하고 (10,3) 행렬로 변환 후 인덱싱으로 다음을 출력하세요.\n",
    "- 12\n",
    "- [24,25,26]\n",
    "- 3번째 열 \n",
    "- 2번째 ~ 5번째 행\n",
    "- [10,13,16]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n",
      "\n",
      "[24 25 26]\n",
      "\n",
      "3번째 열 : \n",
      " [6 7 8]\n",
      "\n",
      "2번째 ~ 5번째 행 : \n",
      " [[ 3  4  5]\n",
      " [ 6  7  8]\n",
      " [ 9 10 11]\n",
      " [12 13 14]\n",
      " [15 16 17]]\n",
      "\n",
      "[10 13 16]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "list1 = np.arange(30)\n",
    "list2 = list1.reshape(10,3)\n",
    "# print(list2)\n",
    "print(list2[4,0])\n",
    "print()\n",
    "print(list2[8])\n",
    "print()\n",
    "print(\"3번째 열 : \\n\", list2[2])\n",
    "print()\n",
    "print(\"2번째 ~ 5번째 행 : \\n\", list2[1:6])\n",
    "print()\n",
    "print(list2[3:6, 1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. 5 ~ 20 연속 정수 배열을 생성하고 불린 인덱싱을 이용하여 짝수만 출력하세요.\n",
    "#### Q. 동일 배열에서 12보다 큰 정수만 출력하세요."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. random.randint()를 이용해서 10개의 배열을 a1으로 생성후 정렬하세요(내림차순)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. 1 ~ 21 정수를 랜덤하게 (3,3) 행렬로 생성 후 row, column 방향으로 각각 정렬하세요."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. 10에서 20사이의 정수로 구성된 (5,3) 행열을 np.random을 이용해서 mt1으로 생성하세요."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. mt1 행렬을 전치 후 mt2로 출력하세요."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. 6개의 원소로 구성되는 배열을 np.random을 활용하여 생성 mt1으로 출력하세요."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. 행벡터 mt1을 전치하여 열벡터로 변환하세요."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. 배열 matrix를 broadcasting을 이용하여 다음 배열을 출력하는 연산을 수행하세요. \n",
    "array([[101, 202, 303],\\\n",
    "       [104, 205, 306],\\\n",
    "       [107, 208, 309]])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. (3,3) 2차원 배열을 np.random으로 생성하여 mt1으로 저장하고 차원을 구하세요."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Q. 아래 두개의 행렬에 대한 덧셈, 뺄셈, 곱셈을 수행하세요"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
