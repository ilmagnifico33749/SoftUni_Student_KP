class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) >= 8 and any(s.isdigit() for s in value) and any(c.isupper() for c in value):
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'



# ##########################################
# Test_Code_1:
profile_with_invalid_password = Profile('My_username', 'My-password')
# ------------------------------------------
# Output_1:
# ValueError: The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.
# ##########################################
# Test_Code_2:
profile_with_invalid_username = Profile('Too_long_username', 'Any')
# ------------------------------------------
# Output_2:
# ValueError: The username must be between 5 and 15 characters.
# ##########################################
# Test_Code_3:
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
# ------------------------------------------
# Output_3:
# You have a profile with username: "Username" and password: ********
# ##########################################

