# 线性回归

## 线性模型

### 基本元素

假设因变量 y 与自变量 x 之间的关系是线性的，即 y 可以表示为 x 元素中的加权和。

!!! tip "tips"
    这里通常允许包含观测值的一些噪声。
    
    其次，我们假设任何噪声都比较正常，如噪声遵循正态分布。

当我们输入包含 d 个特征时，预测结果可以表示为：

$$\hat{y} = w_1  x_1 + ... + w_d  x_d + b.$$

将所有特征放到向量 $\mathbf{x} \in \mathbb{R}^d$ 中，将所有权重放到向量 $\mathbf{w} \in \mathbb{R}^d$ 中，可以用点积形式来简洁地表达：

$$\hat{y} = \mathbf{w}^\top \mathbf{x} + b.$$

用符号表示的矩阵 $\mathbf{X} \in \mathbb{R}^{n \times d}$ 可以很方便地引用我们整个数据集的 $\mathbf{n}$ 个样本。$\mathbf{X}$ 的每一行是一个样本，每一列是一种特征。

对于特征集合 $\mathbf{X}$ ，预测值 $\hat{\mathbf{y}} \in \mathbb{R}^n$ 可以通过矩阵-向量乘法表示为

$${\hat{\mathbf{y}}} = \mathbf{X} \mathbf{w} + b.$$

### 损失函数

**损失函数** 能够量化目标的实际值与预测值之间的差距。通常我们会选择非负数作为损失，且数值越小表示损失越小，完美预测时的损失为0。回归问题中最常用的损失函数是平方误差函数：

$$l_i(\mathbf{w}, b) = \frac{1}{2} \left(\hat{y}_i - y_i\right)^2.$$

为了衡量模型在整个数据级上的拟合质量，我们常需计算在训练集 $\mathbf{n}$ 个样本上的均值损失，即：

$$L(\mathbf{w}, b) = \frac{1}{n}\sum_{i=1}^n l^{(i)}(\mathbf{w}, b) = \frac{1}{n} \sum_{i=1}^n \frac{1}{2}\left(\mathbf{w}^\top \mathbf{x}^{(i)} + b - y^{(i)}\right)^2.$$

将损失关于 $\mathbf{w}$ 的导数设为0，得到解析解：

$$\mathbf{w}^* = (\mathbf X^\top \mathbf X)^{-1}\mathbf X^\top \mathbf{y}.$$

??? success 
    将偏置 $\mathbf{b}$ 合并到参数 $\mathbf{w}$ 中，即得到 $\mathbf{\hat{w}}$ 与 $\mathbf{\hat{X}}$ ：

    $\hat{\mathbf{w}}$ = $\begin{bmatrix} \mathbf{w} \\ b \end{bmatrix} = \begin{bmatrix} w_1 \\ w_2 \\ \vdots \\ w_d \\ b \end{bmatrix}$
    $\hat{\mathbf{X}}$ = $\begin{bmatrix} x_{11} & x_{12} & \dots & x_{1d} & 1 \\ x_{21} & x_{22} & \dots & x_{2d} & 1 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ x_{n1} & x_{n2} & \dots & x_{nd} & 1 \end{bmatrix}$

    那么 $L(\mathbf{w}, b)$ = $\frac{1}{n} \sum_{i=1}^n \frac{1}{2}\left(\mathbf{w}^\top \mathbf{x}^{(i)} + b - y^{(i)}\right)^2$ = $(\hat{\mathbf{X}} \hat{\mathbf{w}} - \mathbf{y})^T (\hat{\mathbf{X}} \hat{\mathbf{w}} - \mathbf{y})$

    使用[矩阵求导法则](https://blog.csdn.net/daaikuaichuan/article/details/80620518)，对 $\mathbf{w}$ 求导，得到
    $\boxed{\frac{\partial L}{\partial \hat{\mathbf{w}}} = \hat{\mathbf{X}}^\top (\hat{\mathbf{X}}\hat{\mathbf{w}} - \mathbf{y})}$

    令 $\frac{\partial L}{\partial \hat{\mathbf{w}}} = 0$ 即得到解析解 $\boxed{\mathbf{w}^* = (\mathbf X^\top \mathbf X)^{-1}\mathbf X^\top \mathbf{y}}$

### 随机梯度下降

计算损失函数关于模型参数的导数的实际过程可能会非常慢：因为在每一次更新参数之前，我们必须遍历整个数据集。因此，我们通常会在每次需要计算更新的时候随机抽取一小批样本，这种变体叫做小批量随机梯度下降（minibatch stochastic gradient descent）。

计算步骤如下：

1. 初始化模型参数的值，如随机初始化；

2. 从数据集中随机抽取小批量样本且在负梯度的方向上更新参数，并不断迭代这一步骤。