import numpy as np

matrix_Vec = np.array([[1,-3,5,-9], #계수행렬은 x,y,z의 계수를 나타내며 이 공식의 값은 벡터로 표현한다 
                       [2,-1,-3,19],#예)x  y  z   값
                       [3,1,4,-13]]) # (1,-3  5) (-9)



if(matrix_Vec[0,0]!=0 and matrix_Vec[1,0]!=0 and matrix_Vec[2,0]!=0): #

    matrix_Vec[1]=matrix_Vec[1]-matrix_Vec[1,0]*matrix_Vec[0] # 0번째 행과 1번쨰 행의 연산 후 대입 
    print(matrix_Vec)

    matrix_Vec[2]=matrix_Vec[2]-matrix_Vec[2,0]*matrix_Vec[0] #0번째 행과 2번째 행의 연산 후 대입
    print(matrix_Vec)

    matrix_Vec[2]=matrix_Vec[1,1]*matrix_Vec[2]-matrix_Vec[2,1]*matrix_Vec[1]#1번째 계산후 변경된 행과 2번째 행을 비교하며 연산 후 대입
    print(matrix_Vec)

#연산

matrix_Vec[2]=matrix_Vec[2]/matrix_Vec[2,2] #z를 구하는 공식 
matrix_Vec[1]=(matrix_Vec[1]-(matrix_Vec[2]*matrix_Vec[1,2]))/matrix_Vec[1,1]#y를 구하는 공식
matrix_Vec[0]=matrix_Vec[0]-(matrix_Vec[0,1]*matrix_Vec[1])-(matrix_Vec[0,2]*matrix_Vec[2])#x를 구하는 공식

#이러한 연산을 하게 된다면 계수행렬의 값이 모두 1아니면 0 으로 나와있고 그것이 순차적으로 나열되어 있을 것 이다
#이것을 기약행 사다리꼴 이라고 한다.

print(matrix_Vec)

