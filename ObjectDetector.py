import json
import math
import os

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

def drawRectangles(ax_, circles, triangles, ground):
    if ground:
        a = 'r'
    else:
        a = 'b'

    lists = [circles, triangles]
    for lst in lists:
        for i in range(len(lst)):
            rect = patches.Rectangle((lst[i][0][0], lst[i][1][1]),
                                     lst[i][1][0] - lst[i][0][0],
                                     lst[i][0][1] - lst[i][1][1],
                                     linewidth=1, edgecolor=a, facecolor='none')
            ax_.add_patch(rect)


def get_difference(ground_, predict_):
    li_dif = [i for i in ground_ if i not in predict_]
    return len(li_dif)


if __name__ == '__main__':
    GROUND = "C:\\Users\\Evyatar\\PycharmProjects\\Detector\\Detector\\ground_truth"
    PREDICT = "C:\\Users\\Evyatar\\PycharmProjects\\Detector\\Detector\\prediction"
    IMG = "C:\\Users\\Evyatar\\PycharmProjects\\Detector\\Detector\\img"
    groundTruths = dict()
    prediction = dict()
    images = dict()

    # draw ground truth
    directory = fr'{GROUND}'
    for filename in os.listdir(directory):
        f = open(f'{GROUND}\\{filename}')
        data = json.load(f)
        groundTruths[filename[:-5:]] = data
        f.close()

    # draw prediction
    directory = fr'{PREDICT}'
    for filename in os.listdir(directory):
        f = open(f'{PREDICT}\\{filename}')
        data = json.load(f)
        prediction[filename[:-5:]] = data
        f.close()

    # get images
    directory = fr'{IMG}'
    for filename in os.listdir(directory):
        im = Image.open(f'{IMG}\\{filename}')
        images[filename[:-4:]] = im

    misses_per_image = []
    for name, im in images.items():

        ground = groundTruths[name]
        predict = prediction[name]

        # Create figure and axes
        fig, ax = plt.subplots()
        # Display the image
        ax.imshow(im)
        # plt.show()

        # draw ground truth
        drawRectangles(ax, ground['circle'], ground['triangle'], True)
        plt.show()

        # draw prediction
        drawRectangles(ax, predict['circle'], predict['triangle'], False)
        plt.draw()
        plt.show()


        # metric
        all_true = len(ground['circle']) + len(ground['triangle'])
        count_miss = 0
        # count_success = 0

        count_miss += get_difference(ground['circle'], predict['circle'])
        # count_success += (len(ground['circle']) - count_miss)

        count_miss += get_difference(ground['triangle'], predict['triangle'])
        # count_success += (len(ground['triangle']) - count_miss)

        a = count_miss / all_true
        misses_per_image.append(a)

    print(sum(misses_per_image)/len(misses_per_image))
