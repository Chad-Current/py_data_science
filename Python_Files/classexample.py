def main():

class Oneclass:
    serialnumber = 1001
    def __init__(self, owner, company,sid):
        self._owner = owner
        self._company = company
        self._sid = sid
        self.serial = Oneclass.next_serial
        Oneclass.next_serial += 1
    def __call__(self):
        print(self)
class Two:
    def __init__(self):
    def __call__(self):



if __name__ == 'class':
    print(__name__)
main()
