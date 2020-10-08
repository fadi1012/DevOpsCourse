#! /bin/bash


get_script_folder() {
    relative_path=$(dirname $0)
    # requires python, but supports both mac and linux
    abs_path=$(python -c 'import os,sys ; print(os.path.realpath(sys.argv[1]))' $relative_path)
    echo ${abs_path}
}
script_folder=$(get_script_folder)
project_root=${script_folder}
pushd ${project_root}/
echo "project root is ${project_root}"
source  ${project_root}/devopscourse/bin/activate
pip install -r requirements.txt