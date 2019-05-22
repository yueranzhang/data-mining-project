import cv2
import numpy as np

import histsimilar


def make_regalur_image(img, size=(125, 150)):
    return img.resize(size).convert('RGB')


def filter(pic):
    img_rgb = cv2.imread(pic)
    # size = (125 * 150)
    # img_rgb = img_rgb.resize(size).convert('RGB')
    img = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    img = cv2.bilateralFilter(img, 9, 75, 75)
    r, g, b = cv2.split(img)
    equalize1 = cv2.equalizeHist(r)
    equalize2 = cv2.equalizeHist(g)
    equalize3 = cv2.equalizeHist(b)
    equalize = cv2.merge((r, g, b))

    equalize = cv2.cvtColor(equalize, cv2.COLOR_RGB2GRAY)

    ret, thresh_image = cv2.threshold(equalize, 127, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    equalize = cv2.equalizeHist(thresh_image)

    canny_image = cv2.Canny(equalize, 250, 255)
    canny_image = cv2.convertScaleAbs(canny_image)
    kernel = np.ones((3, 3), np.uint8)
    dilated_image = cv2.dilate(canny_image, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    c = contours[0]
    final = cv2.drawContours(img, [c], -1, (255, 0, 0), 3)

    mask = np.zeros(img_rgb.shape, np.uint8)
    new_image = cv2.drawContours(mask, [c], 0, 255, -1, )
    new_image = cv2.bitwise_and(img_rgb, img_rgb, mask=equalize)
    return new_image


# def compare_image(pic1, pic2):
#
#     imageA = filter(pic1)
#     imageB = filter(pic2)
#
#     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
#     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
#
#     (score, diff) = compare_ssim(grayA, grayB, full=True)
#     return score

def img_similarity(pic1, pic2):
    try:
        # 读取图片
        img1 = filter(pic1)
        img2 = filter(pic2)

        # 初始化ORB检测器
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        # 提取并计算特征点
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)

        # knn筛选结果
        matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)

        # 查看最大匹配点数目
        good = [m for (m, n) in matches if m.distance < 0.9 * n.distance]
        similary = len(good) / len(matches)
        return similary

    except:
        print('cannot calculate the similarity')
        similary = 0
        return similary


def main(img):
    img1 = img

    cloth_path = []
    with open('clothes_match_labeled_data.txt', encoding='gbk', errors='ignore') as f:
        for line in f:
            name = line.split(':')[0]
            path = 'my_training_shirts/' + name + '.jpg'
            cloth_path.append(path)
        cloth_path = cloth_path[1:]

    similary_list = []
    for img2 in cloth_path:
        print('calculating the similarity with ' + img2)
        sim1 = img_similarity(img1, img2)
        # sim2 = compare_image(img1, img2)
        sim3 = histsimilar.calc_similar_by_path(img1, img2)
        similary = 0.4 * sim1 + 0.6 * sim3
        similary_list.append(similary)
    similary_dic = {}.fromkeys(cloth_path)
    i = 0
    for key, value in similary_dic.items():
        similary_dic[key] = similary_list[i]
        i += 1
    best_img = max(similary_dic, key=similary_dic.get)
    best_img = best_img.split('/')[-1]
    best_img = best_img.split('.')[0]
    return best_img


if __name__ == '__main__':

    img1 = '4.jpg'

    cloth_path = []
    with open('clothes_match_labeled_data.txt', encoding='gbk', errors='ignore') as f:
        for line in f:
            name = line.split(':')[0]
            path = '/my_training_shirts/' + name + '.jpg'
            cloth_path.append(path)
        cloth_path = cloth_path[1:]

    similary_list = []
    for img2 in cloth_path:
        print('calculating the similarity with ' + img2)
        sim1 = img_similarity(img1, img2)
        # sim2 = compare_image(img1, img2)
        sim3 = histsimilar.calc_similar_by_path(img1, img2)
        similary = 0.4 * sim1 + 0.6 * sim3
        similary_list.append(similary)
    similary_dic = {}.fromkeys(cloth_path)
    i = 0
    for key, value in similary_dic.items():
        similary_dic[key] = similary_list[i]
        i += 1
    best_img = max(similary_dic, key=similary_dic.get)
    print(best_img)

    # cv2.namedWindow("new", cv2.WINDOW_NORMAL)
    # cv2.imshow("new", img1)
    # cv2.waitKey()

    # img2_path = '4.jpg'
    # similary1 = img_similarity(img1_path, img2_path)
    # similary2 = compare_image(img1_path, img2_path)
    # similary3 = histsimilar.calc_similar_by_path(img1_path, img2_path)
    # similary = 0.2*similary1 + 0.3*similary2 + 0.5*similary3
    # print(similary,'\n')
