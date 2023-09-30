from Stack import Stack


class LoopFlagsGroup(Stack):
    class LoopFlag:
        def __init__(self, group, state=True, name=None):
            self.state: bool = state
            self.group: LoopFlagsGroup = group
            self.name = name

        def __bool__(self):
            return self.state

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

    def new(self, name=None) -> LoopFlag:
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
    lf = loop_flags.new()
    if lf:
        print(lf.state)
    lf.state = False
    if not lf:
        print(lf.state)


if __name__ == '__main__':
    test()
