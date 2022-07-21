{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8aaf5de4",
   "metadata": {},
   "source": [
    "## 문제정의\n",
    "- 데이터 전처리 및 시각화 방법에 대해 학습"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f46f8038",
   "metadata": {},
   "source": [
    "## 데이터 수집"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "acce7331",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# index_col : 인덱스 컬럼을 설정\n",
    "train = pd.read_csv(\"data/titanic_train.csv\", index_col = \"PassengerId\")\n",
    "test = pd.read_csv(\"data/titanic_test.csv\", index_col = \"PassengerId\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ff3cc9b3",
   "metadata": {},
   "source": [
    "## 탐색적 데이터 분석 및 전처리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "46c15b22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(891, 11)\n",
      "(418, 10)\n"
     ]
    }
   ],
   "source": [
    "print(train.shape)\n",
    "print(test.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a6ddc4c",
   "metadata": {},
   "source": [
    "- 분석 feature : Pclass, Age, Name, SibSp, Parch, Fare, Ticket, Cabin, Embarked\n",
    "- 예측 target label : Survived\n",
    "- feature\n",
    "<table border=0 width=700>\n",
    "  <tr><th>feature<th width=200>의미<th width=300>설명<th> 타입\n",
    "  <tr><td>Survivied<td>생존여부<td>target 라벨 (0 : 사망, 1 : 생존)<td>integer\n",
    "  <tr><td>Pclass<td>티켓의 클래스<td>1 = 1등석, 2 = 2등석, 3 = 3등석<td>integer\n",
    "  <tr><td>Name<td>이름<td>호칭과 이름으로 구성<td>string\n",
    "  <tr><td>Sex<td>성별<td>male, female로 구분<td>string\n",
    "  <tr><td>Age<td>나이<td>0-80세<td>integer\n",
    "  <tr><td>SibSp<td>함께 탑승한 형제와 배우자의 수<td><td>integer\n",
    "  <tr><td>Parch<td>함께 탑승한 부모, 아이의 수<td><td>integer\n",
    "  <tr><td>Ticket<td>티켓 번호<td>alphabat + integer<td>string\n",
    "  <tr><td>Fare<td>탑승료<td><td>float\n",
    "  <tr><td>Cabin<td>객실 번호<td>alphabat + integer<td>string\n",
    "  <tr><td>Embarked<td>탑승 항구<td>C = Cherbourg, Q = Queenstown, S = Southampton<td>string\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "77fa90b1",
   "metadata": {},
   "source": [
    "### 탐석적 데이터 분석\n",
    "- 데이터 이해를 이해하자\n",
    "- 결측치(컬럼에 값이 없는 데이터), 이상치(다른 값들과 차이가 큰 값), 오류가 있는지 확인\n",
    "- 기술통계\n",
    "- 상관관계\n",
    "- 시각화"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6397435",
   "metadata": {},
   "source": [
    "### 결측치 확인\n",
    "- info(), describe(), isnull()과 sum() 함수 등을 이용"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b3345d25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 891 entries, 1 to 891\n",
      "Data columns (total 11 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   Survived  891 non-null    int64  \n",
      " 1   Pclass    891 non-null    int64  \n",
      " 2   Name      891 non-null    object \n",
      " 3   Sex       891 non-null    object \n",
      " 4   Age       714 non-null    float64\n",
      " 5   SibSp     891 non-null    int64  \n",
      " 6   Parch     891 non-null    int64  \n",
      " 7   Ticket    891 non-null    object \n",
      " 8   Fare      891 non-null    float64\n",
      " 9   Cabin     204 non-null    object \n",
      " 10  Embarked  889 non-null    object \n",
      "dtypes: float64(2), int64(4), object(5)\n",
      "memory usage: 83.5+ KB\n"
     ]
    }
   ],
   "source": [
    "# 훈련 데이터의 결측치 - Age, Cabin, Embarked\n",
    "train.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8d141ecd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 418 entries, 892 to 1309\n",
      "Data columns (total 10 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   Pclass    418 non-null    int64  \n",
      " 1   Name      418 non-null    object \n",
      " 2   Sex       418 non-null    object \n",
      " 3   Age       332 non-null    float64\n",
      " 4   SibSp     418 non-null    int64  \n",
      " 5   Parch     418 non-null    int64  \n",
      " 6   Ticket    418 non-null    object \n",
      " 7   Fare      417 non-null    float64\n",
      " 8   Cabin     91 non-null     object \n",
      " 9   Embarked  418 non-null    object \n",
      "dtypes: float64(2), int64(3), object(5)\n",
      "memory usage: 35.9+ KB\n"
     ]
    }
   ],
   "source": [
    "# 테스트 데이터의 결측치 - Age, Fare, Cabin\n",
    "test.info()\n",
    "\n",
    "# Age, Fare, Cabin에 결측치가 존재"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c12a72d8",
   "metadata": {},
   "source": [
    "- 결측치를 채우는 방법\n",
    "  - 수치형인 경우\n",
    "    - 기술통계(평균, 중간값)\n",
    "    - 결측치가 적은 경우 : 전체 평균이나 중간값을 대입\n",
    "    - 결측치가 많은 경우 : 결측치가 있는 데이터의 다른 컬럼과 같은 값을 갖는 데이터의 결측치 통계를 사용\n",
    "  - 범주형인 경우\n",
    "    - 결측치가 적은 경우 : 데이터 수가 가장 많은 클래스로 할당-> 기존 데이터가 결측치가 있는 데이터에 의해 영향을 덜 받기 때문에)\n",
    "    - 결측치가 많은 경우 : 데이터 수가 가장 많은 클래스로 할당 -> 편향이 됨 -> 기존 데이터의 개수 비율만큼 랜덤으로 할당"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0339f208",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Survived      0\n",
       "Pclass        0\n",
       "Name          0\n",
       "Sex           0\n",
       "Age         177\n",
       "SibSp         0\n",
       "Parch         0\n",
       "Ticket        0\n",
       "Fare          0\n",
       "Cabin       687\n",
       "Embarked      2\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 결측치 개수 확인\n",
    "train.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "13af3794",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pclass        0\n",
       "Name          0\n",
       "Sex           0\n",
       "Age          86\n",
       "SibSp         0\n",
       "Parch         0\n",
       "Ticket        0\n",
       "Fare          1\n",
       "Cabin       327\n",
       "Embarked      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dd175a6e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>714.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.383838</td>\n",
       "      <td>2.308642</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>0.523008</td>\n",
       "      <td>0.381594</td>\n",
       "      <td>32.204208</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.486592</td>\n",
       "      <td>0.836071</td>\n",
       "      <td>14.526497</td>\n",
       "      <td>1.102743</td>\n",
       "      <td>0.806057</td>\n",
       "      <td>49.693429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.420000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>20.125000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.910400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>512.329200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Survived      Pclass         Age       SibSp       Parch        Fare\n",
       "count  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000\n",
       "mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208\n",
       "std      0.486592    0.836071   14.526497    1.102743    0.806057   49.693429\n",
       "min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000\n",
       "25%      0.000000    2.000000   20.125000    0.000000    0.000000    7.910400\n",
       "50%      0.000000    3.000000   28.000000    0.000000    0.000000   14.454200\n",
       "75%      1.000000    3.000000   38.000000    1.000000    0.000000   31.000000\n",
       "max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a89f9feb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>418.000000</td>\n",
       "      <td>332.000000</td>\n",
       "      <td>418.000000</td>\n",
       "      <td>418.000000</td>\n",
       "      <td>417.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2.265550</td>\n",
       "      <td>30.272590</td>\n",
       "      <td>0.447368</td>\n",
       "      <td>0.392344</td>\n",
       "      <td>35.627188</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.841838</td>\n",
       "      <td>14.181209</td>\n",
       "      <td>0.896760</td>\n",
       "      <td>0.981429</td>\n",
       "      <td>55.907576</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.170000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.895800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>39.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>76.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>512.329200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Pclass         Age       SibSp       Parch        Fare\n",
       "count  418.000000  332.000000  418.000000  418.000000  417.000000\n",
       "mean     2.265550   30.272590    0.447368    0.392344   35.627188\n",
       "std      0.841838   14.181209    0.896760    0.981429   55.907576\n",
       "min      1.000000    0.170000    0.000000    0.000000    0.000000\n",
       "25%      1.000000   21.000000    0.000000    0.000000    7.895800\n",
       "50%      3.000000   27.000000    0.000000    0.000000   14.454200\n",
       "75%      3.000000   39.000000    1.000000    0.000000   31.500000\n",
       "max      3.000000   76.000000    8.000000    9.000000  512.329200"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9d5d5f32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pclass</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.629630</td>\n",
       "      <td>38.233441</td>\n",
       "      <td>0.416667</td>\n",
       "      <td>0.356481</td>\n",
       "      <td>84.154687</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.472826</td>\n",
       "      <td>29.877630</td>\n",
       "      <td>0.402174</td>\n",
       "      <td>0.380435</td>\n",
       "      <td>20.662183</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.242363</td>\n",
       "      <td>25.140620</td>\n",
       "      <td>0.615071</td>\n",
       "      <td>0.393075</td>\n",
       "      <td>13.675550</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Survived        Age     SibSp     Parch       Fare\n",
       "Pclass                                                    \n",
       "1       0.629630  38.233441  0.416667  0.356481  84.154687\n",
       "2       0.472826  29.877630  0.402174  0.380435  20.662183\n",
       "3       0.242363  25.140620  0.615071  0.393075  13.675550"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 등급별(Pclass) 통계 (평균)\n",
    "# groupby() : 원하는 컬럼을 중심으로 그룹핑해주는 함수\n",
    "# Pclass 컬럼의 클래스별로 각 컬럼의 평균을 계산\n",
    "train.groupby(\"Pclass\").mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "84c9e7b8",
   "metadata": {},
   "source": [
    "- 1등실 생존율이 높았다\n",
    "- 나이를 보면 3등실에 나이가 적은 승객이 많았다\n",
    "- 1등실일수록 가족수가 적었다. 3등실일수록 가족수가 많았다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dfeb235d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pclass</th>\n",
       "      <th>Survived</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">1</th>\n",
       "      <th>0</th>\n",
       "      <td>43.695312</td>\n",
       "      <td>0.287500</td>\n",
       "      <td>0.300000</td>\n",
       "      <td>64.684007</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>35.368197</td>\n",
       "      <td>0.492647</td>\n",
       "      <td>0.389706</td>\n",
       "      <td>95.608029</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">2</th>\n",
       "      <th>0</th>\n",
       "      <td>33.544444</td>\n",
       "      <td>0.319588</td>\n",
       "      <td>0.144330</td>\n",
       "      <td>19.412328</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>25.901566</td>\n",
       "      <td>0.494253</td>\n",
       "      <td>0.643678</td>\n",
       "      <td>22.055700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">3</th>\n",
       "      <th>0</th>\n",
       "      <td>26.555556</td>\n",
       "      <td>0.672043</td>\n",
       "      <td>0.384409</td>\n",
       "      <td>13.669364</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>20.646118</td>\n",
       "      <td>0.436975</td>\n",
       "      <td>0.420168</td>\n",
       "      <td>13.694887</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Age     SibSp     Parch       Fare\n",
       "Pclass Survived                                          \n",
       "1      0         43.695312  0.287500  0.300000  64.684007\n",
       "       1         35.368197  0.492647  0.389706  95.608029\n",
       "2      0         33.544444  0.319588  0.144330  19.412328\n",
       "       1         25.901566  0.494253  0.643678  22.055700\n",
       "3      0         26.555556  0.672043  0.384409  13.669364\n",
       "       1         20.646118  0.436975  0.420168  13.694887"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.groupby([\"Pclass\", \"Survived\"]).mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "804a9bcd",
   "metadata": {},
   "source": [
    "- 3등실 승객의 사망/생존자의 요금은 비슷하다\n",
    "- 1등실 승객의 사망/생존자의 요금은 생존자의 요금이 더 비쌌다\n",
    "- 같은 클래스에서는, 나이가 어릴수록 생존이 높았다"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1894577f",
   "metadata": {},
   "source": [
    "### Age 결측치 채우기\n",
    "- 결측치가 있는 데이터의 다른 컬럼의 값과 같은 데이터의 평균값을 사용해서 결측치를 채움\n",
    "\n",
    "- 그럼 어떤 컬럼을 참조할까요?\n",
    "  - 결측치가 있는 컬럼(Age)와 상관관게가 높은 컬럼 선택(범주형)\n",
    "\n",
    "- 피벗 테이블을 활용\n",
    "- apply()을 이용하여 전체 데이터에 결측치를 채움\n",
    "  - 데이터프레임의 데이터를 분리해서 원하는 처리를 수행한 후 다시 병합하는 함수\n",
    "  - -->재구조화 함수(reconstruct function)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a55f8af1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Survived</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.338481</td>\n",
       "      <td>-0.077221</td>\n",
       "      <td>-0.035322</td>\n",
       "      <td>0.081629</td>\n",
       "      <td>0.257307</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pclass</th>\n",
       "      <td>-0.338481</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.369226</td>\n",
       "      <td>0.083081</td>\n",
       "      <td>0.018443</td>\n",
       "      <td>-0.549500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Age</th>\n",
       "      <td>-0.077221</td>\n",
       "      <td>-0.369226</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.308247</td>\n",
       "      <td>-0.189119</td>\n",
       "      <td>0.096067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SibSp</th>\n",
       "      <td>-0.035322</td>\n",
       "      <td>0.083081</td>\n",
       "      <td>-0.308247</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.414838</td>\n",
       "      <td>0.159651</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Parch</th>\n",
       "      <td>0.081629</td>\n",
       "      <td>0.018443</td>\n",
       "      <td>-0.189119</td>\n",
       "      <td>0.414838</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.216225</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fare</th>\n",
       "      <td>0.257307</td>\n",
       "      <td>-0.549500</td>\n",
       "      <td>0.096067</td>\n",
       "      <td>0.159651</td>\n",
       "      <td>0.216225</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Survived    Pclass       Age     SibSp     Parch      Fare\n",
       "Survived  1.000000 -0.338481 -0.077221 -0.035322  0.081629  0.257307\n",
       "Pclass   -0.338481  1.000000 -0.369226  0.083081  0.018443 -0.549500\n",
       "Age      -0.077221 -0.369226  1.000000 -0.308247 -0.189119  0.096067\n",
       "SibSp    -0.035322  0.083081 -0.308247  1.000000  0.414838  0.159651\n",
       "Parch     0.081629  0.018443 -0.189119  0.414838  1.000000  0.216225\n",
       "Fare      0.257307 -0.549500  0.096067  0.159651  0.216225  1.000000"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Age 컬럼과 상관관계가 높은 컬럼 찾기\n",
    "train.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "857d22ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">1</th>\n",
       "      <th>female</th>\n",
       "      <td>34.611765</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>male</th>\n",
       "      <td>41.281386</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">2</th>\n",
       "      <th>female</th>\n",
       "      <td>28.722973</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>male</th>\n",
       "      <td>30.740707</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">3</th>\n",
       "      <th>female</th>\n",
       "      <td>21.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>male</th>\n",
       "      <td>26.507589</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Age\n",
       "Pclass Sex              \n",
       "1      female  34.611765\n",
       "       male    41.281386\n",
       "2      female  28.722973\n",
       "       male    30.740707\n",
       "3      female  21.750000\n",
       "       male    26.507589"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 피벗 테이블 생성\n",
    "# 결측치를 채울 컬럼\n",
    "# index : 참고할 컬럼 목록 리스트\n",
    "# aggfunc : 사용할 수학 도구(평균, 중간값)\n",
    "pt1 = train.pivot_table(values=\"Age\",\n",
    "                       index=[\"Pclass\",\"Sex\"],\n",
    "                       aggfunc = \"mean\")\n",
    "pt1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "53dbe42e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Age    41.281386\n",
       "Name: (1, male), dtype: float64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 피벗 테이블에 접근하는 방법\n",
    "pt1.loc[1,\"male\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6b987686",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "# Age 컬럼의 결측치를 채우는 함수\n",
    "def fill_age(row):\n",
    "    # 한 줄 데이터에서 Age 컬럼이 결측치라면\n",
    "    if np.isnan(row[\"Age\"]):\n",
    "        # 피벗 테이블을 참조(같은 Pclass와 Sex인 값을 반환)\n",
    "        return pt1.loc[row[\"Pclass\"], row['Sex']]\n",
    "    # 결측치가 아닌 경우\n",
    "    else:\n",
    "        return row[\"Age\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "aa6ce3b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# axis=1 -> 한 줄씩 넘긴다\n",
    "# astype(\"int64\") : 나이는 실수가 없으니 정수로 변환\n",
    "train[\"Age\"] = train.apply(fill_age, axis=1).astype(\"int64\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7eccf227",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 891 entries, 1 to 891\n",
      "Data columns (total 11 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   Survived  891 non-null    int64  \n",
      " 1   Pclass    891 non-null    int64  \n",
      " 2   Name      891 non-null    object \n",
      " 3   Sex       891 non-null    object \n",
      " 4   Age       891 non-null    int64  \n",
      " 5   SibSp     891 non-null    int64  \n",
      " 6   Parch     891 non-null    int64  \n",
      " 7   Ticket    891 non-null    object \n",
      " 8   Fare      891 non-null    float64\n",
      " 9   Cabin     204 non-null    object \n",
      " 10  Embarked  889 non-null    object \n",
      "dtypes: float64(1), int64(5), object(5)\n",
      "memory usage: 83.5+ KB\n"
     ]
    }
   ],
   "source": [
    "train.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7ba8df9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "test[\"Age\"] = test.apply(fill_age, axis=1).astype(\"int64\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5bc1c46b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 418 entries, 892 to 1309\n",
      "Data columns (total 10 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   Pclass    418 non-null    int64  \n",
      " 1   Name      418 non-null    object \n",
      " 2   Sex       418 non-null    object \n",
      " 3   Age       418 non-null    int64  \n",
      " 4   SibSp     418 non-null    int64  \n",
      " 5   Parch     418 non-null    int64  \n",
      " 6   Ticket    418 non-null    object \n",
      " 7   Fare      417 non-null    float64\n",
      " 8   Cabin     91 non-null     object \n",
      " 9   Embarked  418 non-null    object \n",
      "dtypes: float64(1), int64(4), object(5)\n",
      "memory usage: 35.9+ KB\n"
     ]
    }
   ],
   "source": [
    "test.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b8e3d92",
   "metadata": {},
   "source": [
    "### train 데이터의 Embarked 결측치 채우기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7e05292f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "S    644\n",
       "C    168\n",
       "Q     77\n",
       "Name: Embarked, dtype: int64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 가장 많은 데이터 수를 갖는 클래스로 결측치를 할당 -> S\n",
    "train[\"Embarked\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "59225bae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Embarked 컬럼이 결측치인 값을 S로 채운다\n",
    "train['Embarked'] = train['Embarked'].fillna('S')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1bfcd4b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 891 entries, 1 to 891\n",
      "Data columns (total 11 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   Survived  891 non-null    int64  \n",
      " 1   Pclass    891 non-null    int64  \n",
      " 2   Name      891 non-null    object \n",
      " 3   Sex       891 non-null    object \n",
      " 4   Age       891 non-null    int64  \n",
      " 5   SibSp     891 non-null    int64  \n",
      " 6   Parch     891 non-null    int64  \n",
      " 7   Ticket    891 non-null    object \n",
      " 8   Fare      891 non-null    float64\n",
      " 9   Cabin     204 non-null    object \n",
      " 10  Embarked  891 non-null    object \n",
      "dtypes: float64(1), int64(5), object(5)\n",
      "memory usage: 83.5+ KB\n"
     ]
    }
   ],
   "source": [
    "train.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4acdf03d",
   "metadata": {},
   "source": [
    "### test 데이터의 Fare 결측치 채우기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "92a0a75c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1044</th>\n",
       "      <td>3</td>\n",
       "      <td>Storey, Mr. Thomas</td>\n",
       "      <td>male</td>\n",
       "      <td>60</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3701</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Pclass                Name   Sex  Age  SibSp  Parch Ticket  Fare  \\\n",
       "PassengerId                                                                     \n",
       "1044              3  Storey, Mr. Thomas  male   60      0      0   3701   NaN   \n",
       "\n",
       "            Cabin Embarked  \n",
       "PassengerId                 \n",
       "1044          NaN        S  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 결측치가 있는 데이터를 확인\n",
    "test[test[\"Fare\"].isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "516d38c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pclass</th>\n",
       "      <th>Embarked</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">1</th>\n",
       "      <th>C</th>\n",
       "      <td>110.073511</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Q</th>\n",
       "      <td>90.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S</th>\n",
       "      <td>76.677504</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">2</th>\n",
       "      <th>C</th>\n",
       "      <td>20.120445</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Q</th>\n",
       "      <td>11.273950</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S</th>\n",
       "      <td>23.056090</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">3</th>\n",
       "      <th>C</th>\n",
       "      <td>10.658700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Q</th>\n",
       "      <td>8.998985</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S</th>\n",
       "      <td>13.913030</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Fare\n",
       "Pclass Embarked            \n",
       "1      C         110.073511\n",
       "       Q          90.000000\n",
       "       S          76.677504\n",
       "2      C          20.120445\n",
       "       Q          11.273950\n",
       "       S          23.056090\n",
       "3      C          10.658700\n",
       "       Q           8.998985\n",
       "       S          13.913030"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pt2 = test.pivot_table(values=\"Fare\",\n",
    "                       index=[\"Pclass\",\"Embarked\"],\n",
    "                       aggfunc = \"mean\")\n",
    "pt2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "59b605af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pclass</th>\n",
       "      <th>Embarked</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">1</th>\n",
       "      <th>C</th>\n",
       "      <td>104.718529</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Q</th>\n",
       "      <td>90.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S</th>\n",
       "      <td>70.514244</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">2</th>\n",
       "      <th>C</th>\n",
       "      <td>25.358335</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Q</th>\n",
       "      <td>12.350000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S</th>\n",
       "      <td>20.327439</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">3</th>\n",
       "      <th>C</th>\n",
       "      <td>11.214083</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Q</th>\n",
       "      <td>11.183393</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S</th>\n",
       "      <td>14.644083</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Fare\n",
       "Pclass Embarked            \n",
       "1      C         104.718529\n",
       "       Q          90.000000\n",
       "       S          70.514244\n",
       "2      C          25.358335\n",
       "       Q          12.350000\n",
       "       S          20.327439\n",
       "3      C          11.214083\n",
       "       Q          11.183393\n",
       "       S          14.644083"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pt3 = train.pivot_table(values=\"Fare\",\n",
    "                       index=[\"Pclass\",\"Embarked\"],\n",
    "                       aggfunc = \"mean\")\n",
    "pt3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d24f80c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "test[\"Fare\"] = test[\"Fare\"].fillna(13.913030)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "96aac3e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 418 entries, 892 to 1309\n",
      "Data columns (total 10 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   Pclass    418 non-null    int64  \n",
      " 1   Name      418 non-null    object \n",
      " 2   Sex       418 non-null    object \n",
      " 3   Age       418 non-null    int64  \n",
      " 4   SibSp     418 non-null    int64  \n",
      " 5   Parch     418 non-null    int64  \n",
      " 6   Ticket    418 non-null    object \n",
      " 7   Fare      418 non-null    float64\n",
      " 8   Cabin     91 non-null     object \n",
      " 9   Embarked  418 non-null    object \n",
      "dtypes: float64(1), int64(4), object(5)\n",
      "memory usage: 35.9+ KB\n"
     ]
    }
   ],
   "source": [
    "test.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0c8e82f",
   "metadata": {},
   "source": [
    "### Cabin 결측치 채우기\n",
    "- 결측치가 실제 객실이 없는 승객이었을 가능성이 있으므로 원래 값에 중복되지 않는 영문자 채움\n",
    "- 원래 객실번호의 첫번째 영문자 추출"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "6d507ac8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([nan, 'C85', 'C123', 'E46', 'G6', 'C103', 'D56', 'A6',\n",
       "       'C23 C25 C27', 'B78', 'D33', 'B30', 'C52', 'B28', 'C83', 'F33',\n",
       "       'F G73', 'E31', 'A5', 'D10 D12', 'D26', 'C110', 'B58 B60', 'E101',\n",
       "       'F E69', 'D47', 'B86', 'F2', 'C2', 'E33', 'B19', 'A7', 'C49', 'F4',\n",
       "       'A32', 'B4', 'B80', 'A31', 'D36', 'D15', 'C93', 'C78', 'D35',\n",
       "       'C87', 'B77', 'E67', 'B94', 'C125', 'C99', 'C118', 'D7', 'A19',\n",
       "       'B49', 'D', 'C22 C26', 'C106', 'C65', 'E36', 'C54',\n",
       "       'B57 B59 B63 B66', 'C7', 'E34', 'C32', 'B18', 'C124', 'C91', 'E40',\n",
       "       'T', 'C128', 'D37', 'B35', 'E50', 'C82', 'B96 B98', 'E10', 'E44',\n",
       "       'A34', 'C104', 'C111', 'C92', 'E38', 'D21', 'E12', 'E63', 'A14',\n",
       "       'B37', 'C30', 'D20', 'B79', 'E25', 'D46', 'B73', 'C95', 'B38',\n",
       "       'B39', 'B22', 'C86', 'C70', 'A16', 'C101', 'C68', 'A10', 'E68',\n",
       "       'B41', 'A20', 'D19', 'D50', 'D9', 'A23', 'B50', 'A26', 'D48',\n",
       "       'E58', 'C126', 'B71', 'B51 B53 B55', 'D49', 'B5', 'B20', 'F G63',\n",
       "       'C62 C64', 'E24', 'C90', 'C45', 'E8', 'B101', 'D45', 'C46', 'D30',\n",
       "       'E121', 'D11', 'E77', 'F38', 'B3', 'D6', 'B82 B84', 'D17', 'A36',\n",
       "       'B102', 'B69', 'E49', 'C47', 'D28', 'E17', 'A24', 'C50', 'B42',\n",
       "       'C148'], dtype=object)"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train[\"Cabin\"].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "00ef0bb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 결측치를 M으로 채움\n",
    "train[\"Cabin\"] = train[\"Cabin\"].fillna(\"M\")\n",
    "test[\"Cabin\"] = test[\"Cabin\"].fillna(\"M\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a9b3f78d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 891 entries, 1 to 891\n",
      "Data columns (total 11 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   Survived  891 non-null    int64  \n",
      " 1   Pclass    891 non-null    int64  \n",
      " 2   Name      891 non-null    object \n",
      " 3   Sex       891 non-null    object \n",
      " 4   Age       891 non-null    int64  \n",
      " 5   SibSp     891 non-null    int64  \n",
      " 6   Parch     891 non-null    int64  \n",
      " 7   Ticket    891 non-null    object \n",
      " 8   Fare      891 non-null    float64\n",
      " 9   Cabin     891 non-null    object \n",
      " 10  Embarked  891 non-null    object \n",
      "dtypes: float64(1), int64(5), object(5)\n",
      "memory usage: 83.5+ KB\n"
     ]
    }
   ],
   "source": [
    "train.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4826b480",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 원래 객실번호의 첫번째 영문자 추출\n",
    "train[\"Cabin\"] = train[\"Cabin\"].str[0]\n",
    "test[\"Cabin\"] = test[\"Cabin\"].str[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "2741a4ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['M', 'C', 'E', 'G', 'D', 'A', 'B', 'F', 'T'], dtype=object)"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train[\"Cabin\"].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "177fc4dd",
   "metadata": {},
   "source": [
    "### 데이터 시각화하기\n",
    "- test데이터를 활용하지 않고 train데이터를 이용해서 시각화/탐색하는게 좋다."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2dc1d51c",
   "metadata": {},
   "source": [
    "#### 범주형 데이터 시각화\n",
    "- 빈도 기반의 bar chart를 많이 활용"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2daaced8",
   "metadata": {},
   "source": [
    "##### Cabin 시각화"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c34c44fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# matplotlib 기반의 데이터 시각화 라이브러리\n",
    "# https://seaborn.pydata.org/index.html\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "20789211",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Cabin', ylabel='count'>"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(data=train, # 사용할 데이터 지정\n",
    "             x='Cabin')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "8265cbd9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Cabin', ylabel='count'>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEICAYAAACwDehOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAW0klEQVR4nO3dfZBV9Z3n8fdXQDCiiUjjA4022ehswAdmeMhmXLOM7ojlZMHMisBslKw6pKJOkdrdSWCrEk2mmKUSJxvLmJ1QSUaMDy0Z15FYibvGWTM7iSPSDj6AOpCQkRZGHpw10YwPkO/+cQ8nV2jgDvbpc+l+v6q67j2/e87pT1+b/njOPQ+RmUiSBHBU3QEkSe3DUpAklSwFSVLJUpAklSwFSVLJUpAklSothYj4aUQ8HRHrImJtMTYmIh6KiI3F4wlN8y+NiE0R8XxEzKoymyRpf1HleQoR8VNgWmbubBr7AvByZi6PiCXACZn56YiYBNwNzABOBb4PnJmZew60/rFjx2ZXV1dl+SVpMOrp6dmZmR19vTZ8oMMAc4CZxfOVwCPAp4vx7sx8A9gcEZtoFMSjB1pRV1cXa9eurTSsJA02EfH3B3qt6s8UEvjfEdETEYuKsZMycxtA8TiuGB8PbGlatrcYkyQNkKq3FM7LzK0RMQ54KCKeO8i80cfYfvu2inJZBHDaaaf1T0pJElDxlkJmbi0etwP30dgd9FJEnAJQPG4vZu8FJjQt3gls7WOdKzJzWmZO6+joc5eYJOkwVbalEBHHAkdl5s+L5xcBnwdWAwuB5cXj/cUiq4G7IuJLND5oPgNYU1U+DV1vvfUWvb29vP7663VHecdGjRpFZ2cnI0aMqDuKBokqdx+dBNwXEXu/z12Z+WBEPA6sioirgReAuQCZuT4iVgEbgN3AdQc78kg6XL29vRx33HF0dXVR/H4ekTKTXbt20dvby8SJE+uOo0GislLIzJ8A5/Yxvgu48ADLLAOWVZVJAnj99deP+EIAiAhOPPFEduzYUXcUDSKe0awh6UgvhL0Gy8+h9mEpSJJKloIELFu2jMmTJ3POOecwZcoUHnvssXe8ztWrV7N8+fJ+SAejR4/ul/VIh1LHGc2VmfqHtx/2sj1fvLIfk+hI8uijj/LAAw/wxBNPMHLkSHbu3Mmbb77Z0rK7d+9m+PC+/xnNnj2b2bNn92dUqXJuKWjI27ZtG2PHjmXkyJEAjB07llNPPZWuri527mxctmvt2rXMnDkTgBtvvJFFixZx0UUXceWVV/KBD3yA9evXl+ubOXMmPT093HbbbVx//fW88sordHV18ctf/hKAX/ziF0yYMIG33nqLH//4x1x88cVMnTqV888/n+eea5zfuXnzZj74wQ8yffp0PvOZzwzgu6GhzlLQkHfRRRexZcsWzjzzTK699lp+8IMfHHKZnp4e7r//fu666y7mz5/PqlWrgEbBbN26lalTp5bzvvvd7+bcc88t1/ud73yHWbNmMWLECBYtWsQtt9xCT08PN910E9deey0Aixcv5hOf+ASPP/44J598cgU/tdQ3S0FD3ujRo+np6WHFihV0dHQwb948brvttoMuM3v2bI455hgALr/8cr797W8DsGrVKubOnbvf/PPmzeOee+4BoLu7m3nz5vHqq6/yox/9iLlz5zJlyhQ+/vGPs23bNgB++MMfsmDBAgCuuOKK/vpRpUMaVJ8pSIdr2LBhzJw5k5kzZ3L22WezcuVKhg8fXu7y2ffs52OPPbZ8Pn78eE488USeeuop7rnnHr72ta/tt/7Zs2ezdOlSXn75ZXp6erjgggt47bXXeM973sO6dev6zOThpqqDWwoa8p5//nk2btxYTq9bt47TTz+drq4uenp6ALj33nsPuo758+fzhS98gVdeeYWzzz57v9dHjx7NjBkzWLx4MR/+8IcZNmwYxx9/PBMnTiy3MjKTJ598EoDzzjuP7u5uAO68885++TmlVlgKGvJeffVVFi5cyKRJkzjnnHPYsGEDN954IzfccAOLFy/m/PPPZ9iwYQddx2WXXUZ3dzeXX375AeeZN28ed9xxB/PmzSvH7rzzTr7xjW9w7rnnMnnyZO6/v3EpsJtvvplbb72V6dOn88orr/TPDyq1oNI7r1Vt2rRp2XyTHQ9JVSueffZZ3v/+99cdo98Mtp9H1YuInsyc1tdrbilIkkqWgiSpZClIkkqWgiSpZClIkkqWgiSp5BnNUh/eyeHNfWnlkOcHH3yQxYsXs2fPHq655hqWLFnSrxmkVrilILWBPXv2cN111/G9732PDRs2cPfdd7Nhw4a6Y2kIshSkNrBmzRre97738d73vpejjz6a+fPnl2c3SwPJUpDawIsvvsiECRPK6c7OTl588cUaE2moshSkNtDX5Wa8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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(data=train, # 사용할 데이터 지정\n",
    "             x='Cabin', # x축에서 범주로 사용할 컬럼 지정\n",
    "             hue = 'Survived') # 각 범주를 분리할 컬럼 지정"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "36c91852",
   "metadata": {},
   "source": [
    "- B,D 같은 경우는 살아남기에 괜찮은 객실일 수 있다!\n",
    "- M 같은 경우는 죽은 사람들의 비율이 엄청 높다."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d5e175bc",
   "metadata": {},
   "source": [
    "##### Pclass 시각화"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a31b28c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Pclass', ylabel='count'>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEGCAYAAACKB4k+AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAXdElEQVR4nO3dfbAddZ3n8ffHkCGMwQdI0MCNJipMmQjEIsR1Wa0sWsCybtApIaFGxAUnjMJurJqdGrBKRXdTxTqo5eJDGQuHqEiIoptIjbjIio5PYC4bkAQpojBwIQNJUDQqD7l+94/bNNfkJrl5OPfc5LxfVadu9+/8fn2+zanKh193n+5UFZIkATyv2wVIksYPQ0GS1DIUJEktQ0GS1DIUJEmtQ7pdwL6YMmVKzZgxo9tlSNIBpb+/f3NVTR3pvQM6FGbMmMGaNWu6XYYkHVCS/MvO3vPwkSSpZShIklqGgiSpdUCfUxjJM888w8DAAE8++WS3S9lnkyZNoq+vj4kTJ3a7FEk94qALhYGBAQ4//HBmzJhBkm6Xs9eqii1btjAwMMDMmTO7XY6kHnHQHT568sknOfLIIw/oQABIwpFHHnlQzHgkHTgOulAADvhAeNbBsh+SDhwHZShIkvZOz4TC0qVLmT17NieccAJz5szhtttu2+dtrl69miuuuGI/VAeTJ0/eL9uRpH1x0J1oHsmPf/xjbrzxRu644w4OPfRQNm/ezNNPPz2qsdu2beOQQ0b+z7RgwQIWLFiwP0uVDkon/d0Xu13CHun/h3d2u4Su6YmZwsaNG5kyZQqHHnooAFOmTOHoo49mxowZbN68GYA1a9Ywf/58AC6//HIWL17Maaedxjvf+U5e97rXsW7dunZ78+fPp7+/n2uuuYZLLrmEJ554ghkzZvDHP/4RgN///vdMnz6dZ555hl/84hecccYZnHTSSbzhDW/g5z//OQD3338/r3/96zn55JP5wAc+MIb/NSRp53oiFE477TQeeughjjvuON773vfyve99b7dj+vv7WbVqFV/5yldYtGgRK1euBIYC5pFHHuGkk05q+77whS/kxBNPbLf7zW9+k9NPP52JEyeyePFirrrqKvr7+7nyyit573vfC8CSJUt4z3vew09/+lNe+tKXdmCvJWnP9UQoTJ48mf7+fpYtW8bUqVNZuHAh11xzzS7HLFiwgMMOOwyAc845h69+9asArFy5krPPPnuH/gsXLuT6668HYMWKFSxcuJCtW7fyox/9iLPPPps5c+Zw0UUXsXHjRgB++MMfcu655wJw3nnn7a9dlaR90hPnFAAmTJjA/PnzmT9/PscffzzLly/nkEMOaQ/5bP97gOc///nt8jHHHMORRx7JXXfdxfXXX8/nPve5Hba/YMECLrvsMh5//HH6+/s59dRT+d3vfseLXvQi1q5dO2JNXnIqabzpiZnCvffey3333deur127lpe//OXMmDGD/v5+AG644YZdbmPRokV89KMf5YknnuD444/f4f3Jkyczb948lixZwlve8hYmTJjAC17wAmbOnNnOMqqKO++8E4BTTjmFFStWAHDttdful/2UpH3VE6GwdetWzj//fGbNmsUJJ5zA+vXrufzyy/nQhz7EkiVLeMMb3sCECRN2uY23v/3trFixgnPOOWenfRYuXMiXv/xlFi5c2LZde+21XH311Zx44onMnj2bVatWAfDJT36ST3/605x88sk88cQT+2dHJWkfpaq6XcNemzt3bm3/kJ177rmHV7/61V2qaP872PZHvclLUseXJP1VNXek93pipiBJGp2OhUKSSUluT3JnknVJPty0X57k4SRrm9eZw8ZclmRDknuTnN6p2iRJI+vk1UdPAadW1dYkE4EfJPlW894nqurK4Z2TzAIWAbOBo4HvJDmuqgY7WKMkaZiOzRRqyNZmdWLz2tUJjLOAFVX1VFXdD2wA5nWqPknSjjp6TiHJhCRrgceAm6vq2bvQXZLkriRfSPLipu0Y4KFhwweatu23uTjJmiRrNm3a1MnyJanndDQUqmqwquYAfcC8JK8BPgu8EpgDbAQ+1nQf6ZdcO8wsqmpZVc2tqrlTp07tSN2S1KvG5BfNVfXrJLcCZww/l5Dk88CNzeoAMH3YsD7gkU7Us78vjxvt5Ws33XQTS5YsYXBwkHe/+91ceuml+7UOSdpXnbz6aGqSFzXLhwFvBn6eZNqwbm8D7m6WVwOLkhyaZCZwLHB7p+oba4ODg1x88cV861vfYv369Vx33XWsX7++22VJ0p/o5ExhGrA8yQSGwmdlVd2Y5EtJ5jB0aOgB4CKAqlqXZCWwHtgGXHwwXXl0++2386pXvYpXvOIVwNBtM1atWsWsWbO6XJkkPadjoVBVdwGvHaF9p7cEraqlwNJO1dRN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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(data=train, # 사용할 데이터 지정\n",
    "             x='Pclass', # x축에서 범주로 사용할 컬럼 지정\n",
    "             hue = 'Survived') # 각 범주를 분리할 컬럼 지정"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91f75a51",
   "metadata": {},
   "source": [
    "##### Cabin & Pclass 시각화"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "57c8414c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Cabin', ylabel='count'>"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(data=train, # 사용할 데이터 지정\n",
    "             x='Cabin', # x축에서 범주로 사용할 컬럼 지정\n",
    "             hue = 'Pclass') # 각 범주를 분리할 컬럼 지정"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c8645a37",
   "metadata": {},
   "source": [
    "- M에는 3등급이 많이 있어서 죽은사람의 비율이 높아보인 것 같다.\n",
    "- M이 생존여부 판단에는 도움이 덜 될 수 있겠다."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "889b82bc",
   "metadata": {},
   "source": [
    "#### 수치형 데이터 시각화\n",
    "- 구간을 나눠서 종합하는 히스토그램\n",
    "- 커널밀도 추정 그래프"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "677c0067",
   "metadata": {},
   "source": [
    "##### matplotlib hist 함수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "a4340afa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "8f4fb231",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(train['Age'], bins=10)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5c9b4ebd",
   "metadata": {},
   "source": [
    "##### seaborn histplot 함수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "5352c21b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Age', ylabel='Count'>"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data=train, x=train['Age'], bins=20, hue=\"Survived\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "137f6c24",
   "metadata": {},
   "source": [
    "- 20대 중~후반의 사람들이 죽은 비율이 높다.\n",
    "- 10살 미만의 사람들이 산 비율이 약간 높다."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dbc2b932",
   "metadata": {},
   "source": [
    "#### 커널밀도추정 그래프 시각화"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "f9dc8d76",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Age', ylabel='Density'>"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.kdeplot(data=train, x=\"Age\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "1127d4e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Fare', ylabel='Density'>"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 요금 데이터 시각화\n",
    "sns.kdeplot(data=train, x=train['Fare'], hue=\"Survived\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a0f6ec1",
   "metadata": {},
   "source": [
    "- 0~40달러 사이의 사람은 죽은 사람의 밀도가 높다.\n",
    "- 200달러 이상의 사람은 산 사람의 밀도가 아주 살짝 높다."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "599867b1",
   "metadata": {},
   "source": [
    "##### 바이올린플롯 그래프 시각화\n",
    "- 박스 + KDE 그래프"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "36e2e288",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Sex', ylabel='Age'>"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA3UAAAE9CAYAAACsmksIAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAABjaElEQVR4nO3dd3zU9eHH8dfncsll77ASpmyQJcMtiluLq66696zbumrVtiqt1ipqa92zrp8L0YoLQZmyRwYJhACyQxIyb35+f1yM2iIyknxzl/fz8eCR5Mb33lG4u/d9P8NYaxEREREREZHI5HI6gIiIiIiIiOw5lToREREREZEIplInIiIiIiISwVTqREREREREIphKnYiIiIiISARTqRMREREREYlgbqcD7Irs7Gzbo0cPp2OIiIiIiIg4Yv78+VuttTk7ui4iSl2PHj2YN2+e0zFEREREREQcYYwp+7nrNPxSREREREQkgqnUiYiIiIiIRDCVOhERERERkQgWEXPqREREREREfo7f72fdunU0NDQ4HWWvxcfHk5eXR2xs7C7fR6VOREREREQi2rp160hJSaFHjx4YY5yOs8estZSXl7Nu3Tp69uy5y/fT8EsREREREYloDQ0NZGVlRXShAzDGkJWVtdtnHFXqREREREQk4kV6ofvenvweKnUiIiIiIhKV7r//fgYNGsSQIUMYNmwYc+bM2etjTpo0iQkTJjRDOkhOTm6W42hOnYiIiIiIRJ1Zs2YxefJkFixYgMfjYevWrfh8vl26byAQwO3ecVUaP34848ePb86oe01n6kREREREJOps2LCB7OxsPB4PANnZ2XTp0oUePXqwdetWAObNm8fYsWMBuPfee7n88ss5+uijOf/88xkzZgzLly9vOt7YsWOZP38+L774Itdeey1VVVX06NGDUCgEQF1dHV27dsXv97Ny5UqOPfZY9ttvPw455BAKCwsBKC0t5YADDmDUqFHcfffdzfa7qtSJRLlgMMjVV1/FM88843QUERERkVZz9NFHs3btWvr27cvVV1/NtGnTfvE+8+fP54MPPuDf//43Z511Fm+99RYQLojr169nv/32a7ptWloaQ4cObTruhx9+yDHHHENsbCyXX345jz/+OPPnz+fhhx/m6quvBuD666/nqquu4ttvv6VTp07N9ruq1IlEOa/XS35+Aa+99prTUURERERaTXJyMvPnz+fpp58mJyeHM888kxdffHGn9xk/fjwJCQkAnHHGGbz99tsAvPXWW5x++un/c/szzzyTN998E4A33niDM888k5qaGmbOnMnpp5/OsGHDuOKKK9iwYQMAM2bM4OyzzwbgvPPOa65fVXPqREREREQkOsXExDB27FjGjh3Lvvvuy0svvYTb7W4aMvnfWwckJSU1fZ+bm0tWVhZLlizhzTff5F//+tf/HH/8+PHccccdbNu2jfnz53PEEUdQW1tLeno6ixYt2mGmllilU2fqREREREQk6hQVFVFcXNz086JFi+jevTs9evRg/vz5ALzzzjs7PcZZZ53FX//6V6qqqth3333/5/rk5GRGjx7N9ddfz4knnkhMTAypqan07Nmz6SyftZbFixcDcNBBB/HGG28ANOsoKpU6ERERERGJOjU1NVxwwQUMHDiQIUOGkJ+fz7333ss999zD9ddfzyGHHEJMTMxOj/HrX/+aN954gzPOOONnb3PmmWfy6quvcuaZZzZd9tprr/Hcc88xdOhQBg0axAcffADAY489xpNPPsmoUaOoqqpqnl8UMNbaZjtYSxk5cqSdN2+e0zFEIlJdXR3HH388AF9++SUulz7LERERkehSUFDAgAEDnI7RbHb0+xhj5ltrR+7o9np3J9KO1NXVOR1BRERERJqZSp1IO1JdXe10BBERERFpZip1Iu1Ic47dFhEREZG2QaVOpB1RqRMRERGJPip1Iu2ISp2IiIhI9FGpE2lHKioqnI4gIiIiIs1MpU6kHVGpExEREWk9n3zyCf369aN3795MmDChxR7H3WJHFpE2R6VORERE2qtrb7qVzVu3NdvxOmRn8sQjD/3s9cFgkGuuuYbPPvuMvLw8Ro0axfjx4xk4cGCzZfieSp1IO7JtW/M9kYmIiIhEks1bt7Gy42HNd8BN03Z69dy5c+nduze9evUC4KyzzuKDDz5okVKn4Zci7ci28q1ORxARERFpF7777ju6du3a9HNeXh7fffddizyWSp1IO1KhM3UiIiIircJa+z+XGWNa5LFU6kTaiViXpbJqO8Fg0OkoIiIiIlEvLy+PtWvXNv28bt06unTp0iKPpVIn0k6kxYUIWcv27dudjiIiIiIS9UaNGkVxcTGlpaX4fD7eeOMNxo8f3yKPpVIn0k6kxoaHAFRWVjobRERERKQdcLvd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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,5)) # 그래프의 가로, 세로 크기 설정\n",
    "sns.violinplot(data=train, # 사용할 데이터\n",
    "              x=\"Sex\",\n",
    "              y=\"Age\",\n",
    "              hue=\"Survived\",\n",
    "              split=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca6f0eb9",
   "metadata": {},
   "source": [
    "#### 텍스트 데이터\n",
    "- 비정형 데이터는 단어중심 시각화\n",
    "- wordcloud\n",
    "- 빈도기반의 시각화 활용가능"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a71a045",
   "metadata": {},
   "source": [
    "## 특성공학\n",
    "- feature에서 유의미한 컬럼을 추출하거나 병합하는 행위"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "d485aa79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',\n",
       "       'Fare', 'Cabin', 'Embarked'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd21b148",
   "metadata": {},
   "source": [
    "### 가족 컬럼을 만들어보자!\n",
    "- SibSp와 Parch를 병합하자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "16988347",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='SibSp', ylabel='count'>"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(data=train,\n",
    "              x=\"SibSp\",\n",
    "              hue=\"Survived\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "0b01ce73",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Parch', ylabel='count'>"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(data=train,\n",
    "              x=\"Parch\",\n",
    "              hue=\"Survived\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "c32d55ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Family', ylabel='count'>"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "train['Family'] = train[\"SibSp\"] + train['Parch']\n",
    "sns.countplot(data=train,\n",
    "              x=\"Family\",\n",
    "              hue=\"Survived\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cedce24b",
   "metadata": {},
   "source": [
    "#### Cut 함수를 이용한 Binning(수치->범주)\n",
    "- 사소한 관찰 오류를 줄여줄 수 있다.(모델의 단순화를 유도)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "3794ecd8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId\n",
       "1      Small\n",
       "2      Small\n",
       "3      Alone\n",
       "4      Small\n",
       "5      Alone\n",
       "       ...  \n",
       "887    Alone\n",
       "888    Alone\n",
       "889    Small\n",
       "890    Alone\n",
       "891    Alone\n",
       "Name: Family, Length: 891, dtype: category\n",
       "Categories (3, object): ['Alone' < 'Small' < 'Large']"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bins = [-1,0,3,20] # 데이터를 잘라낼 구간정보 설정\n",
    "labels = [\"Alone\", \"Small\", \"Large\"] # 구간별 범주 이름\n",
    "cut_result = pd.cut(x=train[\"Family\"], # 구간화할 데이터 설정\n",
    "                   bins = bins, # 잘라낼 구간정보 설정\n",
    "                   labels = labels) # 구간별 범주 이름 설정\n",
    "cut_result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "05c4402c",
   "metadata": {},
   "outputs": [],
   "source": [
    "train['Family_cat'] = cut_result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "6709ea44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Family_cat', ylabel='count'>"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(data=train,\n",
    "              x=\"Family_cat\",\n",
    "              hue=\"Survived\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "f6371eee",
   "metadata": {},
   "outputs": [],
   "source": [
    "test['Family'] = test[\"SibSp\"] + test['Parch']\n",
    "bins = [-1,0,3,20] # 데이터를 잘라낼 구간정보 설정\n",
    "labels = [\"Alone\", \"Small\", \"Large\"] # 구간별 범주 이름\n",
    "cut_result = pd.cut(x=test[\"Family\"], # 구간화할 데이터 설정\n",
    "                   bins = bins, # 잘라낼 구간정보 설정\n",
    "                   labels = labels) # 구간별 범주 이름 설정\n",
    "test['Family_cat'] = cut_result"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a77b6dd",
   "metadata": {},
   "source": [
    "### 비정형 데이터 다루기(Name)\n",
    "- 이름 중간에 호칭을 추출해서 사용해보자."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "14690420",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId\n",
       "1                                Braund, Mr. Owen Harris\n",
       "2      Cumings, Mrs. John Bradley (Florence Briggs Th...\n",
       "3                                 Heikkinen, Miss. Laina\n",
       "4           Futrelle, Mrs. Jacques Heath (Lily May Peel)\n",
       "5                               Allen, Mr. William Henry\n",
       "                             ...                        \n",
       "887                                Montvila, Rev. Juozas\n",
       "888                         Graham, Miss. Margaret Edith\n",
       "889             Johnston, Miss. Catherine Helen \"Carrie\"\n",
       "890                                Behr, Mr. Karl Howell\n",
       "891                                  Dooley, Mr. Patrick\n",
       "Name: Name, Length: 891, dtype: object"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['Name']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "2202adfc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def split_title(row):\n",
    "    return row.split(\",\")[1].split(\".\")[0].strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "58415354",
   "metadata": {},
   "outputs": [],
   "source": [
    "train[\"Title\"] = train[\"Name\"].apply(split_title)\n",
    "test[\"Title\"] = test[\"Name\"].apply(split_title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "6427e8cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Title', ylabel='count'>"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA3sAAAE9CAYAAACyU3u7AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAktklEQVR4nO3dfdhcdX0n/veHBAktAkKiAkGDilaQh5aAtVY3PkKtG2wrEK8q8NMua9EVd7ddpbtVxIstq253rQ+/StWKFQWsWpD6RFGsVSsmGkBAfmCxEKHyYMViKwJ+f3/MuWEId5JJMnPPnZPX67rua85858yZz/eeOWfO+zxNtdYCAABAv+ww7QIAAAAYP2EPAACgh4Q9AACAHhL2AAAAekjYAwAA6CFhDwAAoIcWTruArbF48eK2bNmyaZcBAAAwFWvWrLm9tbZktse26bC3bNmyrF69etplAAAATEVV/eOGHnMYJwAAQA8JewAAAD0k7AEAAPTQNn3OHgAAwIbcc889WbduXX7yk59Mu5SttmjRoixdujQ77rjjyM8R9gAAgF5at25dHv7wh2fZsmWpqmmXs8Vaa7njjjuybt267LfffiM/z2GcAABAL/3kJz/JnnvuuU0HvSSpquy5556bvYdS2AMAAHprWw96M7akH8IeAACwXTnjjDNy4IEH5uCDD86hhx6ar33ta1s9zQsvvDBnnnnmGKpLdtlll7FMxzl7AADAduOrX/1qLrroonzjG9/ITjvtlNtvvz0//elPR3ruvffem4ULZ49QK1euzMqVK8dZ6lazZw8AANhu3HLLLVm8eHF22mmnJMnixYuz9957Z9myZbn99tuTJKtXr86KFSuSJKeddlpOOumkPP/5z8/xxx+fpz71qbnqqqvun96KFSuyZs2afOADH8irX/3q3HnnnVm2bFl+9rOfJUn+9V//Nfvuu2/uueeefOc738lRRx2Vww47LM94xjPy7W9/O0lyww035GlPe1oOP/zw/OEf/uHY+irsAQAA243nP//5uemmm/LEJz4xJ598cr74xS9u8jlr1qzJBRdckA9/+MNZtWpVzj///CSD4HjzzTfnsMMOu3/c3XbbLYcccsj90/3kJz+ZI488MjvuuGNOOumkvOMd78iaNWvytre9LSeffHKS5JRTTsnv/u7v5utf/3oe/ehHj62vvTuM87Df/+BY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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# countplot을 이용한 시각화\n",
    "plt.figure(figsize=(15,5)) # 그림판의 가로, 세로 크기 조정(인치 단위)\n",
    "sns.countplot(data=train, x=\"Title\", hue=\"Survived\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6ec4a14",
   "metadata": {},
   "source": [
    "#### 일부 수치가 적응 호칭을 Other로 통일하자.\n",
    "- Mr, Mrs, Miss, Master, Rev, Other"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "40639842",
   "metadata": {},
   "outputs": [],
   "source": [
    "# map 함수 이용하기(데이터 치환시 사용)\n",
    "title_dic = {\n",
    "    \"Mr\" : \"Mr\",\n",
    "    \"Mrs\" : \"Mrs\",\n",
    "    \"Miss\" :\"Miss\",\n",
    "    \"Master\":\"Master\",\n",
    "    \"Rev\":\"Rev\"  \n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "6649afac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId\n",
       "31     NaN\n",
       "246    NaN\n",
       "318    NaN\n",
       "370    NaN\n",
       "399    NaN\n",
       "444    NaN\n",
       "450    NaN\n",
       "537    NaN\n",
       "557    NaN\n",
       "600    NaN\n",
       "633    NaN\n",
       "642    NaN\n",
       "648    NaN\n",
       "661    NaN\n",
       "695    NaN\n",
       "711    NaN\n",
       "746    NaN\n",
       "760    NaN\n",
       "767    NaN\n",
       "797    NaN\n",
       "823    NaN\n",
       "Name: Title, dtype: object"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title_mapping = train['Title'].map(title_dic)\n",
    "title_mapping[title_mapping.isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "343a5393",
   "metadata": {},
   "outputs": [],
   "source": [
    "train[\"Title\"] = title_mapping.fillna(\"Other\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "193d5cc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# test 적용\n",
    "title_mapping = test[\"Title\"].map(title_dic)\n",
    "test[\"Title\"] = title_mapping.fillna(\"Other\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "e5fcc18d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Mr' 'Mrs' 'Miss' 'Master' 'Other' 'Rev']\n",
      "['Mr' 'Mrs' 'Miss' 'Master' 'Other' 'Rev']\n"
     ]
    }
   ],
   "source": [
    "print(train[\"Title\"].unique())\n",
    "print(test[\"Title\"].unique())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8fb81a08",
   "metadata": {},
   "source": [
    "#### 사용하지 않을 컬럼 정리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "f64990b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',\n",
       "       'Fare', 'Cabin', 'Embarked', 'Family', 'Family_cat', 'Title'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "aae2d3c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare',\n",
       "       'Cabin', 'Embarked', 'Family', 'Family_cat', 'Title'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "98da65f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "train.drop([\"Name\", \"SibSp\", \"Parch\", \"Ticket\"], axis=1, inplace=True)\n",
    "test.drop([\"Name\", \"SibSp\", \"Parch\", \"Ticket\"], axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "1479b5a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "train columns :  Index(['Survived', 'Pclass', 'Sex', 'Age', 'Fare', 'Cabin', 'Embarked',\n",
      "       'Family', 'Family_cat', 'Title'],\n",
      "      dtype='object')\n",
      "test columns :  Index(['Pclass', 'Sex', 'Age', 'Fare', 'Cabin', 'Embarked', 'Family',\n",
      "       'Family_cat', 'Title'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(\"train columns : \", train.columns)\n",
    "print(\"test columns : \", test.columns)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d701064",
   "metadata": {},
   "source": [
    "## 모델링\n",
    "- 인코딩(문자형태의 데이터를 숫자형태로 변환)\n",
    "  1. lable encoding\n",
    "  2. one-hot encoding\n",
    "- 특성선택(feature selection)\n",
    "- 모델선택 및 하이퍼파라미터 튜닝\n",
    "- 모델학습 및 평가"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "3563f2a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Survived', 'Pclass', 'Sex', 'Age', 'Fare', 'Cabin', 'Embarked',\n",
       "       'Family', 'Family_cat', 'Title'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "8ba37e86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 891 entries, 1 to 891\n",
      "Data columns (total 10 columns):\n",
      " #   Column      Non-Null Count  Dtype   \n",
      "---  ------      --------------  -----   \n",
      " 0   Survived    891 non-null    int64   \n",
      " 1   Pclass      891 non-null    int64   \n",
      " 2   Sex         891 non-null    object  \n",
      " 3   Age         891 non-null    int64   \n",
      " 4   Fare        891 non-null    float64 \n",
      " 5   Cabin       891 non-null    object  \n",
      " 6   Embarked    891 non-null    object  \n",
      " 7   Family      891 non-null    int64   \n",
      " 8   Family_cat  891 non-null    category\n",
      " 9   Title       891 non-null    object  \n",
      "dtypes: category(1), float64(1), int64(4), object(4)\n",
      "memory usage: 102.9+ KB\n"
     ]
    }
   ],
   "source": [
    "train.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7cd25ff2",
   "metadata": {},
   "source": [
    "### 인코딩"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "85b456d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 인코딩할 컬럼명만 선택\n",
    "categorical_features = [\"Sex\",\"Cabin\",\"Embarked\",\"Family_cat\", \"Title\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "4e9a688a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>female</th>\n",
       "      <th>male</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>891</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             female  male\n",
       "PassengerId              \n",
       "1                 0     1\n",
       "2                 1     0\n",
       "3                 1     0\n",
       "4                 1     0\n",
       "5                 0     1\n",
       "...             ...   ...\n",
       "887               0     1\n",
       "888               1     0\n",
       "889               1     0\n",
       "890               0     1\n",
       "891               0     1\n",
       "\n",
       "[891 rows x 2 columns]"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.get_dummies(train[\"Sex\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "9b8d021e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 반복문으로 인코딩하기(train)\n",
    "for feature_name in categorical_features:\n",
    "    one_hot = pd.get_dummies(train[feature_name], prefix=feature_name)\n",
    "    train = pd.concat([train, one_hot], axis=1) # 기존 데이터 끝에 one_hot을 붙임\n",
    "    train.drop(feature_name, axis=1, inplace = True) # 기존 글자컬럼을 삭제"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "bc05f640",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Family</th>\n",
       "      <th>Sex_female</th>\n",
       "      <th>Sex_male</th>\n",
       "      <th>Cabin_A</th>\n",
       "      <th>Cabin_B</th>\n",
       "      <th>Cabin_C</th>\n",
       "      <th>...</th>\n",
       "      <th>Embarked_S</th>\n",
       "      <th>Family_cat_Alone</th>\n",
       "      <th>Family_cat_Small</th>\n",
       "      <th>Family_cat_Large</th>\n",
       "      <th>Title_Master</th>\n",
       "      <th>Title_Miss</th>\n",
       "      <th>Title_Mr</th>\n",
       "      <th>Title_Mrs</th>\n",
       "      <th>Title_Other</th>\n",
       "      <th>Title_Rev</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>38</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>26</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>35</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>35</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 28 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Survived  Pclass  Age     Fare  Family  Sex_female  Sex_male  \\\n",
       "PassengerId                                                                 \n",
       "1                   0       3   22   7.2500       1           0         1   \n",
       "2                   1       1   38  71.2833       1           1         0   \n",
       "3                   1       3   26   7.9250       0           1         0   \n",
       "4                   1       1   35  53.1000       1           1         0   \n",
       "5                   0       3   35   8.0500       0           0         1   \n",
       "\n",
       "             Cabin_A  Cabin_B  Cabin_C  ...  Embarked_S  Family_cat_Alone  \\\n",
       "PassengerId                             ...                                 \n",
       "1                  0        0        0  ...           1                 0   \n",
       "2                  0        0        1  ...           0                 0   \n",
       "3                  0        0        0  ...           1                 1   \n",
       "4                  0        0        1  ...           1                 0   \n",
       "5                  0        0        0  ...           1                 1   \n",
       "\n",
       "             Family_cat_Small  Family_cat_Large  Title_Master  Title_Miss  \\\n",
       "PassengerId                                                                 \n",
       "1                           1                 0             0           0   \n",
       "2                           1                 0             0           0   \n",
       "3                           0                 0             0           1   \n",
       "4                           1                 0             0           0   \n",
       "5                           0                 0             0           0   \n",
       "\n",
       "             Title_Mr  Title_Mrs  Title_Other  Title_Rev  \n",
       "PassengerId                                               \n",
       "1                   1          0            0          0  \n",
       "2                   0          1            0          0  \n",
       "3                   0          0            0          0  \n",
       "4                   0          1            0          0  \n",
       "5                   1          0            0          0  \n",
       "\n",
       "[5 rows x 28 columns]"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "24e6f029",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 반복문으로 인코딩하기(test)\n",
    "for feature_name in categorical_features:\n",
    "    one_hot = pd.get_dummies(test[feature_name], prefix=feature_name)\n",
    "    test = pd.concat([test, one_hot], axis=1) # 기존 데이터 끝에 one_hot을 붙임\n",
    "    test.drop(feature_name, axis=1, inplace = True) # 기존 글자컬럼을 삭제"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "e5037a4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Family</th>\n",
       "      <th>Sex_female</th>\n",
       "      <th>Sex_male</th>\n",
       "      <th>Cabin_A</th>\n",
       "      <th>Cabin_B</th>\n",
       "      <th>Cabin_C</th>\n",
       "      <th>Cabin_D</th>\n",
       "      <th>...</th>\n",
       "      <th>Embarked_S</th>\n",
       "      <th>Family_cat_Alone</th>\n",
       "      <th>Family_cat_Small</th>\n",
       "      <th>Family_cat_Large</th>\n",
       "      <th>Title_Master</th>\n",
       "      <th>Title_Miss</th>\n",
       "      <th>Title_Mr</th>\n",
       "      <th>Title_Mrs</th>\n",
       "      <th>Title_Other</th>\n",
       "      <th>Title_Rev</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>892</th>\n",
       "      <td>3</td>\n",
       "      <td>34</td>\n",
       "      <td>7.8292</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>893</th>\n",
       "      <td>3</td>\n",
       "      <td>47</td>\n",
       "      <td>7.0000</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>894</th>\n",
       "      <td>2</td>\n",
       "      <td>62</td>\n",
       "      <td>9.6875</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>895</th>\n",
       "      <td>3</td>\n",
       "      <td>27</td>\n",
       "      <td>8.6625</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>896</th>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>12.2875</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Pclass  Age     Fare  Family  Sex_female  Sex_male  Cabin_A  \\\n",
       "PassengerId                                                                \n",
       "892               3   34   7.8292       0           0         1        0   \n",
       "893               3   47   7.0000       1           1         0        0   \n",
       "894               2   62   9.6875       0           0         1        0   \n",
       "895               3   27   8.6625       0           0         1        0   \n",
       "896               3   22  12.2875       2           1         0        0   \n",
       "\n",
       "             Cabin_B  Cabin_C  Cabin_D  ...  Embarked_S  Family_cat_Alone  \\\n",
       "PassengerId                             ...                                 \n",
       "892                0        0        0  ...           0                 1   \n",
       "893                0        0        0  ...           1                 0   \n",
       "894                0        0        0  ...           0                 1   \n",
       "895                0        0        0  ...           1                 1   \n",
       "896                0        0        0  ...           1                 0   \n",
       "\n",
       "             Family_cat_Small  Family_cat_Large  Title_Master  Title_Miss  \\\n",
       "PassengerId                                                                 \n",
       "892                         0                 0             0           0   \n",
       "893                         1                 0             0           0   \n",
       "894                         0                 0             0           0   \n",
       "895                         0                 0             0           0   \n",
       "896                         1                 0             0           0   \n",
       "\n",
       "             Title_Mr  Title_Mrs  Title_Other  Title_Rev  \n",
       "PassengerId                                               \n",
       "892                 1          0            0          0  \n",
       "893                 0          1            0          0  \n",
       "894                 1          0            0          0  \n",
       "895                 1          0            0          0  \n",
       "896                 0          1            0          0  \n",
       "\n",
       "[5 rows x 26 columns]"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "b569cb2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((891, 28), (418, 26))"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.shape, test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "e805a9d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Cabin_T', 'Survived'}"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 집합연산으로 다른 컬럼을 확인해보자.\n",
    "set(train.columns) - set(test.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "fe3c6c91",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 훈련용 데이터는 Cabin에 T가 존재했지만\n",
    "# 테스트 데이터는 Cabin에 T가 없어서 one-hot 인코딩 시 컬럼이 안만들어졌다.\n",
    "# 테스트 데이터 끝에 Cabin_T를 추가하자\n",
    "test['Cabin_T']=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "7e6b507c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Family</th>\n",
       "      <th>Sex_female</th>\n",
       "      <th>Sex_male</th>\n",
       "      <th>Cabin_A</th>\n",
       "      <th>Cabin_B</th>\n",
       "      <th>Cabin_C</th>\n",
       "      <th>Cabin_D</th>\n",
       "      <th>...</th>\n",
       "      <th>Family_cat_Alone</th>\n",
       "      <th>Family_cat_Small</th>\n",
       "      <th>Family_cat_Large</th>\n",
       "      <th>Title_Master</th>\n",
       "      <th>Title_Miss</th>\n",
       "      <th>Title_Mr</th>\n",
       "      <th>Title_Mrs</th>\n",
       "      <th>Title_Other</th>\n",
       "      <th>Title_Rev</th>\n",
       "      <th>Cabin_T</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>892</th>\n",
       "      <td>3</td>\n",
       "      <td>34</td>\n",
       "      <td>7.8292</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>893</th>\n",
       "      <td>3</td>\n",
       "      <td>47</td>\n",
       "      <td>7.0000</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>894</th>\n",
       "      <td>2</td>\n",
       "      <td>62</td>\n",
       "      <td>9.6875</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>895</th>\n",
       "      <td>3</td>\n",
       "      <td>27</td>\n",
       "      <td>8.6625</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>896</th>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "      <td>12.2875</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 27 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Pclass  Age     Fare  Family  Sex_female  Sex_male  Cabin_A  \\\n",
       "PassengerId                                                                \n",
       "892               3   34   7.8292       0           0         1        0   \n",
       "893               3   47   7.0000       1           1         0        0   \n",
       "894               2   62   9.6875       0           0         1        0   \n",
       "895               3   27   8.6625       0           0         1        0   \n",
       "896               3   22  12.2875       2           1         0        0   \n",
       "\n",
       "             Cabin_B  Cabin_C  Cabin_D  ...  Family_cat_Alone  \\\n",
       "PassengerId                             ...                     \n",
       "892                0        0        0  ...                 1   \n",
       "893                0        0        0  ...                 0   \n",
       "894                0        0        0  ...                 1   \n",
       "895                0        0        0  ...                 1   \n",
       "896                0        0        0  ...                 0   \n",
       "\n",
       "             Family_cat_Small  Family_cat_Large  Title_Master  Title_Miss  \\\n",
       "PassengerId                                                                 \n",
       "892                         0                 0             0           0   \n",
       "893                         1                 0             0           0   \n",
       "894                         0                 0             0           0   \n",
       "895                         0                 0             0           0   \n",
       "896                         1                 0             0           0   \n",
       "\n",
       "             Title_Mr  Title_Mrs  Title_Other  Title_Rev  Cabin_T  \n",
       "PassengerId                                                        \n",
       "892                 1          0            0          0        0  \n",
       "893                 0          1            0          0        0  \n",
       "894                 1          0            0          0        0  \n",
       "895                 1          0            0          0        0  \n",
       "896                 0          1            0          0        0  \n",
       "\n",
       "[5 rows x 27 columns]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "ca319112",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 훈련용 데이터와 테스트 데이터의 인덱스 순서가 다르기 때문에 정렬해주자.\n",
    "train.sort_index(axis=1, inplace=True)\n",
    "test.sort_index(axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "d0ba39ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Age', 'Cabin_A', 'Cabin_B', 'Cabin_C', 'Cabin_D', 'Cabin_E', 'Cabin_F',\n",
       "       'Cabin_G', 'Cabin_M', 'Cabin_T', 'Embarked_C', 'Embarked_Q',\n",
       "       'Embarked_S', 'Family', 'Family_cat_Alone', 'Family_cat_Large',\n",
       "       'Family_cat_Small', 'Fare', 'Pclass', 'Sex_female', 'Sex_male',\n",
       "       'Survived', 'Title_Master', 'Title_Miss', 'Title_Mr', 'Title_Mrs',\n",
       "       'Title_Other', 'Title_Rev'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "32c9da1b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Age', 'Cabin_A', 'Cabin_B', 'Cabin_C', 'Cabin_D', 'Cabin_E', 'Cabin_F',\n",
       "       'Cabin_G', 'Cabin_M', 'Cabin_T', 'Embarked_C', 'Embarked_Q',\n",
       "       'Embarked_S', 'Family', 'Family_cat_Alone', 'Family_cat_Large',\n",
       "       'Family_cat_Small', 'Fare', 'Pclass', 'Sex_female', 'Sex_male',\n",
       "       'Title_Master', 'Title_Miss', 'Title_Mr', 'Title_Mrs', 'Title_Other',\n",
       "       'Title_Rev'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6031687e",
   "metadata": {},
   "source": [
    "### 특성선택\n",
    "- 예측결과에 영향을 줄 특성들을 골라본다.\n",
    "- Family와 Family_cat이 비슷한 특성이기 때문에 선택해보자."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a1aa549e",
   "metadata": {},
   "source": [
    "#### 문제와 답 만들기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "5af1ea20",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train = train.drop(['Survived', 'Family'], axis=1)\n",
    "y_train = train.Survived # = train['Survived']\n",
    "X_test = test.drop('Family', axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "ee0c3685",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((891, 26), (891,))"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape, y_train.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a70b63a",
   "metadata": {},
   "source": [
    "### 학습\n",
    "- KNN모델과 DecisionTree모델 활용"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "5a45a702",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "92289ff5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 모델 생성\n",
    "knn_model = KNeighborsClassifier()\n",
    "tree_model = DecisionTreeClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "62e193a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier()"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 모델 학습\n",
    "knn_model.fit(X_train, y_train)\n",
    "tree_model.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "cc4e2434",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 모델 예측\n",
    "knn_pre = knn_model.predict(X_test)\n",
    "tree_pre = tree_model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "8029948a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 정답파일 만들기\n",
    "submission = pd.read_csv('./data/gender_submission.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "b120fae4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>892</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>893</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>894</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>895</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>896</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived\n",
       "0          892         0\n",
       "1          893         1\n",
       "2          894         0\n",
       "3          895         0\n",
       "4          896         1"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "submission.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "ebdf6188",
   "metadata": {},
   "outputs": [],
   "source": [
    "submission[\"Survived\"] = knn_pre"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "117a03c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 데이터프레임을 csv파일로 저장\n",
    "submission.to_csv(\"./data/knn_pre.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "22aa307d",
   "metadata": {},
   "outputs": [],
   "source": [
    "submission['Survived'] = tree_pre\n",
    "submission.to_csv(\"./data/tree_pre.csv\", index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "464a5778",
   "metadata": {},
   "source": [
    "### 정규화\n",
    "- 편향된 데이터를 정규분포로 만드는 작업\n",
    "- 모델의 성능을 향상"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "94035d64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>56</td>\n",
       "      <td>18</td>\n",
       "      <td>27</td>\n",
       "      <td>2.926144</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>81</td>\n",
       "      <td>57</td>\n",
       "      <td>3</td>\n",
       "      <td>4.744364</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>25</td>\n",
       "      <td>9</td>\n",
       "      <td>11</td>\n",
       "      <td>1.439488</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>20</td>\n",
       "      <td>13</td>\n",
       "      <td>30</td>\n",
       "      <td>0.569621</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>27</td>\n",
       "      <td>13</td>\n",
       "      <td>13</td>\n",
       "      <td>1.230924</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    0   1   2         y\n",
       "0  56  18  27  2.926144\n",
       "1  81  57   3  4.744364\n",
       "2  25   9  11  1.439488\n",
       "3  20  13  30  0.569621\n",
       "4  27  13  13  1.230924"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv(\"./data/data_skew.csv\")\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c7994be3",
   "metadata": {},
   "source": [
    "##### 데이터 스케일링\n",
    "- 각 feature의 스케일이 다르면 예측결과가 안좋은 경우가 있다.\n",
    "- KNN, SVM, 신경망모델, Clustering 모델 등"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "0a57214c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "89b5d1c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 스케일러 생성 (평균과 표준편차)\n",
    "std_scaler = StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "f480872c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "StandardScaler()"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 기준값 생성\n",
    "std_scaler.fit(X_train[[\"Fare\"]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "1398df76",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 데이터 변형(train)\n",
    "scaled_fare = std_scaler.transform(X_train[['Fare']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "7995047b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Fare', ylabel='Density'>"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "X_train['Fare'] = scaled_fare\n",
    "sns.kdeplot(data=X_train, x='Fare')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "8b755518",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 데이터 변형(test)\n",
    "scaled_fare = std_scaler.transform(X_test[['Fare']])\n",
    "X_test['Fare'] = scaled_fare"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "90cfdc47",
   "metadata": {},
   "outputs": [],
   "source": [
    "knn_model2 = KNeighborsClassifier()\n",
    "knn_model2.fit(X_train, y_train)\n",
    "knn_pre2 = knn_model2.predict(X_test)\n",
    "submission['Survived'] = knn_pre2\n",
    "submission.to_csv('./data/scale_knn_pre.csv', index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9d0b561",
   "metadata": {},
   "source": [
    "### 하이퍼 파라미터 튜닝\n",
    "- KNN모델과 DecisionTree 모델을 최적화해보자.\n",
    "- KNN : 이웃숫자\n",
    "- Tree : 나무의 깊이, 리프노드의 개수, 한 리프노드에 들어갈 샘플 수 등"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6702ae83",
   "metadata": {},
   "source": [
    "#### 모델 최적화를 위해 검증 데이터셋을 만들자!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "3d808431",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "f171cefb",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train2, X_val, y_train2, y_val = train_test_split(X_train,\n",
    "                                                   y_train,\n",
    "                                                   test_size=0.3,\n",
    "                                                   random_state=719)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "71ae9405",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((623, 26), (623,))"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train2.shape, y_train2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "51516fec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((268, 26), (268,))"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_val.shape, y_val.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ea0dcdb7",
   "metadata": {},
   "source": [
    "##### KNN 튜닝"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "2933812a",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_score = [] # 훈련데이터의 점수가 들어갈 리스트\n",
    "val_score = [] # 검증데이터의 점수가 들어갈 리스트\n",
    "\n",
    "for n in range(1,20): \n",
    "    # 이웃을 1~19개까지 변경하면서 모델생성\n",
    "    knn_model = KNeighborsClassifier(n_neighbors=n)\n",
    "    # 모델 학습\n",
    "    knn_model.fit(X_train2, y_train2)\n",
    "    # 훈련데이터에 대한 점수 누적\n",
    "    train_score.append(knn_model.score(X_train2, y_train2))\n",
    "    # 검증데이터에 대한 점수 누적\n",
    "    val_score.append(knn_model.score(X_val, y_val))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "e5e63ffd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,5))\n",
    "plt.plot(range(1,20), train_score, label=\"train\")\n",
    "plt.plot(range(1,20), val_score, label=\"val\")\n",
    "plt.xticks(range(1,20))\n",
    "plt.grid()\n",
    "plt.legend()\n",
    "plt.ylabel(\"accuracy\")\n",
    "plt.xlabel('n_neighbors')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09af3067",
   "metadata": {},
   "source": [
    "##### DecisionTree 튜닝"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "d732825f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 교차검증함수\n",
    "from sklearn.model_selection import cross_val_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "8b170f33",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_score = []\n",
    "val_score = []\n",
    "\n",
    "for d in range(1,30):\n",
    "    tree_model = DecisionTreeClassifier(max_depth=d, random_state=720)\n",
    "    result = cross_val_score(tree_model, X_train, y_train, cv=5)\n",
    "    val_score.append(result.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "75de8f18",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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3W4BZrj7EGBGsNzmvLuihG89+j798rL4x7fG0aVDRrybJCIiIiIibVCYPYXjgGXuvsLd9wCTgYmNbH8B8Hit5TSgvZmlAVnA2mD9RODR4PWjwJnRbHQieH9VKZc9MpuenTN57Irx5GW3i3eTRERERESkjQqzKOwFrK61XBys+wIzywJOAZ4CcPc1wG+AImAdsNXdXwo2z3f3dcF264DuobQ+TuYWbeabf51NfsdMHr9yPN1yVBCKiIiIiEh4zN3DObDZucDJ7n5FsHwJMM7dr69n2/OAi9399GC5C5EC8TxgC/Bv4El3/4eZbXH3zrX23ezuX7iv0MyuAq4CyM/PHzN58uQon2HLlZWVkZ2dvXd55dYq7py9i+x0Y9LhmeRmRq9mr5sVplhmxTpPWcpKlDxlKStR8pTVurJinacsZSVKXlvNao4JEybMcfex9b7p7qF8AEcA02stTwImNbDtM8CFtZbPBf5Sa/kbwIPB6yVAQfC6AFiyr7aMGTPGE9HMmTP3vp5fvMVH3PqiH3XHDC/eXB5qVthimRXrPGUpK1HylKWsRMlTVuvKinWespSVKHltNas5gPe9gXopzOGjs4EhZjbAzDKIPChmSt2NzKwTcBzwbK3VRcB4M8syMwNOBBYH700BLg1eX1pnv1Zp8bptXPyXd8lul8bjV46nV+f28W6SiIiIiIgkidBmQXf3SjO7DphO5OmhD7v7QjO7Onj/oWDTs4CX3H1HrX3fNbMngblAJfAB8Mfg7TuAJ8zsW0SKx3PDOodY+GT9di7687tkpqXy+FXj6ZObFe8miYiIiIhIEgmtKARw92nAtDrrHqqz/AjwSD373grcWs/6EiI9h63e2rJqfvCnd0lLMf555eH0y+sQ7yaJiIiIiEiSCXXyemnYyk07uHP2LsD555XjGdgt8W5GFRERERGRti/UnkKpX3W1c81jc6mqdp64cjyDu6sgFBERERGR+FBRGAcpKcZvzx3F++/PZmh+TrybIyIiIiIiSUxFYZwM69mRDR1T490MERERERFJcrqnUEREREREJImpKBQREREREUliKgpFRERERESSmIpCERERERGRJKaiUEREREREJImpKBQREREREUliKgpFRERERESSmIpCERERERGRJKaiUEREREREJImpKBQREREREUli5u7xbkPozGwjUBjvdtSjK7BJWa0q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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,5))\n",
    "plt.plot(range(1,30), val_score, label=\"val\")\n",
    "plt.xticks(range(1,30))\n",
    "plt.grid()\n",
    "plt.legend()\n",
    "plt.ylabel(\"accuracy\")\n",
    "plt.xlabel('max_depth')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1cbc552",
   "metadata": {},
   "source": [
    "### 모델 평가\n",
    "- KNN의 이웃은 7\n",
    "- DecisionTree의 최대깊이는 4 정도가 좋겠다~"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "235eece8",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_knn = KNeighborsClassifier(n_neighbors=7)\n",
    "final_tree = DecisionTreeClassifier(max_depth=4, random_state=720)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "218a7cea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier(max_depth=4, random_state=720)"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_knn.fit(X_train, y_train)\n",
    "final_tree.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "907e9f0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "knn_pre = final_knn.predict(X_test)\n",
    "tree_pre = final_tree.predict(X_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be1ea705",
   "metadata": {},
   "source": [
    "#### 성능개선을 위해 고려해볼 사항\n",
    "1. 특성선택\n",
    "2. 데이터 확보\n",
    "3. 전처리 작업 변경(결측치, 특성공학, 스케일링 등)\n",
    "4. 모델변경 - 앙상블"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b14d41d",
   "metadata": {},
   "source": [
    "## 앙상블\n",
    "1. 보팅(voting)\n",
    "  - 서로 다른 알고리즘의 모델 여러개를 이용해서 투표로 예측결과를 만들어낸다.\n",
    "  - 하드보팅 : 모델의 최종 예측결과로 투표\n",
    "  - 소프트보팅 : 모델의 확률결과로 투표\n",
    "2. 배깅(bagging)\n",
    "  - 같은 알고리즘 모델 여러개를 이용해서 투표를 진행\n",
    "  - 여러개의 모델들이 학습할 때 다른 의견이 나올 수 있도록 부트스트래핑 작업을 한다.\n",
    "  - 매번 모델이 학습할때마다 랜덤하게 데이터를 추출하되,  중복된 추출을 허용한다.\n",
    "  - 랜덤포레스트 : DecisionTree의 배깅모델\n",
    "3. 부스팅(boosting)\n",
    "  - 같은 알고리즘 모델 여러개를 이용해서 투표를 진행\n",
    "  - 이전 모델이 잘못 학습한 결과를 다음 모델이 반영해서 학습하도록 하는 기법\n",
    "  - 학습 진행이 순차적으로 일어나기 때문에 상대적으로 속도가 느리다."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e0bcb7fe",
   "metadata": {},
   "source": [
    "### Random Forest(랜덤포레스트)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "2d52a409",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "52d43c86",
   "metadata": {},
   "outputs": [],
   "source": [
    "rf_model = RandomForestClassifier(n_estimators=100, # 배깅할 모델 개수\n",
    "                                 max_features=0.9, # 각 모델이 랜덤하게 사용할 특성 수\n",
    "                                  max_depth=8, # 각 모델의 최대 깊이\n",
    "                                  min_samples_leaf=10, # 리프노드의 최소샘플수\n",
    "                                  random_state=721\n",
    "                                 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "bc812a48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.83798883, 0.82022472, 0.84831461, 0.80337079, 0.83146067])"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf_rs = cross_val_score(rf_model, X_train, y_train, cv=5)\n",
    "rf_rs"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b1498bc",
   "metadata": {},
   "source": [
    "#### 그리드서치\n",
    "- 앙상블 모델의 경우 하이퍼파라미터 수가 엄청 많다.\n",
    "- 각 파라미터를 독립적으로 튜닝하는건 불가능하다.\n",
    "- 많은 양의 파라미터를 동시에 튜닝하기 위한 함수로 그리드서치를 지원한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "ff3965ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "f4b2e9bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 탐색하고 싶은 하이퍼파라미터 조합을 딕셔너리로 생성\n",
    "param_grid = {\n",
    "    'max_depth':[5,10,15,20],\n",
    "    'n_estimators': [100,500,1000,1500],\n",
    "    'max_features':[0.5,0.7],\n",
    "    'min_samples_leaf' : [10,20,25]\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "77b789dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 튜닝할 모델, 사용할 파라미터, 교차검증 횟수\n",
    "model = RandomForestClassifier(random_state=721)\n",
    "grid = GridSearchCV(model, param_grid, cv=3, n_jobs=-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "62552a07",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GridSearchCV(cv=3, estimator=RandomForestClassifier(random_state=721),\n",
       "             n_jobs=-1,\n",
       "             param_grid={'max_depth': [5, 10, 15, 20],\n",
       "                         'max_features': [0.5, 0.7],\n",
       "                         'min_samples_leaf': [10, 20, 25],\n",
       "                         'n_estimators': [100, 500, 1000, 1500]})"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grid.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "e27d2043",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'max_depth': 5,\n",
       " 'max_features': 0.7,\n",
       " 'min_samples_leaf': 10,\n",
       " 'n_estimators': 100}"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 최고의 조합 확인\n",
    "grid.best_params_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "3f44b474",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8338945005611672"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 최고점수 확인\n",
    "grid.best_score_ "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "28281955",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 최고조합으로 학습완료된 모델\n",
    "best_model = grid.best_estimator_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "79b50f1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "pre = best_model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "78306b0b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1,\n",
       "       1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,\n",
       "       1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,\n",
       "       1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1,\n",
       "       1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,\n",
       "       0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0,\n",
       "       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,\n",
       "       0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,\n",
       "       1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1,\n",
       "       0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0,\n",
       "       1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,\n",
       "       0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1,\n",
       "       0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,\n",
       "       0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1,\n",
       "       0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0,\n",
       "       1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0,\n",
       "       0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,\n",
       "       1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1,\n",
       "       0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],\n",
       "      dtype=int64)"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pre"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3d550d4",
   "metadata": {},
   "source": [
    "#### boosting 라이브러리 설치"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "93b4684b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting xgboost\n",
      "  Downloading xgboost-1.6.1-py3-none-win_amd64.whl (125.4 MB)\n",
      "Requirement already satisfied: numpy in c:\\users\\ai\\anaconda3\\lib\\site-packages (from xgboost) (1.21.5)\n",
      "Requirement already satisfied: scipy in c:\\users\\ai\\anaconda3\\lib\\site-packages (from xgboost) (1.7.3)\n",
      "Installing collected packages: xgboost\n",
      "Successfully installed xgboost-1.6.1\n"
     ]
    }
   ],
   "source": [
    "!pip install xgboost"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "3fc27b42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting lightGBM\n",
      "  Downloading lightgbm-3.3.2-py3-none-win_amd64.whl (1.0 MB)\n",
      "Requirement already satisfied: scikit-learn!=0.22.0 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from lightGBM) (1.0.2)\n",
      "Requirement already satisfied: wheel in c:\\users\\ai\\anaconda3\\lib\\site-packages (from lightGBM) (0.37.1)\n",
      "Requirement already satisfied: numpy in c:\\users\\ai\\anaconda3\\lib\\site-packages (from lightGBM) (1.21.5)\n",
      "Requirement already satisfied: scipy in c:\\users\\ai\\anaconda3\\lib\\site-packages (from lightGBM) (1.7.3)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from scikit-learn!=0.22.0->lightGBM) (2.2.0)\n",
      "Requirement already satisfied: joblib>=0.11 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from scikit-learn!=0.22.0->lightGBM) (1.1.0)\n",
      "Installing collected packages: lightGBM\n",
      "Successfully installed lightGBM-3.3.2\n"
     ]
    }
   ],
   "source": [
    "!pip install lightGBM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "75c20f98",
   "metadata": {},
   "outputs": [],
   "source": [
    "from xgboost import XGBClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "2235166c",
   "metadata": {},
   "outputs": [],
   "source": [
    "xgb_model = XGBClassifier(booster=\"gbtree\", # 모델의 종류\n",
    "                         n_estimators=100, # 앙상블 모델 개수\n",
    "                         learning_Rate=0.1, # 학습률\n",
    "                          max_depth=4, # 최대깊이(일반적으로 깊게 설정X)\n",
    "                          gamma = 0.2 # 키우면 모델 단순, 작아지면 모델이 복잡!\n",
    "                         )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "6d17829d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 탐색하고 싶은 하이퍼파라미터 조합을 딕셔너리로 생성\n",
    "param_grid = {\n",
    "    'max_depth':[5,10,15,20],\n",
    "    'n_estimators': [100,500,1000,1500],\n",
    "    'max_features':[0.5,0.7],\n",
    "    'min_samples_leaf' : [10,20,25]\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "f703edec",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 튜닝할 모델, 사용할 파라미터, 교차검증 횟수\n",
    "xgb_model = XGBClassifier(random_state=721)\n",
    "xgb_grid = GridSearchCV(xgb_model, param_grid, cv=3, n_jobs=-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "4bcdbf74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11:17:00] WARNING: C:/Users/Administrator/workspace/xgboost-win64_release_1.6.0/src/learner.cc:627: \n",
      "Parameters: { \"max_features\", \"min_samples_leaf\" } might not be used.\n",
      "\n",
      "  This could be a false alarm, with some parameters getting used by language bindings but\n",
      "  then being mistakenly passed down to XGBoost core, or some parameter actually being used\n",
      "  but getting flagged wrongly here. Please open an issue if you find any such cases.\n",
      "\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "GridSearchCV(cv=3,\n",
       "             estimator=XGBClassifier(base_score=None, booster=None,\n",
       "                                     callbacks=None, colsample_bylevel=None,\n",
       "                                     colsample_bynode=None,\n",
       "                                     colsample_bytree=None,\n",
       "                                     early_stopping_rounds=None,\n",
       "                                     enable_categorical=False, eval_metric=None,\n",
       "                                     gamma=None, gpu_id=None, grow_policy=None,\n",
       "                                     importance_type=None,\n",
       "                                     interaction_constraints=None,\n",
       "                                     learning_rate=None, max_bin=None,\n",
       "                                     max_ca...\n",
       "                                     max_delta_step=None, max_depth=None,\n",
       "                                     max_leaves=None, min_child_weight=None,\n",
       "                                     missing=nan, monotone_constraints=None,\n",
       "                                     n_estimators=100, n_jobs=None,\n",
       "                                     num_parallel_tree=None, predictor=None,\n",
       "                                     random_state=721, reg_alpha=None,\n",
       "                                     reg_lambda=None, ...),\n",
       "             n_jobs=-1,\n",
       "             param_grid={'max_depth': [5, 10, 15, 20],\n",
       "                         'max_features': [0.5, 0.7],\n",
       "                         'min_samples_leaf': [10, 20, 25],\n",
       "                         'n_estimators': [100, 500, 1000, 1500]})"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xgb_grid.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "05d25965",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "({'max_depth': 5,\n",
       "  'max_features': 0.7,\n",
       "  'min_samples_leaf': 10,\n",
       "  'n_estimators': 100},\n",
       " 0.819304152637486)"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 최고의 조합 확인, 점수 확인\n",
    "grid.best_params_, xgb_grid.best_score_ "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f4720b0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {
    "height": "calc(100% - 180px)",
    "left": "10px",
    "top": "150px",
    "width": "257.997px"
   },
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
