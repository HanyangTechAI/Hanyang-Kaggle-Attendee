# WEEK1

## 문제 설명
하나(**하**이**나**리)는 헬스장에 가서 사람들의 키가 모두 다르다는 것을 알게 되었다. 이후 한명씩 체중계에 올라 자신의 몸무게를 측정하는 것을 보게 되었다.

하나는 평소 과학적으로 분석하는 것을 좋아하여 헬스장에서 사람들의 키와 몸무게에 대한 데이터를 모두 수집하였다.

|Column 명|의미|
|:-----------:|:-------------:|
|Weight|몸무게(kg)|
|Height|키(cm)|


하나는 어떤 사람의 키를 알면 그 사람의 몸무게를 예측할 수 있다고 생각을 하였다. 하나를 도와 사람의 몸무게를 예측하는 인공지능을 만들어보자!

## Dataset
Dataset은 **weight-height.csv** 을 사용합니다.  

남성의 키와 몸무게에 대한 데이터셋은 주어진 csv 파일로부터 다음의 코드를 이용하여 불러올 수 있습니다.

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.open_csv("weight-height.csv")

X, y =  data['Height'], data['Weight']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

## Data Format 설명
채점에 사용되는 app.py - run 메소드의 input과 output 텐서의 shape는 다음과 같습니다.
- **Input Shape** [batch_size, height(1)]
- **Output Shape** [batch_size, logit(1)]

*반드시 상기된 형식을 준수해주세요. 형식이 다른 경우 0점 처리됩니다.*

## 채점 기준
- metric은 accuracy를 사용합니다. (app.py의 metric() 메소드 참고)
- accuracy가 70% 이상이어야 합니다.
