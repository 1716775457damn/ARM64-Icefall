import os
import shutil

def sort_and_rename_files(directory):
    # 获取目录中的所有文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    # 根据文件名中的数字排序文件
    files.sort(key=lambda x: int(x.split('ppy')[1].split('.PCM')[0]))

    # 重命名文件
    for i, filename in enumerate(files, start=1):
        new_filename = f"ppy{i:07d}.PCM"
        src_path = os.path.join(directory, filename)
        dst_path = os.path.join(directory, new_filename)
        shutil.move(src_path, dst_path)
        print(f"Renamed '{filename}' to '{new_filename}'")

# 定义目录路径
directory = r'C:\Users\陶鑫旺\Desktop\win录音工具\data\wav2'

# 调用函数
sort_and_rename_files(directory)