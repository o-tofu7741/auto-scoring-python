import json
from os import path
import glob

from Util.student import Student


def main():
    settings_file_name = "settings.json"
    target_dir_path = settings_path = ""
    while target_dir_path == "":
        try:
            print("採点対象フォルダの絶対パスを入力してください。例 : C:/hoge/huga")
            tmp_dir_path = input()
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
    student_dir_paths = glob.glob(path.join(target_dir_path, "**") + "/")
    students: list[Student] = []
    print("採点中...")
    for stu in student_dir_paths:
        students.append(Student(stu, settings["tasks"]))
    with open(path.join(target_dir_path, "result.txt"), "w", encoding="utf-8") as f:
        for stu in students:
            stu.get_results()
            f.write(stu.result)
    print("採点終了")


if __name__ == "__main__":
    main()
