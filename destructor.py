class xyz:
    def _init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destructor called")
obj=xyz()
del obj
