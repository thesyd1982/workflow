from functools import wraps


def error_handler(func, verbose=False):
    @wraps(func)
    def _try_except(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if verbose:
                print(str(e))
            return None
    return _try_except
