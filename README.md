# Github-clone-speedup
加速 Github clone，支持 recursive 命令。

### 什么时候需要 Github-clone-speedup？

TODO

### 如何使用 Github-clone-speedup？

**Example usage**

With recursively clone:

update_github_mirror.py -u -r https://github.com/taichi-dev/taichi.git

this is equivalent to execute 'git clone --recursive https://github.com/taichi-dev/taichi.git'

​    

Without recursively clone:

update_github_mirror.py -u https://github.com/taichi-dev/taichi.git

this is equivalent to execute 'git clone https://github.com/taichi-dev/taichi.git'"""



TODO

<img src="/Users/hector/Desktop/Github-clone-speedup/README_img/image-20211224201807413.png" alt="image-20211224201807413" style="zoom:50%;" />



### Future Planning

- [ ] Support for cloning to a different path.



### Requirements

Only Python 3 is needed. Any specific version of Python should be fine. No package requirement.

### Contributing

This script is only tested by myself on Mac OS. The compatibality to the Windows Linux system has not been verified. If you encounter an error, or have more feature requirements, better implementation, suggestions for documents, etc. please make a PR or post a issue.
