# 本文件是云计算器的一部分。
#
# 云计算器是自由软件：你可以再分发之和/或依照由自由软件基金会发布的 GNU 通用公共许可证修改之，无论是版本 3 许可证，还是（按你的决定）任何以后版都可以。
#
# 发布云计算器是希望它能有用，但是并无保障;甚至连可销售和符合某个特定的目的都不保证。请参看 GNU 通用公共许可证，了解详情。
#
# 你应该随程序获得一份 GNU 通用公共许可证的复本。如果没有，请看 <https://www.gnu.org/licenses/>.
#
# This file is part of WebCalculator.
#
# WebCalculator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# WebCalculator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with WebCalculator. If not, see <https://www.gnu.org/licenses/>.
from .Stack import Stack


class LoopFlagsGroup(Stack):
    class LoopFlag:
        def __init__(self, group, name: str, state=True, max_repeat: int = -1):
            self.state: bool = state
            self.group: LoopFlagsGroup = group
            if name in [flag.name for flag in self.group.stack]:
                raise ValueError(f"LoopFlag {name} already exists")
            self.name = name
            self.max_repeat = max_repeat
            self.repeat_count: int = 0
            self.over_repeat: bool = False

        def __bool__(self):
            return self.state

        def repeat_once(self):
            if 0 < self.max_repeat == self.repeat_count:
                self.over_repeat = True
                self.break_loop()
            self.repeat_count += 1

        def repeat_clear(self):
            self.repeat_count = 0

        def end(self):
            self.state = False
            while self.group.pop() is not self:
                continue
            return

        def break_loop(self):
            self.state = False

        def resume(self):
            self.state = True

        def set_state(self, state):
            self.state = state

        @property
        def break_flag(self):
            return not self.state

        def __str__(self):
            return str(self.state)

    def __init__(self):
        super().__init__()

    def new(self, name: str) -> LoopFlag:
        self.push(self.LoopFlag(group=self, name=name))
        return self.top_element()

    def break_top(self):
        self.top_element().break_loop()

    def break_all(self):
        for flag in self:
            flag.break_loop()

    def end(self):
        self.top_element().end()


def test():
    loop_flags = LoopFlagsGroup()
    lf = loop_flags.new("1")
    if lf:
        print(lf.state)
    lf.state = False
    if not lf:
        print(lf.state)


if __name__ == '__main__':
    test()
