from os import path
import subprocess
from chardet import detect
import zipfile


class Answer:
    def __init__(
        self,
        file_path: str,
        args: str = "",
        inputs: str | None = None,
    ) -> None:
        self.file_path = file_path.replace("\\", "/")
        self.code_txt: str = ""
        self.result_txt: str = ""
        self.task_name: str = path.basename(self.file_path)
        self.args = args.split()
        self.inputs = inputs
        self.file_list: list[str] = [self.task_name]

    def __str__(self) -> str:
        return (
            f"file_path : {self.file_path}\n"
            f"code_txt : {self.code_txt}\n"
            f"result_txt : {self.result_txt}\n"
            f"name : {self.task_name}\n"
            f"args : {self.args}\n"
            f"inputs : {self.inputs}\n"
        )

    # def prints(self) -> str:
    #     return (
    #         f"{' USER : ' + self.user + ' ':#^70}\n"
    #         "\n"
    #         f"FILE LIST : {self.file_list}\n"
    #         "\n"
    #         f"{' START CODE ':=^70}\n"
    #         "\n"
    #         f"{self.code_txt}\n"
    #         f"{' FINISH CODE ':=^70}\n"
    #         "\n"
    #         f"{' RESULT ' + self.user + ' ':-^70}\n"
    #         f"{self.result_txt}\n"
    #     )

    # def get_user_name(self):
    #     for i in self.file_path.replace("\\", "/").split("/"):
    #         if "@" in i:
    #             return i.split("@")[0]
    #     else:
    #         return self.file_path

    def get_code(self):
        try:
            if self.file_path.endswith((".jar", ".zip")):
                self.code_txt, f_list = unpack_files(
                    self.file_path, get_encoding_type(self.file_path)
                )
                self.file_list += f_list
            else:
                with open(self.file_path, encoding=get_encoding_type(self.file_path)) as f:
                    self.code_txt = f.read().strip()
        except Exception as e:
            self.code_txt = "Open Error : " + self.file_path + "\n手動で確認してくれい"
            print(self.file_path, e)

    def execute(self):
        if self.task_name.endswith(".jar"):
            cmd = ["java", "-jar", self.file_path] + self.args
        elif self.task_name.endswith(".java"):
            cmd = ["java", self.file_path] + self.args
        else:
            self.result_txt = "cmd error"
            return

        result = subprocess.run(
            cmd,
            # encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=self.inputs,
        )
        self.result_txt = (
            result.stdout.decode(detect(result.stdout)["encoding"]).strip()
            if result.stdout
            else "exec error"
        )


def get_encoding_type(file_path: str):
    with open(file_path, "rb") as f:
        rawdata = f.read()
    return detect(rawdata)["encoding"]


def unpack_files(file_path, file_encoding):
    texts: str = ""
    file_list: list[str] = []
    with zipfile.ZipFile(file_path, metadata_encoding=file_encoding) as zf:
        for info in zf.infolist():
            if info.is_dir():
                # print(info.filename)
                continue  # ディレクトリならスキップ

            if not info.filename.endswith((".txt", ".java", ".c")):
                # print(info.filename)
                continue  # .txt 以外のファイルもスキップ

            # ファイルのバイトデータを読み込んでテキストに変換する
            text = zf.read(info).decode("utf-8").strip()
            # print(f"=== {info.filename} ===")
            # print(text)
            texts += f"{' ' + path.basename(info.filename) + '' '':-^70}\n{text}\n\n"
            file_list.append(path.basename(info.filename))
    return texts.strip() if texts != "" else "対象ファイル無し", file_list


if __name__ == "__main__":
    import glob
    from pprint import pprint

    lst = glob.glob("./tmp/*/*.*", recursive=True)
    pprint(lst)
    with open("answers.txt", "w", encoding="utf-8") as f:
        for ans in lst:
            test = Answer(ans, args="test.txt")
            test.get_code()
            # print(test.code_txt)
            test.execute()
            # print(test.result_txt)
            # print(test, end="\n" * 5, file=f)
            # print(test.prints(), end="\n" * 10, file=f)
