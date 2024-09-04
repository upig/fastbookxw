import os
from PIL import Image

def compress_images(directory, output_directory, quality=25):
    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # 遍历指定文件夹
    for filename in os.listdir(directory):
        # 构建完整的文件路径
        file_path = os.path.join(directory, filename)
        
        # 检查文件是否是文件并且是图像文件
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 打开图像
            img = Image.open(file_path)
            
            # 处理不支持透明度的图像格式，例如JPEG
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                img = img.convert('RGB')
            
            # 构建输出文件名，改为.jpg后缀
            base_filename = os.path.splitext(filename)[0]
            output_path = os.path.join(output_directory, f"{base_filename}.jpg")
            
            # 保存压缩后的图像为JPEG格式
            img.save(output_path, 'JPEG', quality=quality)
            print(f'Compressed and saved {filename} as {output_path}')



# 设置源文件夹和目标文件夹路径
source_directory = './ballimg/selectimg/full3'
target_directory = './ballimg/selectlittle/full3'

# 调用函数
compress_images(source_directory, target_directory)
