# 1. 导入numpy库并简写为 np
import numpy as np

# 2. 打印numpy的版本和配置说明
print(np.__version__)

# 3. 创建长度为10的空向量
Z = np.zeros(10)
print(Z)
print(Z.shape)
print(Z.ndim)

# 4. 如何找到任何一个数组的内存大小？
Z = np.zeros((10, 10))
print(Z)
print(Z.shape)
print(Z.ndim)

# 5. 如何从命令行得到numpy中add函数的说明文档?
print( np.info( np.add ) )

# 6. 创建一个长度为10并且除了第五个值为1的空向量
Z = np.zeros(10)
Z[4] = 1
print(Z)

# 7. 创建一个值域范围从10到49的向量
Z = np.arange(10, 50)
print(Z)

# 8. 反转一个向量(第一个元素变为最后一个)
Z = np.arange(50)
#print(Z)
Z = Z[::-1] # 切片索引
print(Z)

# 9. 创建一个 3x3 并且值从0到8的矩阵
Z = np.arange(9).reshape(3, 3)
print(Z)

# 10. 找到数组[1,2,0,0,4,0]中非0元素的位置索引
nz = np.nonzero([1, 2, 0, 0, 4, 0])
print(nz)

# 11. 创建一个 3x3 的单位矩阵
Z = np.eye(3)
print(Z)

# 12. 创建一个 3x3x3的随机数组
Z = np.random.random((3, 3, 3))
print(Z)

# 13. 创建一个 10x10 的随机数组并找到它的最大值和最小值
Z = np.random.random((10, 10))
Zmax, Zmin = Z.max(), Z.min()
print(Zmax, Zmin)

Z = np.random.random((10))
print(Z)
m = Z.mean()
print(m)

# 15. 创建一个二维数组，其中边界值为1，其余值为0
Z = np.ones((10, 10))
Z[1:-1, 1:-1] = 0
print(Z)

# 16. 对于一个存在在数组，如何添加一个用0填充的边界?
Z = np.ones((5, 5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)

# 17. 以下表达式运行的结果分别是什么?
print(0 * np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3*0.1)


# 18. 创建一个 5x5的矩阵，并设置值1,2,3,4落在其对角线下方位置
#  np.diag(array) 中
# array是一个1维数组时，结果形成一个以一维数组为对角线元素的矩阵
# array是一个二维矩阵时，结果输出矩阵的对角线元素

print( np.diag(np.arange(1, 5), -1) )

# 19. 创建一个8x8 的矩阵，并且设置成棋盘样式
Z = np.zeros((8, 8), dtype=int)
Z[1::2, 0::2] = 1
Z[0::2, 1::2] = 1
print(Z)

# 20. 考虑一个 (6,7,8) 形状的数组，其第100个元素的索引(x,y,z)是什么?
# https://www.cnblogs.com/lucas-zhao/p/11792365.html
print(np.unravel_index(100, (6, 7, 8)))
























