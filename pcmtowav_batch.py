import wave
import argparse
import os
import glob

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", required=True, help="directory containing pcm files")
parser.add_argument("-s", "--sample_rate", type=int, default=16000, help="sample rate")
parser.add_argument("-c", "--num_channels", type=int, default=1, help="number of channels")
parser.add_argument("-w", "--sample_width", type=int, default=2, help="sample width")
args = parser.parse_args()

# 获取目录中的所有PCM文件
pcm_files = glob.glob(os.path.join(args.directory, '*.pcm'))

# 遍历所有PCM文件
for pcm_path in pcm_files:
    wav_path = pcm_path.replace('.pcm', '.wav')

    # PCM文件参数
    sample_width = args.sample_width  # 16-bit
    num_channels = args.num_channels  # 单声道
    sample_rate = args.sample_rate  # 采样率

    # 打开PCM文件
    pcm_file = open(pcm_path, 'rb')

    # 创建WAV文件
    wav_file = wave.open(wav_path, 'wb')

    # 设置WAV文件参数
    wav_file.setsampwidth(sample_width)
    wav_file.setnchannels(num_channels)
    wav_file.setframerate(sample_rate)

    # 读取PCM数据，并写入WAV文件
    data = pcm_file.read()
    wav_file.writeframes(data)

    # 关闭文件
    pcm_file.close()
    wav_file.close()

    print(f"转换完成：{wav_path}")