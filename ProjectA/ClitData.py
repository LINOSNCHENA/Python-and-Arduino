
import pandas as pd
import numpy as np
x = np.arange(6000).reshape(250,24)
x1,x2,x3=np.split(x, [150,200])
print(x.shape)
# print(x)
print("=======================|DA2-fake|=========================XXX========="+'\n')
print('x1.shape=',x1.shape)
print('x2.shape=',x2.shape)
print('x3.shape=',x3.shape)
TRAIN_SPLIT=15
TEST_SPLIT=20
outputs=x
outputs_train, outputs_test, outputs_validate = np.split(outputs, [TRAIN_SPLIT, TEST_SPLIT])
print("=======================|DA3-used|========================XXX========="+'\n')
print('4-Train-output=',outputs_train.shape)
print('5-Test-Xoutput=',outputs_test.shape)
print('6-Valid-output=',outputs_validate.shape)

print("=======================|DA4|=========================XXX========="+'\n')

print('7-Train_Split=',TRAIN_SPLIT)
print('8-Test_Splitt=',TEST_SPLIT)

print("=======================|ARRAY_OR_LIST|================XXX========="+'\n')
X1=np.split(x, [1,3])
a,b,X2=np.split(x, [150,200])
#X2=np.split(x, [150,200])

print(x.shape)
print('xxxxxx')
# print(X1.shape)
print('xxxxxx-change-Array to 11111111-list-INPUTS')
print(type(x))
print(type(outputs))
print('xxxxxx-change-Array to 222222222-list-OUTPUTS')
print('type(X1)=',type(X1))
print('type(X2)=',type(X2))
print('type(outputs_trin)=',type(outputs_train))
print('type(x3)=',type(x3))

print("=======================|END|=========================XXX========="+'\n')