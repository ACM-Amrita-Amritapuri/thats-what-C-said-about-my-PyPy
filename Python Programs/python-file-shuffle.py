import os, shutil, random, tempfile


def shuffle_file(src, dst):
    lst_to_shuffle = [os.path.join(src, filename) for filename in os.listdir(src)]
    save_path = dst
    if os.path.exists(save_path):
        pass
    else:
        os.mkdir(save_path)

    shuffled_lst = []

    for file_to_shuffle in lst_to_shuffle:
        copied_file_to_shuffle = shutil.copy(file_to_shuffle, save_path)
        shuffled_lst.append(copied_file_to_shuffle)
    random.shuffle(shuffled_lst)

    temp_dir = tempfile.mkdtemp(dir=save_path)

    dst = os.path.join(temp_dir, os.path.basename(shuffled_lst[0]))
    first_file = shutil.move(shuffled_lst[0], dst)

    new_name = shuffled_lst[0]

    for i in range(1, len(shuffled_lst)):
        os.rename(shuffled_lst[i], new_name)
        new_name = shuffled_lst[i]

    shutil.move(first_file, new_name)
    os.rmdir(temp_dir)