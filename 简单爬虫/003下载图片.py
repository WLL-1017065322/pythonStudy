import requests

import os

import threading


# d = 'D:\\B\\'
# path = d + url.split('=')[-1] + '.jpg'

def downPicture(url,i):
    d = 'D:\\B\\'
    path = d + url.split('=')[-1] + '.jpg'
    try:

        if not os.path.exists(d):
            os.mkdir(d)

        if not os.path.exists(path):

            r = requests.get(url)

            r.raise_for_status()

            with open(path, 'wb') as f:

                f.write(r.content)

                f.close()

                print(path, i, "图片保存成功")

        else:

            print(path, i, "图片已存在")

    except:

        print(path, "图片获取失败")


# [a-zA-z]+://[^\s]*正则 匹配url

# ([a-zA-z]+://[^\s]*) ==> '$1',
# urlList = [
#     'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-u-path-run-kids-g28109-1',
#     'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-u-path-run-kids-g28109-2' ]



urlList = [
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-u-path-run-kids-g28109-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-u-path-run-kids-g28109-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-u-path-run-kids-g28109-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-u-path-run-kids-g28109-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-u-path-run-kids-g28109-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-u-path-run-kids-g28109-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-u-path-run-kids-g28109-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-matchcourt-f37382-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-matchcourt-f37382-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-matchcourt-f37382-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-matchcourt-f37382-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-matchcourt-f37382-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-matchcourt-f37382-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-matchcourt-f37382-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1210-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1210-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1210-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1210-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1210-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1210-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1210-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1209-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1209-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1209-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1209-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1209-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1209-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-kids-db1209-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6750-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6750-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6750-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6750-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6750-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6750-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6750-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6748-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6748-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6748-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6748-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6748-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6748-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-tubular-shadow-kids-bb6748-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-gazelle-j-originals-lifestyle-shoes-bb2502-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-gazelle-j-originals-lifestyle-shoes-bb2502-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-gazelle-j-originals-lifestyle-shoes-bb2502-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-gazelle-j-originals-lifestyle-shoes-bb2502-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-gazelle-j-originals-lifestyle-shoes-bb2502-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-gazelle-j-originals-lifestyle-shoes-bb2502-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-gazelle-j-originals-lifestyle-shoes-bb2502-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-200-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-200-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-200-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-200-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-200-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-200-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-200-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-002-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-002-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-002-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-002-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-002-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-002-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-blazer-low-sd-av9373-002-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-w-aq3091-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-w-aq3091-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-w-aq3091-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-w-aq3091-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-w-aq3091-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-w-aq3091-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=adidas-superstar-w-aq3091-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-blazer-ac-xt-ah3434-100-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-blazer-ac-xt-ah3434-100-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-blazer-ac-xt-ah3434-100-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-blazer-ac-xt-ah3434-100-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-blazer-ac-xt-ah3434-100-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-blazer-ac-xt-ah3434-100-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-blazer-ac-xt-ah3434-100-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-portmore-ii-ultralight-880271-021-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-portmore-ii-ultralight-880271-021-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-portmore-ii-ultralight-880271-021-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-portmore-ii-ultralight-880271-021-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-portmore-ii-ultralight-880271-021-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-portmore-ii-ultralight-880271-021-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-portmore-ii-ultralight-880271-021-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-tanjun-se-kids-859617-004-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-tanjun-se-kids-859617-004-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-tanjun-se-kids-859617-004-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-tanjun-se-kids-859617-004-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-tanjun-se-kids-859617-004-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-tanjun-se-kids-859617-004-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-tanjun-se-kids-859617-004-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-nylon-819720-819720011-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-nylon-819720-819720011-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-nylon-819720-819720011-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-nylon-819720-819720011-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-nylon-819720-819720011-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-nylon-819720-819720011-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-nylon-819720-819720011-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719110-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719110-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719110-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719110-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719110-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719110-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719110-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719012-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719012-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719012-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719012-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719012-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719012-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-cortez-basic-leather-819719-819719012-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-classic-cortez-nylon-749864-702-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-classic-cortez-nylon-749864-702-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-classic-cortez-nylon-749864-702-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-classic-cortez-nylon-749864-702-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-classic-cortez-nylon-749864-702-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-classic-cortez-nylon-749864-702-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-women-s-classic-cortez-nylon-749864-702-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-022-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-022-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-022-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-022-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-022-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-022-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-022-22',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-020-1',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-020-2',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-020-3',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-020-4',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-020-5',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-020-21',
    'http://s7d5.scene7.com/is/image/sneakerhead/overstock_zhutumuban_nologo?$800x800$&$layer_1_src=nike-sb-stefan-janoski-kids-525104-020-22',

]

# for url in urlList:
#     downPicture(url)

for i in range(len(urlList)):
    downPicture(urlList[i], i+1)



# 进一步改善: 直接添加,不需要手动正则,即自动将分析字符串,将地址放入列表(数组)