class PasswordChecker:
    def check(self, passsword):
        if len(passsword) >= 8:
            return True
        else:
            raise Exception("Invalid!! Password must be longer than 8 characters!")
