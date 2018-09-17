'''
VoTTで作成したアノテーションファイルは全ての画像データをまとめた形になっている。
SageMakerでは「画像ごと」にアノテーションファイルが必要。
なので、このスクリプトで「全ての画像データのアノテーションファイル」から「画像ファイル単位」にアノテーションファイルを出力する。

・処理内容の概要
「file_name」変数に指定したアノテーションファイルを参照して、「json」フォルダに「画像単位」のアノテーションファイルを出力する。

・参考
https://dev.classmethod.jp/cloud/aws/sagemaker-umaibo-object-detection/
'''


import json

# 1.参照するアノテーションファイルを指定
# VoTTで作成した「全画像のアノテーションファイル」を想定
file_name = 'data.json'

# 2.分類対象クラスを辞書型で登録
# VoTTで指定したものと同じものにすること
class_list = {'cuisine':0, 'man':1, 'glasses':2}

# 3.画像単位でのアノテーションファイルを出力
with open(file_name) as f:
    js = json.load(f)
 
    for k, v in js['frames'].items():
 
        k = int(k)
        line = {}
        line['file'] = '{0:04d}'.format(k+1) + '.jpg'
        line['image_size'] = [{
            'width':int(v[0]['width']),
            'height':int(v[0]['height']),
            'depth':3
        }]
 
        line['annotations'] = []
 
        for annotation in v:
 
            line['annotations'].append(
                {
                    'class_id':class_list[annotation['tags'][0]],
                    'top':int(annotation['y1']),
                    'left':int(annotation['x1']),
                    'width':int(annotation['x2'])-int(annotation['x1']),
                    'height':int(annotation['y2']-int(annotation['y1']))
                }
            )
 
        line['categories'] = []
         
        for name, class_id in class_list.items():
 
            line['categories'].append(
                {
                    'class_id':class_id,
                    'name':name
                }
            )
 
        f = open('./json/'+'{0:04d}'.format(k+1) + '.json', 'w')
        json.dump(line, f)