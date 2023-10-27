import glob
from os import path

from Util.answer import Answer


class Student:
    def __init__(self, student_dir_path, tasks: list[dict[str]]) -> None:
        self.dir_path = student_dir_path
        # self.correct_path_list = correct_file_list
        self.answer_path_list = glob.glob(path.join(student_dir_path, "*"))
        self.answers: list[Answer] = []
        self.tasks = tasks

    def __str__(self) -> str:
        return self.dir_path

    def set_answers(self):
        for task in self.tasks:
            print(task)


if __name__ == "__main__":
    Student("hoge")
