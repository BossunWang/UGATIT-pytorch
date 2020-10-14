import os
from shutil import copyfile
import tqdm


def copy_files_from_dir(source_data_dir, source_sub_dir_list, target_dir):
    for dir in tqdm.tqdm(source_sub_dir_list):
        for root, _, fnames in sorted(os.walk(source_data_dir + dir)):
            for fname in fnames:
                source_path = os.path.join(root, fname)
                target_path = os.path.join(target_dir, dir + '_' + fname)
                copyfile(source_path, target_path)

def main():
    source_data_dir = '../face_dataset/CASIA-maxpy-clean_crop/'
    target_data_dir = '../face_dataset/CASIA/'

    source_sub_dir = os.listdir(source_data_dir)
    target_sub_dir = os.listdir(source_data_dir)

    assert len(source_sub_dir) == len(target_sub_dir)

    test_count = len(source_sub_dir) // 10

    trainA_source_dir = source_sub_dir[:-test_count]
    trainB_source_dir = target_sub_dir[:-test_count]
    testA_source_dir = source_sub_dir[-test_count:]
    testB_source_dir = target_sub_dir[-test_count:]

    trainA_target_dir = target_data_dir + 'trainA'
    trainB_target_dir = target_data_dir + 'trainB'
    testA_target_dir = target_data_dir + 'testA'
    testB_target_dir = target_data_dir + 'testB'

    copy_files_from_dir(source_data_dir, trainA_source_dir, trainA_target_dir)
    copy_files_from_dir(source_data_dir, trainB_source_dir, trainB_target_dir)
    copy_files_from_dir(source_data_dir, testA_source_dir, testA_target_dir)
    copy_files_from_dir(source_data_dir, testB_source_dir, testB_target_dir)


if __name__ == "__main__":
    main()
