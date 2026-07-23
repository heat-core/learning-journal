class ExceptionProxy(Exception):
    def __init__(self, message, function):
        self.message = message
        self.function = function




def transform_exceptions(func_ls: list) -> list[ExceptionProxy]:
    result = []
    for func in func_ls:
        try:
            func()
            err = ExceptionProxy("ok!", func)
            result.append(err)



        except Exception as e:
            err = ExceptionProxy(str(e), func)
            result.append(err)

    return result



