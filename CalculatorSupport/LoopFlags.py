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
