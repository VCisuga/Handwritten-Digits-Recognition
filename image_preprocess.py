import cv2
import numpy as np

IMAGE_MAX_WIDTH = 1000
IMAGE_MAX_HEIGHT = 1000
MARGIN_RATIO = 6
MIX_TEST_NUM = 5


def image_preprocessing(image_dir, model):

	# 读取图片
	img = cv2.imread(image_dir)

	# =====================图像处理======================== #

	# 转换成灰度图像
	gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
	# cv2.imshow('gray_img', gray_img)
	# cv2.waitKey()

	# 进行高斯滤波
	gauss_img = cv2.GaussianBlur(gray_img, (5,5), 0, 0, cv2.BORDER_DEFAULT)

	# 边缘检测
	img_edge1 = cv2.Canny(gauss_img, 100, 200)
	# img_edge1 = cv2.Canny(gray_img, 100, 200)
	# cv2.imshow('img_edge1', img_edge1)
	# cv2.waitKey()
	# ==================================================== #
	# =====================图像分割======================== #
    
    # 这里缺代码！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 这一段图像分割的预处理，请同学们思考并完成
	# 获取原始图像的宽和高
	high = img.shape[0]
	width = img.shape[1]

	# 分别初始化高和宽的和
	add_width = np.zeros(high, dtype=int)
	add_high = np.zeros(width, dtype=int)

	# 计算每一行的灰度图的值的和
	for h in range(high):
		for w in range(width):
			add_width[h] = add_width[h] + img_edge1[h][w]

	# 计算每一列的值的和
	for w in range(width):
		for h in range(high):
			add_high[w] = add_high[w] + img_edge1[h][w]

	# 初始化上下边界为宽度总值最大的值的索引
	# acount_high_up = np.argmax(add_width)
	# acount_high_down = np.argmax(add_width)
	acount_high_up = IMAGE_MAX_WIDTH - 1
	acount_high_down = 0

	for i in range(len(add_width) - MIX_TEST_NUM + 1):
		mix_width = 0
		for j in range(MIX_TEST_NUM):
			mix_width = mix_width + add_width[i+j]
		if mix_width > 255 * MIX_TEST_NUM:
			acount_high_down = i
			break
	for i in range(len(add_width) - MIX_TEST_NUM + 1):
		mix_width = 0
		for j in range(MIX_TEST_NUM):
			mix_width = mix_width + add_width[len(add_width) - i - j -1]
		if mix_width > 255 * MIX_TEST_NUM:
			acount_high_up = len(add_width) -i - 1
			break

	for i in range(len(add_high) - MIX_TEST_NUM + 1):
		mix_heigth = 0
		for j in range(MIX_TEST_NUM):
			mix_heigth = mix_heigth + add_high[i+j]
		if mix_heigth > 255 * MIX_TEST_NUM:
			acount_width_left = i
			break
	for i in range(len(add_high) - MIX_TEST_NUM + 1):
		mix_heigth = 0
		for j in range(MIX_TEST_NUM):
			mix_heigth = mix_heigth + add_high[len(add_high) - i - j -1]
		if mix_heigth > 255 * MIX_TEST_NUM:
			acount_width_right = len(add_high) -i - 1
			break

	# 求出宽和高的间距
	width_spacing = acount_width_right - acount_width_left
	high_spacing = acount_high_up - acount_high_down

	# 上下左右各保留一部分的空白部分
	if acount_width_left > width_spacing / MARGIN_RATIO:
		acount_width_left = acount_width_left - int(np.floor(width_spacing / MARGIN_RATIO))
	else:
		acount_width_left = 1

	if width_spacing / MARGIN_RATIO < IMAGE_MAX_WIDTH - acount_width_right:
		acount_width_right = acount_width_right + int(np.floor(width_spacing / MARGIN_RATIO))
	else:
		acount_width_right = 1

	if acount_high_down > high_spacing / MARGIN_RATIO:
		acount_high_down = acount_high_down - int(np.floor(high_spacing / MARGIN_RATIO))
	else:
		acount_high_down = 1

	if high_spacing / MARGIN_RATIO < IMAGE_MAX_HEIGHT - acount_high_up:
		acount_high_up = acount_high_up + int(np.floor(high_spacing / MARGIN_RATIO))
	else:
		acount_high_up = 1

	# 求出宽和高的间距
	width_spacing = acount_width_right - acount_width_left
	high_spacing = acount_high_up - acount_high_down

	# 求出宽和高的间距差
	poor = width_spacing - high_spacing

	# 将数字进行正方形分割，目的是方便之后进行图像压缩
	tailor_image = img[acount_high_down:acount_high_up,
					acount_width_left:acount_width_right]
	# print(tailor_image.shape)

	# 展示
	# cv2.imshow('tailor_image', tailor_image)
	# cv2.waitKey()

	# ===================================================================================
	# h_mid_index = int(np.floor(len(sum_h_nonzero) / 2))  # 获取不为0的像素点的中心点位置
	# w_mid_index = int(np.floor(len(sum_w_nonzero) / 2)) # 获取不为0的像素点的中心点位置
	# offset_h = int(h/2) - h_mid_index
	# offset_w = int(h/2) - w_mid_index
	# offset_martrix_h = np.zeros((h, w))
	# offset_h_abs = abs(offset_h)
	# for i in range(h):
	# 	if offset_h_abs + i < w: 平移
	# 		offset_martrix_h[i][offset_h_abs + i] = 1
	# 	else:
	# 		offset_martrix_h[i][offset_h_abs + i - w] = 1

	# offset_martrix_w = np.zeros((h, w))
	# for i in range(h):
	# 	if offset_w_abs + i < h: 平移
	# 		offset_martrix_w[i][offset_h_abs + i] = 1
	# 	else:
	# 		offset_martrix_w[i][offset_h_abs + i - h] = 1

	# if offset_h > 0:
	# 	gray_img = np.matmul(gray_img, offset_martrix_w)
	# else:
	#
    # ===================================================================================

	# 将裁剪后的图片进行灰度化
	gray_img = cv2.cvtColor(tailor_image, cv2.COLOR_BGR2GRAY)
	# cv2.imshow('gray_img', gray_img)
	# cv2.waitKey()

	# 高斯去噪
	gauss_img = cv2.GaussianBlur(gray_img, (5, 5), 0, 0, cv2.BORDER_DEFAULT)

	# 将图像扩展到正方形
	pixel_range_width = np.zeros(width_spacing, dtype=np.uint8)
	pixel_range_width = pixel_range_width + 255
	pixel_range_height = np.zeros((high_spacing,1), dtype=np.uint8)
	pixel_range_height = pixel_range_height + 255
	# print(pixel_range_width, pixel_range_height)

	if poor > 0:
		for i in range(int(abs(np.floor(poor/2)))):
			gauss_img = np.insert(gauss_img, 0, 255, axis=0)
			gauss_img = np.append(gauss_img, pixel_range_width, axis=0)
	else:
		for i in range(int(abs(np.floor(poor/2)))):
			gauss_img = np.insert(gauss_img, 0, 255, axis=1)
			gauss_img = np.append(gauss_img, pixel_range_height, axis=1)
	# print(len(gauss_img),len(gauss_img[0]))

	# 获取图像的高和宽
	high = gauss_img.shape[0]
	wide = gauss_img.shape[1]
	# print(high, wide)

	# 将图像每个点的灰度值进行阈值比较
	for h in range(high):
		for w in range(wide):

			# 若灰度值大于100，则判断为背景并赋值0，否则将深灰度值变白处理
			if gauss_img[h][w] > 100:
				gauss_img[h][w] = 0
			else:
				gauss_img[h][w] = 255 - gauss_img[h][w]
	# cv2.imshow('gauss_img', gauss_img)
	# cv2.waitKey()

	# ==================================================== #
	# ======================小图处理======================= #
	# 将图像形状调整到28*28大小
	if model == 'Normal':
		zoom_image = cv2.resize(gauss_img, (28, 28))
	elif model == 'LeNet':
		zoom_image = cv2.resize(gauss_img, (28, 28))
	# ==================================================== #
	# print(zoom_image)
	# cv2.imshow('zoom_image', zoom_image)
	# cv2.waitKey()

	return zoom_image
