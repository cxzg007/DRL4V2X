import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 加载图像数据
img1 = mpimg.imread('E:\jie\power23 0.05\Evaluated-Return-per--Episode-10000-Step-100-0.png')
img2 = mpimg.imread('E:\jie\power23 0.05\Evaluated-Return-per--Episode-10000-Step-100-1.png')

# 创建图形和子图
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制第一个图像
ax.plot(img1[:,0], img1[:,1], label='Algorithm 1', color='blue')

# 绘制第二个图像
ax.plot(img2[:,0], img2[:,1], label='Algorithm 2', color='red')

# 添加标签和标题
ax.set_xlabel('Number of Episodes')
ax.set_ylabel('Mean Return per Episode')
ax.set_title('Comparison of Mean Return per Episode for Two Algorithms')
ax.legend()

# 显示图表
plt.show()
