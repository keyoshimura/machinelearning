'''
物体検出の推論用エンドポイントが立ち上がっている状態で、画像を推論するときのスクリプト。
下記はやっていることの流れ。

1.必要なモジュールのインポート
2.パラメータの指定
3.結果描写用の関数を作成
4.エンドポイントから「予測結果」を取得
5.表示
'''


################################################
# 1.必要なモジュールのインポート                    #
################################################

import json
import numpy as np
import boto3
import PIL.Image as pil_img

runtime = boto3.Session(region_name='ap-northeast-1').client(service_name='sagemaker-runtime')


################################################
# 2.パラメータの指定                              #
# 分類クラス、エンドポイント、対象画像を指定          #
################################################

# 2-1.分類クラスを指定
object_categories = ['person', 'bicycle', 'car',  'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat', 
                     'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog',
                     'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag',
                     'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat',
                     'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
                     'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot',
                     'hot dog', 'pizza', 'donut', 'cake', 'chair', 'sofa', 'pottedplant', 'bed', 'diningtable',
                     'toilet', 'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven',
                     'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier',
                     'toothbrush']


# 2-2.推論用エンドポイントを指定
endpoint_name = 'object-detection-2018-09-17-09-52-12-041'

# 2-3.対象画像を指定
img = open('/Users/yoshimura.keta/Downloads/000000002587.jpg', 'rb').read()


################################################
# 3.推論結果を綺麗にする関数を作成                  #
# 閾値でのフィルタリング、 クラスの重複を削除         #
################################################

def listup_obj(result, thresh):
    '''
    result:推論エンドポイントから取得した結果
    thresh:閾値。
    '''
    list_obj = []
    result_list = result['predictions']
    for det_list in result_list:
        for det in det_list['prediction']:
            (klass, score, _x0, _y0, _x1, _y1) = det
            if score < thresh:
                continue
            cls_id = int(klass)
            list_obj.append(object_categories[cls_id])

    # 重複を削除した状態で結果を返す
    return list(set(list_obj))


################################################
# 4.推論エンドポイントから予測結果を取得             #
################################################

# Call your model for predicting which object appears in this image.
response = runtime.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType='image/jpeg',
    Body=bytearray(img)
)
# read the prediction result and parse the json
result = response['Body'].read()
result = json.loads(result)


################################################
# 5.実行                                        #
################################################
list_object = listup_obj(result, thresh = 0.7)
print(list_object)