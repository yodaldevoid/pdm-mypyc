from typing import List, NoReturn

from onepm.base import PackageManager


class Poetry(PackageManager):
    name = "poetry"

    def get_command(self) -> List[str]:
        return [self.find_executable(self.name)]

    def install(self, *args: str) -> NoReturn:
        if self.has_unknown_args(args, ["E", "extras"]):
            command = "add"
        else:
            command = "install"
        self.execute(command, *args)

    def uninstall(self, *args: str) -> NoReturn:
        self.execute("remove", *args)

    def update(self, *args: str) -> NoReturn:
        self.execute("update", *args)

    def run(self, *args: str) -> NoReturn:
        self.execute("run", *args)
