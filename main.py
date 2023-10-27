import json
from os import path
import glob

from pprint import pprint


def main():
    settings_file_name = "settings.json"
    target_dir_path = settings_path = ""
    while target_dir_path == "":
        try:
            print("採点対象フォルダの絶対パスを入力してください。例 : C:/hoge/huga")
            tmp_dir_path = "/tmp"  # input()
            if not path.exists(tmp_dir_path):
                raise Exception("入力されたパスは存在しません。")
            if not path.isdir(tmp_dir_path):
                raise Exception("入力されたパスはフォルダではありません。")
            if not path.exists(path.join(tmp_dir_path, settings_file_name)):
                raise Exception(f"対象フォルダ内に{settings_file_name}が存在しません")
        except Exception as e:
            print(e)
        else:
            target_dir_path = tmp_dir_path
            settings_path = path.join(target_dir_path, settings_file_name)

    try:
        with open(settings_path) as f:
            settings = json.load(f)
    except Exception as e:
        print(e)
    print(settings)
    student_dir_paths = glob.glob(path.join(target_dir_path, "**") + "/")
    print(student_dir_paths)
    students_file_paths: list[list[str]] = []
    # students = list(map(lambda x: path.basename(path.dirname(x)), student_dir_paths))
    print(settings["tasks"])
    for student in glob.glob(path.join(target_dir_path, "**") + "/"):
        students_file_paths.append(glob.glob(path.join(student, "*")))
    pprint(students_file_paths)
    for file_paths in students_file_paths:
        print(file_paths)


if __name__ == "__main__":
    main()
