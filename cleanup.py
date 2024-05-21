import os

SIZE_IN_MB = 1024 * 1024


def get_size(dir_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total_size += os.path.getsize(fp)
            except FileNotFoundError:
                continue
    return total_size


def print_large_directories(start_path, size_in_mb, indent_level, max_depth):
    for directory in os.listdir(start_path):
        dir_path = os.path.join(start_path, directory)
        size = get_size(dir_path)
        if size > size_in_mb * SIZE_IN_MB:  # size > 300MB
            print(f"{indent_level*'__'}Directory: {dir_path}, Size: {size / (1024 * 1024)} MB")
            if indent_level < max_depth-1:
                print_large_directories(dir_path, size_in_mb/3, indent_level+1, max_depth)


# Call the function with the directory path
print_large_directories("/home/truongchu/.cache/huggingface/hub", 1000, 0,1)
