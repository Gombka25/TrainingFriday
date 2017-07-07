from HTTPRequest import check_internet_connection
import time


#print(check_internet_connection())


def wait_until(condition, timeout=10, raise_exception=True, msg=""):

    baseTime = time.time()

    while  time.time() - baseTime < 10.0:
        if condition():
            return True
        time.sleep(0.1)

    if raise_exception:
        raise TimeoutError(f"{msg} after {timeout} sec")
    else:
        return False

# wait_until(check_internet_connection, msg='No connection')

"""Wait until the condition returned by 'condition' function is fulfilled,
    or the timeout is expired. The condition should be checked every 100ms

    Args:
        condition: a function that checks a condition and returns True or False
        timeout: maximal timeout after which the function will raise TimeoutException
                or return False (if raise_exception is False)
        msg: message added to the TimeoutException
    Returns:
        True when the condition is fulfilled within the timeout,
        False when the condition is not fulfilled within the timeout
                and 'raise_exception' is False
    Raises:
        TimeoutException: if raise_exception is True
                        and the condition is not fulfilled within timeout

    """

