#!/usr/bin/env python3
import subprocess
from statistics import median

if __name__ == "__main__":
    count = 10
    auto_vec_times = []
    vector_times = []
    
    print("Running auto_vec")
    for i in range(count):
        result = subprocess.run(
            ["./euler3d_cpu_double", "../../data/cfd/fvcorr.domn.193K"], stdout=subprocess.PIPE)
        splited_lst = result.stdout.decode("utf-8").split()
        find_index = splited_lst.index("time:")
        auto_vec_times.append(float(splited_lst[find_index + 1]))

    print("Running vector")
    for i in range(count):
        result = subprocess.run(
            ["./euler3d_cpu_double_rtcheck", "../../data/cfd/fvcorr.domn.193K"], stdout=subprocess.PIPE)
        splited_lst = result.stdout.decode("utf-8").split()
        find_index = splited_lst.index("time:")
        vector_times.append(float(splited_lst[find_index + 1]))

    median_auto_vec_t = median(auto_vec_times)
    median_vector_t = median(vector_times)

    print(f"Auto-vec: {median_auto_vec_t}s, Intrinsic: {median_vector_t}s")
