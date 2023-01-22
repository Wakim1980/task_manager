class Menu:
    def __init__(self):
        self._menu_items = {}

    def add_menu_item(self, item_text: str, value):
        self._menu_items[len(self._menu_items) + 1] = [item_text, value]

    def show(self):
        for index, value in self._menu_items.items():
            print(f"{index}. {value[0]}")

    def _get_associated_value(self, user_choice: int):
        if user_choice in self._menu_items.keys():
            return self._menu_items[user_choice][1]
        return None

    def _get_user_input(self, text: str):
        user_input = input(text)
        if user_input.isnumeric():
            result = int(user_input)
            if 0 < result <= len(self._menu_items):
                return result
        return None

    def get_value_from_input(self, text: str):
        user_choice = self._get_user_input(text)
        if user_choice is None:
            return None
        return self._get_associated_value(user_choice)


