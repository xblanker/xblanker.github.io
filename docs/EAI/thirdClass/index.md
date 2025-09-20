# 神经网络基础原理

## 环境配置

下载 Pytorch ：

访问 [Pytorch](https://pytorch.org/get-started/locally)，按照官网上的要求来下载相应版本的 Pytorch ，如下图所示。

![Pytorch](image/pytorch.png)

在命令行中输入相应的命令即可。

!!! tip "如何查看 cuda 版本"
    在命令行输入
    ```bash
    nvidia-smi
    ```
    即可查看对应的 cuda 版本。
    有 gpu 才能用 cuda ，没有的用 cpu 版本的 Pytorch。

## 知识讲解

### 损失函数

**损失函数** 能够量化目标的实际值与预测值之间的差距。通常我们会选择非负数作为损失，且数值越小表示损失越小，完美预测时的损失为0。回归问题中最常用的损失函数是平方误差函数：

$$l_i(\mathbf{w}, b) = \frac{1}{2} \left(\hat{y}_i - y_i\right)^2.$$

为了衡量模型在整个数据级上的拟合质量，我们常需计算在训练集 $\mathbf{n}$ 个样本上的均值损失，即：

$$L(\mathbf{w}, b) = \frac{1}{n}\sum_{i=1}^n l^{(i)}(\mathbf{w}, b) = \frac{1}{n} \sum_{i=1}^n \frac{1}{2}\left(\mathbf{w}^\top \mathbf{x}^{(i)} + b - y^{(i)}\right)^2.$$

### 梯度下降



### softmax 回归



### 线性层

## 参考资料

- [Pytorch Learn](https://pytorch.org/get-started/locally/)

- [动手学深度学习 Pytorch 版](https://zh.d2l.ai)