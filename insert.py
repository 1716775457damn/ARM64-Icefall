import os
import shutil

def get_file_index(filename):
    # 从文件名中提取数字索引
    return int(filename.split('ppy')[1].split('.PCM')[0])

def insert_files(input_dir, insert_dir, insert_index):
    # 读取被插入目录中的所有文件并排序
    original_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    original_files.sort(key=get_file_index)

    # 读取插入目录中的所有文件并排序
    insert_files = [f for f in os.listdir(insert_dir) if os.path.isfile(os.path.join(insert_dir, f))]
    insert_files.sort(key=get_file_index)

    # 确保插入位置有效
    if insert_index > len(original_files):
        print(f"Insert position {insert_index} is beyond the number of original files.")
        return

    # 临时存放后续文件
    temp_dir = os.path.join(input_dir, "temp")
    os.makedirs(temp_dir, exist_ok=True)

    # 移动后续文件到临时目录
    for i, filename in enumerate(original_files[insert_index:], start=insert_index):
        new_index = i + len(insert_files)
        new_filename = f"ppy{new_index:07d}.PCM"
        src_path = os.path.join(input_dir, filename)
        dst_path = os.path.join(temp_dir, new_filename)
        shutil.move(src_path, dst_path)

    # 插入新文件
    for i, insert_file in enumerate(insert_files, start=insert_index):
        new_index = i
        new_filename = f"ppy{new_index:07d}.PCM"
        src_path = os.path.join(insert_dir, insert_file)
        dst_path = os.path.join(input_dir, new_filename)
        shutil.copy2(src_path, dst_path)

    # 将文件从临时目录移回原目录
    for filename in os.listdir(temp_dir):
        new_index = get_file_index(filename) + len(insert_files)
        new_filename = f"ppy{new_index:07d}.PCM"
        src_path = os.path.join(temp_dir, filename)
        dst_path = os.path.join(input_dir, new_filename)
        shutil.move(src_path, dst_path)

    # 清理临时目录
    shutil.rmtree(temp_dir)

    # 对全部文件进行最终排序
    final_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    final_files.sort(key=get_file_index)
    for i, filename in enumerate(final_files, start=1):
        new_filename = f"ppy{i:07d}.PCM"
        src_path = os.path.join(input_dir, filename)
        dst_path = os.path.join(input_dir, new_filename)
        if src_path != dst_path:
            shutil.move(src_path, dst_path)

input_dir = r'C:\Users\陶鑫旺\Desktop\win录音工具\data\wav2'
insert_dir = r'C:\Users\陶鑫旺\Desktop\win录音工具\data\wav3'
insert_index = 10  # 定义插入位置

insert_files(input_dir, insert_dir, insert_index)