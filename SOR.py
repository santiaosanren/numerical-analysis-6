# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:29:01 2018

@author: 闫汝海
"""

import numpy as np

def SOR(A,b,w,tol):
    N=np.shape(A)[0]
    x=np.mat(np.zeros((N,11)))
    def fun(x,ii):
        for i in range(N):
            sum1=0.0
            sum2=0.0
            for j in range(N-1):
                sum1+=A[i,j]*x[j,ii+1]
            for j in range(i+1,N):
                sum2+=A[i,j]*x[j,ii]
            #x[i,ii+1]=x[i,ii]+w*((b[i]-sum1-sum2)/A[i,i])
            x[i,ii+1]=w*((b[i]-sum1-sum2)/A[i,i])
        return(x)
        
    for k in range(10):
        temp=fun(x,k)
        if max(abs(x[:,k]-temp[:,k+1]))<tol:
            print("最终结果：x=")
            print(temp[:,k+1])
            return(temp[:,k+1])
        print("第" + str(k+1) + "次结果：x=")
        x=temp
        print(x[:,k+1])
    
    
"""main"""
#tol=1e-6 #tol为精度要求
#w=1 #w为松弛因子
#A=np.mat([[8.0,-3.0,2.0],
#          [4.0,11.0,-1.0],
#          [6.0,3.0,12.0]])
#b=np.mat([[20.0],
#          [33.0],
#          [36.0]])
#SOR(A,b,w,tol)
    
tol=1e-5 #tol为精度要求
w=0.8
w=0.9
w=1.0
w=1.1
w=1.2 #w为松弛因子
A3=np.mat([[4.0, 2.0, -3.0, -1.0, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0],
           [8.0, 6.0, -5.0, -3.0, 6.0, 5.0, 0.0, 1.0, 0.0, 0.0],
           [4.0, 2.0, -2.0, -1.0, 3.0, 2.0, -1.0, 0.0, 3.0, 1.0],
           [0.0, -2.0, 1.0, 5.0, -1.0, 3.0, -1.0, 1.0, 9.0, 4.0],
           [-4.0, 2.0, 6.0, -1.0, 6.0, 7.0, -3.0, 3.0, 2.0, 3.0],
           [8.0, 6.0, -8.0, 5.0, 7.0, 17.0, 2.0, 6.0, -3.0, 5.0],
           [0.0, 2.0, -1.0, 3.0, -4.0, 2.0, 5.0, 3.0, 0.0, 1.0],
           [16.0, 10.0, -11.0, -9.0, 17.0, 34.0, 2.0, -1.0, 2.0, 2.0],
           [4.0, 6.0, 2.0, -7.0, 13.0, 9.0, 2.0, 0.0, 12.0, 4.0],
           [0.0, 0.0, -1.0, 8.0, -3.0, -24.0, -8.0, 6.0, 3.0, -1.0]])
b3=np.mat([[5.0],[12.0],[3.0],[2.0],[3.0],[46.0],[13.0],[38.0],[19.0],[-21.0]])

A4=np.mat([[4.0, 2.0, -4.0, 0.0, 2.0, 4.0, 0.0, 0.0],
           [2.0, 2.0, -1.0, -2.0, 1.0, 3.0, 2.0, 0.0],
           [-4.0, -1.0, 14.0, 1.0, -8.0, -3.0, 5.0, 6.0],
           [0.0, -2.0, 1.0, 6.0, -1.0, -4.0, -3.0, 3.0],
           [2.0, 1.0, -8.0, -1.0, 22.0, 4.0, -10.0, -3.0],
           [4.0, 3.0, -3.0, -4.0, 4.0, 11.0, 1.0, -4.0],
           [0.0, 2.0, 5.0, -3.0, -10.0, 1.0, 14.0, 2.0],
           [0.0, 0.0, 6.0, 3.0, -3.0, -4.0, 2.0, 19.0]])
b4=np.mat([[0.0],[-6.0],[20.0],[23.0],[9.0],[-22.0],[-15.0],[45.0]])

A5=np.mat([[4.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
           [-1.0, 4.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
           [0.0, -1.0, 4.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
           [0.0, 0.0, -1.0, 4.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
           [0.0, 0.0, 0.0, -1.0, 4.0, -1.0, 0.0, 0.0, 0.0, 0.0],
           [0.0, 0.0, 0.0, 0.0, -1.0, 4.0, -1.0, 0.0, 0.0, 0.0],
           [0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 4.0, -1.0, 0.0, 0.0],
           [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 4.0, -1.0, 0.0],
           [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 4.0, -1.0],
           [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 4.0]])
b5=np.mat([[7.0],[5.0],[-13.0],[2.0],[6.0],[-12.0],[14.0],[-4.0],[5.0],[-5.0]])

SOR(A3,b3,w,tol)
SOR(A4,b4,w,tol)
SOR(A5,b5,w,tol)

