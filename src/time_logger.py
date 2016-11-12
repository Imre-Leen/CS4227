import time


def measure_execution_time(function):
    def measure_time(*args, **kw):
        start_time = time.time()
        result = function(*args, **kw)
        end_time = time.time()

        print "[TIME_LOGGING] Function '{}' took {} seconds".format(function.__name__,
                                                                    start_time-end_time)
        return result

    return measure_time

