import numpy as np

class Sigmoid:
    def __init__(self):
        self.params=[]

    def forward(self,x):
        y=1/(1+np.exp(-x))
        return y

class Affine:
    def __init__(self,W,b):
        self.params=[W,b]

    def forward(self,x):
        W,b=self.params
        out=np.dot(x,W)+b
        return out

class TwoLayerNet:
    def __init__(self,input_size,hidden_size,out_size):
        I,H,O=input_size,hidden_size,out_size
        W1=np.random.randn(I,H)
        b1=np.random.randn(H,)
        W2=np.random.randn(H,O)
        b2=np.random.randn(O,)
        self.layers=[Affine(W1,b1),Sigmoid(),Affine(W2,b2)]
        self.params=[]
        for layer in self.layers:
            self.params+=layer.params

    def predict(self,x):
        for layer in self.layers:
            x=layer.forward(x)
        return x

class MatMul:
    def __init__(self,W):
        self.params=[W]
        self.grads=[np.zeros_like(W)]
        self.x=None
    def forward(self,x):
        self.x=x
        W,=self.params
        out=np.dot(x,W)
        return out
    def backward(self,dout):
        W,=self.params
        dW=np.dot(self.x.T,dout)
        dx=np.dot(dout,W.T)
        self.grads[0][...]=dW
        return dx