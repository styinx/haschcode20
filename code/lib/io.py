class Log:
    debug = True

    @staticmethod
    def log(*args):
        if Log.debug:
            print(*args)


def log(*args):
    Log.log(*args)


