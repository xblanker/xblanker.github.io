# Numpy 基础

[NumPy](https://numpy.org) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算。提供多维数组对象，各种派生对象（如掩码数组和矩阵），以及用于数组快速操作的各种 API，有包括数学、逻辑、形状操作、排序、选择、输入输出、离散傅立叶变换、基本线性代数，基本统计运算和随机模拟等等。

## 安装 NumPy

=== "pip"
    ```bash
    pip install numpy==<version>
    
    # 下载过慢可以考虑国内镜像
    # 清华镜像
    pip install numpy -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

    # ZJU镜像
    pip install numpy -i https://mirrors.zju.edu.cn/pypi/web/simple
    ```

=== "conda"
    ```bash
    conda install numpy
    ```

!!! tip "tips"
    我们建议在虚拟环境下下载 NumPy 等本课程所需的 Pypi 。

NumPy 是 Python 科学计算生态系统的基石，其核心数据结构是 ndarray（N-dimensional array），即N维数组对象。

## ndarray

可以使用一下命令来创建 NumPy 数组。

```python
import numpy as np

np.array()

# 全 0 数组
np.zeros(shape=shape, dtype=dtype, order='C')           # 行优先

# 未初始化的数组
np.empty(shape=shape, dtype=dtype, order='F')           # 列优先
```

![ndarray](image/ndarray.png)

### 关键属性

- Data Block(数据块)： 一块连续的内存区域，用于存储数组的实际数据。

- Metadata(元数据)：描述数组的额外信息。

    - `ndarray.shape`：tuple，表示数组的大小。

    - `ndarray.dtype`：元素数据类型。

    - `ndarray.ndim`：维度。

    - `ndarray.size`：数组中元素个数。

    - `ndarray.flags`：内存的布局信息等。

    - `ndarray.itemsize`：元素所占字节数。

    - `ndarray.strides`：tuple，储存跨度信息，描述了在内存中为了移动到下一个元素，在每个维度上需要移动的字节数，是 NumPy 数组高性能的原因之一。

![Metadata](image/metadata.png)

## 索引和切片

Numpy 数组可以基于下标进行索引，切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组。

```python
SampleNdarray = numpy.array([[1, 2, 3], [4, 5, 6]])

print(SampleNdarray[0])
# 输出 [1 2 3]
print(SampleNdarray[0, 0])
# 输出 1
print(SampleNdarray[0, :])
# 输出 [1 2 3]
print(SampleNdarray[:, 0])
# 输出 [1 4]
print(SampleNdarray[0:2, 0:2])
# 输出 [[1 2], 
#       [4 5]]
print(SampleNdarray[:, 0::2])
# 输出 [[1 3],
#       [4 6]]
```

### 高级索引

- 整数数组索引：

    ```python
    x = numpy.array([[1,  2],  [3,  4],  [5,  6]]) 
    y = x[[0,1,2],  [0,1,0]] # [1 4 5]
    ```

- 布尔索引

    ```python
    x = numpy.array([[1,  2],  [3,  4],  [5,  6]])
    y = x[x > 4] # [5 6]
    ```

- 花式索引

    ```python
    ```















## 参考资料

- [Guide to NumPy](https://web.mit.edu/dvp/Public/numpybook.pdf)
- [菜鸟教程](https://www.runoob.com/numpy/numpy-tutorial.html)