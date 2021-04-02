# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html



import shutil
import os


for i in os.listdir('my_project'):
    template_dir = os.path.join('my_project', i, 'templates', i)
    if os.path.isdir(template_dir):
        templates = os.path.join('my_project', 'templates')
        shutil.copytree(template_dir, os.path.join(templates, i))
