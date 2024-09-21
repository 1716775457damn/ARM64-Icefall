import os

# 定义原始文件所在的目录，注意使用双反斜杠或原始字符串
# source_dir = r'C:\Users\陶鑫旺\Desktop\win录音工具\MusicFile'
source_dir = r'C:\Users\陶鑫旺\Desktop\win录音工具\data\wav2'
# 确保源目录存在
if not os.path.exists(source_dir):
    print(f"Error: The directory {source_dir} does not exist.")
else:
    # 获取所有 .PCM 文件并按创建时间排序
    files = [f for f in os.listdir(source_dir) if f.endswith('.PCM')]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(source_dir, x)))

    # 定义重命名的起始编号
    a1 = 1

    # 遍历文件列表并重命名
    for file in files:
        # 构建完整的原始文件路径
        original_file_path = os.path.join(source_dir, file)

        # 格式化新的文件名
        new_filename = f"ppy{str(a1).zfill(7)}.PCM"

        # 构建完整的新文件路径
        new_file_path = os.path.join(source_dir, new_filename)

        # 检查新文件名是否已存在
        if not os.path.exists(new_file_path):
            # 重命名文件
            os.rename(original_file_path, new_file_path)
            print(f"Renamed '{file}' to '{new_filename}'")
        else:
            print(f"Skipped renaming '{file}' because '{new_filename}' already exists.")

        # 增加编号
        a1 += 1

    print("Finished renaming files.")