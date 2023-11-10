import glob
from os import path

from Util.answer import Answer


class Student:
    def __init__(self, student_dir_path: str, tasks: list[dict[str, str]]) -> None:
        self.dir_path = student_dir_path.replace("\\", "/")
        self.user = path.basename(path.dirname(self.dir_path)).split("@")[0]
        self.answers: list[Answer] = []
        self.tasks = tasks
        self.not_exists_tasks: list[str] = []
        self.result: str = ""

    def set_answers(self):
        ans_abs_paths = glob.glob(path.join(self.dir_path, "*"))
        ans_names = list(map(path.basename, ans_abs_paths))
        for task in self.tasks:
            if task["name"] in ans_names:
                self.answers.append(
                    Answer(
                        path.join(self.dir_path, task["name"]),
                        task.get("args", ""),
                        task.get("input"),
                    )
                )
            else:
                self.not_exists_tasks.append(task["name"])

    def get_results(self):
        self.set_answers()
        self.result += (
            f"{' USER : ' + self.user + ' ':#^70}\n\n"
            f"左記の課題ファイル無し or 名前ミス : {' ,'.join(self.not_exists_tasks) if self.not_exists_tasks else 'ミスしているファイルはありません'}\n\n"
        )

        for ans in self.answers:
            ans.get_code()
            ans.execute()
            self.result += (
                f"{' 課題 : ' + ans.task_name + ' ':=^70}\n\n"
                f"FILE LIST : {ans.file_list}\n\n"
                f"{' コード ':-^70}\n\n"
                f"{ans.code_txt}\n\n"
                f"{' 実行結果 ' + ans.task_name + ' ':~^70}\n\n"
                f"{ans.result_txt}\n\n\n\n"
            )


if __name__ == "__main__":
    hoge = Student(
        "C:/github/auto-scoring-python/tmp/20J5-129@20j5129",
        [{"name": "Expand.java"}, {"name": "Loop.java"}],
    )
    hoge.set_answers()
    hoge.get_results()
    print(hoge.result)
