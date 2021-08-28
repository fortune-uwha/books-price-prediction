from typing import Union


class InputValidator:
    """
    A class to validate user's input for a correct structure, data types, empty strings e.t.c.
    """
    def __init__(self, input_data) -> None:
        self.__input_data = input_data

    @property
    def validate_keys(self) -> dict:
        """
        Validates input keys to ensure the correct structure of the input.
        :param: None
        :return: json response ok if keys match, errors if input is incorrect.
        """
        valid_keys = ("author", "edition", "category")
        if not all(name in self.__input_data for name in valid_keys):
            return {
                "response": "error",
                "validation_errors": "missing keys, please refer to documentation"
            }
        return {"response": "ok"}

    @property
    def validate_input(self) -> Union[list, bool]:
        """
        Validates input values and builds an error response if any errors are present.
        :param: None
        :return: json response ok if no errors, otherwise errors
        """
        validation_errors = []
        if self.validate_author_not_str:
            validation_errors.append(self.validate_author_not_str)
        if self.validate_edition_not_str:
            validation_errors.append(self.validate_edition_not_str)
        if self.validate_category_not_str:
            validation_errors.append(self.validate_category_not_str)
        if self.validate_author_name_empty:
            validation_errors.append(self.validate_author_name_empty)
        if self.validate_edition_empty:
            validation_errors.append(self.validate_edition_empty)
        if self.validate_category_empty:
            validation_errors.append(self.validate_category_empty)

        if validation_errors:
            return {
                "response": "error",
                "validation_errors": validation_errors
            }
        return {"response": "ok"}

    @property
    def validate_author_not_str(self) -> Union[str, None]:
        if not isinstance(self.__input_data["author"], str):
            return "Invalid data type for author given. Author must be a string."
        return

    @property
    def validate_edition_not_str(self) -> Union[str, None]:
        if not isinstance(self.__input_data["edition"], str):
            return "Invalid data type for edition given. Edition must be a string."

    @property
    def validate_category_not_str(self) -> Union[str, None]:
        if not isinstance(self.__input_data["category"], str):
            return "Invalid data type for book category. Category must be a string."

    @property
    def validate_author_name_empty(self) -> Union[str, None]:
        if not self.__input_data["author"]:
            return "Author cannot be empty."

    @property
    def validate_edition_empty(self) -> Union[str, None]:
        if not self.__input_data["edition"]:
            return "Edition cannot be empty."

    @property
    def validate_category_empty(self) -> Union[str, None]:
        if not self.__input_data["category"]:
            return "category cannot be empty."
