#!/bin/bash

function get_branches {
    remote_url=$1
    branches=($(git ls-remote --heads $remote_url | awk -F'/' '{print $NF}'))
    echo "${branches[@]}"
}

function log_info {
    echo "[INFO] $1"
}

function clone_or_update_repo {
    repo_url=$1
    path_to_folder=$2
    branch=$3

    if [ -d $path_to_folder ]; then
        (cd $path_to_folder && git fetch origin && git reset --hard origin/$branch)
        log_info "Repository updated: $path_to_folder"
    else
        git clone $repo_url --branch $branch --single-branch $path_to_folder
        log_info "Repository cloned: $path_to_folder"
    fi
}

function create_timestamp_file {
    repo_folder=$1
    branch=$2

    timestamp=$(date +"%Y-%m-%d:%H-%M-%S")
    filename="${timestamp}_${branch}.txt"
    file_path="$repo_folder/$filename"

    echo -e "Timestamp: $timestamp\nRepository: $repo_folder\nBranch: $branch" > $file_path
    log_info "Created timestamp file: $file_path"
}

function upload_file_to_repo {
    repo_folder=$1
    branch=$2

    cd $repo_folder
    git add *.txt
    git commit -m "Add timestamp file for branch $branch"
    git push origin $branch
    cd ..
    log_info "Uploaded timestamp file for branch: $branch to repository: $repo_folder"
}

function process_repositories {
    repo_url_list=("$@")

    log_info "Logging started"

    for repo_url in "${repo_url_list[@]}"; do
        repo_name=$(basename $repo_url | sed 's/\.git//')
        branches=($(get_branches $repo_url))

        for branch in "${branches[@]}"; do
            path_to_folder="$repo_name/$branch"
            clone_or_update_repo $repo_url $path_to_folder $branch
            create_timestamp_file $path_to_folder $branch
            upload_file_to_repo $path_to_folder $branch
        done
    done

    log_info "End of logging"
}


repositories=(
    'https://github.com/TestTaskGitHub/First-Repository.git'
    'https://github.com/TestTaskGitHub/Second-Repository.git'
    'https://github.com/TestTaskGitHub/Third-Repository.git'
)

process_repositories "${repositories[@]}"
