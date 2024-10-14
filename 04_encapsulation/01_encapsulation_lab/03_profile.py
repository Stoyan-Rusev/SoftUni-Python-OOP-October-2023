class Profile:
    def __init__(self, username: str, password: str):
        self.name = username
        self.password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 5 <= len(name) <= 15:
            self.__name = name
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        is_long_enough = len(password) >= 8
        have_digit = False
        have_upper = False

        for ch in password:
            if ch.isupper():
                have_upper = True
            elif ch.isdigit():
                have_digit = True

        if is_long_enough and have_digit and have_upper:
            self.__password = password
        else:
            raise ValueError("The password must be 8 or more characters "
                             "with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return (f'You have a profile with username: '
                f'"{self.name}" and password: {"*" * len(self.password)}')


profile_one = Profile('Stoyan', 'sdafafs1G')
print(profile_one.name)
print(profile_one.password)
print(profile_one)
print()
profile_two = Profile('Gosho', 'asdadk2F')
print(profile_two.name)
print(profile_two.password)
print(profile_two)
