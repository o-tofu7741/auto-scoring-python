import json
from os import path


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
    print(settings)


if __name__ == "__main__":
    main()