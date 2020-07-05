# WEEK4

## 문제 설명
MNIST 데이터셋을 CNN 이 아닌 RNN 으로 Classification 해봅시다.
기존에는 [batch_size, image_dim(width*height)] shape 의 이미지를 2-D Convolution 을 이용해 분류를 하셨다면, 이미지의 width 를 sequence 라고 생각하고(shape: [batch_size(32), sequence_length(image_width=256), image_height(256)]) RNN 을 이용하여 이미지를 분류해보세요

## Dataset 다운로드 링크
다음 링크를 통해 데이터셋을 다운받아주세요. 직접 Dataloader 를 사용하여 학습에 학습에 사용하십시오. 학습에 사용되는 input과 output 텐서의 shape 은 app.py 의 run 과 metric 메서드의 documentation을 참고하십시오.

Dataset 은 Yann lecun 교수님의 ubyte 형식의 mnist 데이터셋입니다. 

- Train Image 다운로드 링크: [다운로드](http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz)
- Train Label 다운로드 링크: [다운로드](http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz)
- Test Image 다운로드 링크: [다운로드](http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz)
- Test Label 다운로드 링크: [다운로드](http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz)

압축 풀기 후 [python mnist](https://pypi.org/project/python-mnist/) 파이선 모듈을 이용해 데이터를 사용하시면 됩니다.

**예시 코드**
```python
from mnist import MNIST
mndata = MNIST('./dir_with_mnist_data_files')
images, labels = mndata.load_training()
```

## Data Format 설명
채점에 사용되는 app.py - run 메서드의 input 과 output 텐서의 shape 입니다. 다음을 고려하여 app.py 의 run 메서드를 작성해주십시오. 다음 포맷과 다른 shape 을 반환할 경우 0점 처리 됩니다.

- **INPUT Shape**
	```[batch_size(32), image_dim(width(28)*height(28)=784)]```

- **OUTPUT Shape**
	```[batch_size(32), num_classes(10)]```

## 체점 기준
- 체점 Metric 은 정확도를 사용합니다. (app.py 의 metric() 메서드 참고)
- 평균 정확도가 96% 이상의 모델을 제작하십시오

