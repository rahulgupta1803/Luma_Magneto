import configparser



config = configparser.RawConfigParser()
fpath = "D:\\credence\\Luma_Magneto_Pytest_Project\\configuration\\config.ini"
config.read(fpath)

class ReadConfig():
    @staticmethod
    def getUserEmail():
        email = config.get('commondata','Email')
        return email

    @staticmethod
    def getUserPassword():
        password = config.get("commondata","Password")
        return password
