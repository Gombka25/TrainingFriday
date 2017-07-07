
def gui_interaction(func):

    def wrapper(*args, **kwargs):
        print("Gui interaction starts")
        result = func(*args, **kwargs)
        print("Gui interaction done")
        return result
    return wrapper()

def click_some_element():
    print("I try to click element")