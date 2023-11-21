from aip import AipOcr

# 设置你的APPID/AK/SK
APP_ID = '43257106'
API_KEY = 'B4fzZ7ltiK6TWW3VkOnujO0p'
SECRET_KEY = 'GaCIaxKPbGLTFsyZMkKNOzKSGxAmCOMY'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 调用通用文字识别接口
image = get_file_content('test.png')
result = client.basicGeneral(image)  # 调用百度OCR的通用文字识别接口
print(result)
# for word in result['words_result']:
#     print(word['words'])
