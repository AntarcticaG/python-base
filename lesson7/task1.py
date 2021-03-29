# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


import os

starter = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for key in starter:
   if not os.path.exists(key):
      os.mkdir(key)
   way = os.path.abspath(key)
   print(way)
   for name_direct in starter[key]:
      if not os.path.exists(name_direct):
         dir_path = os.path.join(key, name_direct)
         os.mkdir(dir_path)


# как лучше хранить конфигурацию этого стартера,
# чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

# Мне кажется словарь будет достаточно удобен,
# да, расширять конфигурацию в таком случае можно


