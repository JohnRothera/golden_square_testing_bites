class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("Contents have already been wrapped!")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("Pressies have been unwrapped already!")
        return f"You get a {self.contents}!"
