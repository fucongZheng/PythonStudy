import configparser
from mhxyGame.project_mhxy.maps.map import Maps
from mhxyGame.project_mhxy.maps.city.city_changan import CA
# 创建 ConfigParser 对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('text.ini', encoding='Utf-8')

# 获取配置文件中所有部分的列表
sections = config.sections()

# 计算有多少个配置项
num_of_sections = len(sections)
print(f"配置文件中有 {num_of_sections} 个配置项")
class_params = {
    'Maps': ("'电脑屏幕'", '0', '0', '1920', '1080'),
    'CA':("'長安'",'760','480','1317', '766')
}
# for i in sections:
#     class_params[i] = (config.get(i, 'name'),config.get(i, 'left_one'),config.get(i, 'left_two'),config.get(i, 'right_one'),config.get(i, 'right_two'))

print(class_params)


def get_map():
    # 假设有一个存储类名称和初始化参数的字典
    # 实例化这些类
    instances = []
    for class_name, params in class_params.items():
        class_ = globals()[class_name]  # 通过类名字符串获取对应的类对象
        instance = class_(*params)  # 实例化类对象并传入参数
        instances.append(instance)

    return instances
    # 现在，instances 列表中包含了每个类的实例，并且这些实例都分别使用了特定的参数进行了初始化


m = get_map()[1]
print(m.)
