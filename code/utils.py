import mmap

dataPath = {
    'English': '../data/english.stackexchange.com',
    'Math': '../data/math.stackexchange.com',
    'Superuser': '../data/superuser.com',
    'Stackoverflow': '../data/stackoverflow.com'}


def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines
