import glob
import shutil

file_name = 'diabetes.xlsx'
full_name = 'raw_results_100/' + file_name

for i in range(100):
    src_dir = full_name

    dst_dir4 = "raw_results_100/db_0rand_missing_attr" + str(i + 1) + ".xlsx"
    dst_dir5 = "raw_results_100/db_0rand_missing_measure" + str(i + 1) + ".xlsx"
    dst_dir6 = "raw_results_100/db_0rand_missing_a_m" + str(i + 1) + ".xlsx"

    #shutil.copy(src_dir, dst_dir1)
    #shutil.copy(src_dir, dst_dir2)
    #shutil.copy(src_dir, dst_dir3)
    shutil.copy(src_dir, dst_dir4)
    shutil.copy(src_dir, dst_dir5)
    shutil.copy(src_dir, dst_dir6)
