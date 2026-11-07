import os   #导入OS模块

def batch_rename(folder_path, new_name, extension=None): #定义批量重命名函数,接收三个参数:文件夹路径,新文件名前缀,文件后缀名(默认None即不过滤)
    """
    Batch rename files in a specified folder.   #函数说明: 批量重命名指定文件夹中的文件

    :param folder_path: path from folder   #参数说明: 文件夹路径
    :param new_name: new prefix for the file    #参数说明: 新文件的前缀
    :param extension: file extension to filter by (optional)    #参数说明: 要过滤的文件后缀(可选参数)
    """
    # Get all files in the folder 获取文件夹中所有的文件
    files = os.listdir(folder_path) #获取该文件夹下所有文件和子文件夹的名称,返回一个列表

    # Sort by name by a to z 按名称排序,保证顺序一致
    files.sort()    #对文件名列表按字母(A-Z)顺序进行排序,保证重命名的顺序一致

    count = 0   #初始化计数器,记录成功重命名的文件数量
    for old_name in files:  #遍历排序后的每个文件名
        # Check full path of the file name 拼接完整路径
        old_path = os.path.join(folder_path, old_name)  #将文件夹路径和文件名拼接成一个完成的文件路径,用于后续的重命名操作

        # Ignore sub folders 跳过子文件夹
        if os.path.isdir(old_path): #判断当前路径是否是文件夹
            continue    #如果是文件夹,则跳过该循环,继续处理下一个文件

        # only proceed file which match prefix if you direct it. 如果指定了后缀,只处理匹配的文件
        if extension and not old_name.lower().endswith(extension.lower()):  #如果指定了后缀过滤条件,且当前文件名不以该后缀结尾(忽略大小写)
            continue    #如果不匹配,则跳过该循环,继续处理下一个文件

        # Keep the extension if original new files 生成新文件名,保留原后缀
        _, ext = os.path.splitext(old_name) #拆分文件名和后缀, _接收文件名部分(丢弃不用), ext接收后缀部分(如.rtf)
        new_file_name = f"{new_name}_{count + 1:03d}{ext}"  #生成新文件名,格式为: 新前缀_序号(三位数,不足补零)+原后缀
        new_path = os.path.join(folder_path, new_file_name) #将文件夹路径和新文件名拼接成新的完整路径,用于后续的重命名操作

        # Rename the file 重命名
        os.rename(old_path, new_path)   #使用os.rename()函数将旧文件路径重命名为新文件路径,实现文件的重命名操作
        print(f"Renamed: {old_name} -> {new_file_name}") #打印重命名的结果,显示旧文件名和新文件名
        count += 1 #计数器加1,记录本次成功重命名

    print(f"\n Completed! Total files renamed: {count} files")  #打印完成信息,显示总共成功重命名的文件数量

# Example usage: 使用示例
batch_rename("/Users/apple/rename_folder", "python_name", ".rtf")   #调用批量重命名函数,传入文件夹路径,新文件名前缀和要过滤的文件后缀,实现对指定文件夹中所有.rtf文件的批量重命名操作
