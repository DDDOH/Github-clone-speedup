import os
import sys
import getopt
import subprocess
import re


def main(argv):
    # read args
    try:
        opts, args = getopt.getopt(
            argv, "h:u:r", ["help", "url=", "recursive"])
        # TODO opts, args = getopt.getopt(argv, "h:u:t:", ["help", "url=", "target="])
    except getopt.GetoptError:
        print("""
update_github_mirror.py -u <url> -r

Script for speeding github clone. Support recursively clone.

Example usage:
    With recursively clone:
    update_github_mirror.py -u -r https://github.com/taichi-dev/taichi.git
    this is equivalent to execute 'git clone --recursive https://github.com/taichi-dev/taichi.git'
    
    Without recursively clone:
    update_github_mirror.py -u https://github.com/taichi-dev/taichi.git
    this is equivalent to execute 'git clone https://github.com/taichi-dev/taichi.git'"""
              )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('update_github_mirror.py -u <url> -t <target_path>')
            sys.exit()
        elif opt in ("-u", "--url"):  # 'https://github.com/pytorch/pytorch'
            url = arg
        elif opt in ("-r", "--recursive"):
            recursive_flag = True
        # elif opt in ("-t", "--target"):
        #     target = arg

    # clone repo
    url = re.sub("//github.com/", "//github.com.cnpmjs.org/", url)
    repo_name = url[url.rfind('/')+1:-4]
    print('Clone main module.............')
    list_files = subprocess.run(["git", "clone", url])
    git_path = os.path.join(os.getcwd(), repo_name)  # 文件夹目录


    if recursive_flag:
        # update .gitmodules
        g = os.walk(git_path)

        def update_git_path(path, file):
            f1 = open(path + "/" + file, 'r').read()  # 把整个文件读进来作为整个字符串
            n_matched = len(re.findall("//github.com/", f1))
            f1 = re.sub("//github.com/",
                        "//github.com.cnpmjs.org/", f1)  # 替换所有符合的情况
            f_w = open(path + "/" + file, 'wb')  # 新建一个文件，把替换后的内容写进去
            f_w.write(f1.encode())
            return n_matched

        # record results
        n_file_replaced = 0
        n_link_replaced = 0
        updated_path_list = []

        for path, dir_list, file_list in g:
            for file_name in file_list:
                if file_name == '.gitmodules':
                    n_match = update_git_path(path, file_name)
                    if n_match != 0:
                        updated_path_list.append(path)
                        n_file_replaced += 1
                        n_link_replaced += n_match

        # print results
        print('Clone submodules...........')
        if n_file_replaced == 0:
            print('All links have been updated.')
        else:
            print('Path to updated files:')
            for updated_path in updated_path_list:
                print(updated_path)
            print('\n{} links are updated.'.format(n_link_replaced))

        # clone submodules
        os.chdir(git_path)
        subprocess.run(["git", "submodule", "update", "--init", "--recursive"])


if __name__ == "__main__":

    main(sys.argv[1:])
