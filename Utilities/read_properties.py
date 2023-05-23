import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_user_name():
        user_name = config.get('common info', 'user_name')
        return user_name

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
