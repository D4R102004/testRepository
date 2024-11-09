from typing import Callable, TypeVar, Dict ,Any
# Define a generic type variable T
T = TypeVar('T')


class UserInput:
    # This method allows the user to input an array
    @staticmethod
    def cycle_get_input(message: str, t: type) -> list[Any]:
        result = []
        while True:
            item = UserInput.get_input(message, t)
            if item is None:
                break
            result.append(item)
        return result

    # This method makes sure that the user inputs something of a desired type
    # even giving him the option to cancel its request at a given point.
    @staticmethod
    def get_input(message: str, t: type) -> Any:
        while True:
            print("Enter 'quit' to stop")
            user_input = input(message)
            try:
                if user_input.lower() == "quit":
                    print("Exiting...")
                    return None
                if t == int:
                    number = float(user_input)
                    if number.is_integer():
                        return int(number)
                    else:
                        raise ValueError("Invalid input. Please try Again")
                elif t == str:
                    return str(user_input)
                elif t == float:
                    number = float(user_input)
                    if number.is_integer():
                        return int(number)
                    return number
                else:
                    raise ValueError("Invalid input. Please try Again")
            except ValueError:
                print(f"Input '{user_input}' is not of type '{t.__name__}'. \nPlease try again")


class ListUtils:
    # This method takes a certain number of conditions, and returns a dictionary with
    # keys being said conditions' names. It is very similar to filter method, but it's
    # more efficient, because it only goes through the list once.
    @staticmethod
    def filter_by_conditions(input_list: list[T], *conditions: Callable[[T], bool]) -> Dict[str, list[T]]:
        results = {getattr(condition, "__name__", str(condition)): [] for condition in conditions}
        for item in input_list:
            for condition in conditions:
                if condition(item):
                    condition_name = getattr(condition, "__name__", str(condition))
                    results[condition_name].append(item)
        return results





