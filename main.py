import os

# 在当前同级目录下创建一个新的目录
# os.mkdir("dirPractice")

# 删除当前同级目录下的目录
# os.removedirs('dirPractice')

# 获取当前项目的路径
# os.getcwd()

# 判断文件是否存在
os.path.exists('main.py')

# 创建一个新的文件
if not os.path.exists('practice'):
    os.mkdir('practice')

if not os.path.exists('practice/osPractice.txt'):
    with open('practice/osPractice', 'a') as f:
        f.write('Hello World')