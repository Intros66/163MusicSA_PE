# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:31:22 2020

@author: Oliver
"""

import datetime
import jieba
import jieba.analyse

import matplotlib.image
import wordcloud
import src.sql_sqlite
from matplotlib.image import imread
from wordcloud import WordCloud
from src import sql_sqlite as sql


def cloudArtist(user_id, shape, font_choice):
    print("start analyse lyrics")
    startTime = datetime.datetime.now()
    print(startTime.strftime('%Y-%m-%d %H:%M:%S'))
    texts = []

    lyr = sql.get_artist(user_id)
    # lyr = sql.get_all_artist()
    texts.append(lyr)
    for n in range(len(lyr)):
        texts[0][n]['nickname'] = texts[0][n]['nickname'].replace('\xa0', '')
        # 把歌词中的\n干掉
    ShapePath = './data/wordcloud/shape/'
    color_mask = imread(ShapePath+shape)
    FontPath = './data/wordcloud/font/'
    font_mask = FontPath+font_choice
    midTime = datetime.datetime.now()
    print("获取歌手信息完毕，分析start:")
    tags = jieba.analyse.extract_tags(str(texts), 1000, withWeight=True)
    data = {item[0]: item[1] for item in tags}
    data.pop('nickname')
    word_cloud = WordCloud(scale=16,
                           font_path=font_mask,
                           background_color="white",
                           max_words=400,
                           max_font_size=100,
                           width=1920,
                           mask=color_mask,
                           height=1080,
                           random_state=42).generate_from_frequencies(data)
    # plt.figure()  # 创建一个图形实例
    # plt.imshow(word_cloud)
    # plt.axis("off")  # 不显示坐标尺寸
    # plt.savefig(r'wordcloud/'+user_id+'_artistCloud.png', dpi=400)  # 指定分辨率
    word_cloud.to_file(r'./data/wordcloud/' + user_id + '_artistCloud.png')
    # plt.show()

    print("finish analyse lyric")
    endTime = datetime.datetime.now()
    print(endTime.strftime('%Y-%m-%d %H:%M:%S'))
    print("耗时：", (endTime - startTime).seconds, "秒")

# if __name__ == '__main__':
#     cloudArtist()
