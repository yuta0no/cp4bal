import matplotlib.pyplot as plt
import numpy as np


def main():
    random_log_list = [
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/random/2025-08-18T22:20:53-8d02.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/random/2025-08-18T22:20:57-82f6.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/random/2025-08-18T22:21:02-a711.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/random/2025-08-18T22:21:07-9dd2.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/random/2025-08-18T22:21:12-45c7.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/random/2025-08-18T22:21:17-1ab9.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/random/2025-08-18T22:21:21-578b.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/random/2025-08-18T22:21:26-6c38.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/random/2025-08-18T22:21:31-390b.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/random/2025-08-18T22:21:36-9594.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/random/2025-08-18T21:57:46-0ed3.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/random/2025-08-18T21:57:51-352b.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/random/2025-08-18T21:57:55-9d37.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/random/2025-08-18T21:58:00-4ff4.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/random/2025-08-18T21:58:05-d5a9.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/random/2025-08-18T21:58:10-8ad4.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/random/2025-08-18T21:58:14-70fa.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/random/2025-08-18T21:58:19-89a7.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/random/2025-08-18T21:58:24-f3a8.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/random/2025-08-18T21:58:29-ad25.log",
    ]
    us_prop_log_list = [
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:21:33-5ae7.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:22:07-e37d.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:22:39-9469.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:23:17-b50a.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:23:52-04e2.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:24:27-04e2.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:25:01-ffc1.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:25:37-5d42.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:26:12-b217.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:26:47-116d.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T21:59:08-3816.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T21:59:27-0eeb.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T21:59:46-d6bd.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:00:06-4d94.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:00:26-10f6.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:00:46-f458.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:01:05-b980.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:01:25-96a8.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:01:45-6a36.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:02:05-f862.log",
    ]
    us_non_prop_log_list = [
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:27:37-a4af.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:28:11-7e88.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:28:43-3215.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:29:21-3a73.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:29:55-3c7a.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:30:31-9b3f.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:31:05-88db.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:31:41-37b8.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:32:17-ff17.log",
        "/home/members/ono/workspace/cp4bal/log/csbm/sgc/1/approximate_uncertainty/2025-08-18T22:32:51-5da3.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:03:24-12dc.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:03:43-1b7f.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:04:00-2bc3.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:04:21-00bc.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:04:41-8c5e.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:05:00-4823.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:05:20-023c.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:05:41-c363.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:06:01-d3e6.log",
        # "/home/members/ono/workspace/cp4bal/log/csbm/sgc/approximate_uncertainty/2025-08-18T22:06:21-fa43.log",
    ]

    random_accuracy_list = [read_accuracy_from_log(log_file) for log_file in random_log_list]
    us_prop_accuracy_list = [read_accuracy_from_log(log_file) for log_file in us_prop_log_list]
    us_non_prop_accuracy_list = [read_accuracy_from_log(log_file) for log_file in us_non_prop_log_list]

    print(np.array(random_accuracy_list).mean(axis=0))
    print(np.array(us_prop_accuracy_list).mean(axis=0))
    print(np.array(us_non_prop_accuracy_list).mean(axis=0))

    print(np.array(random_accuracy_list).std(axis=0))
    print(np.array(us_prop_accuracy_list).std(axis=0))
    print(np.array(us_non_prop_accuracy_list).std(axis=0))


def read_accuracy_from_log(log_file_path: str):
    accuracy_list = []
    with open(log_file_path, 'r') as file:
        for line in file:
            if 'Accuracy (TEST):' in line:
                parts = line.strip().split(':')
                if len(parts) > 1:
                    try:
                        accuracy_value = float(parts[-1].strip())
                        accuracy_list.append(accuracy_value)
                    except ValueError:
                        # Skip lines where the value is not a number (e.g., 'nan')
                        continue
    return accuracy_list



if __name__ == "__main__":
    main()