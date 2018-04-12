class bankaccount:


	def __init__(self,name,sid,checking_balance,savings_balance,checking=True,savings=False):
		self._name = name
		self._sid = sid
		self._chk_bal = checking_balance
		self._sav_bal = savings_balance
		self._chk = checking
		self._sav = savings
		self._chk_bal = checking_balance
		self._sav_bal = savings_balance


	def __call__(self):
		print('Name: ',self._name)
		if self._chk:
			print('Checking Balance $',self._chk_bal)
		if self._sav:
			print('Savings Balance $',self._sav_bal)
		print('Total Balance $',total_balance)

    def __balance__(self):
        total_balance = self._chk_bal + self._sav_bal
        print('Total Balance $',total_balance)

# def newaccount(*args):
#     newperson = bankaccount(args)

def main():
    pass




if __name__ == 'practiceclass':
    print(__name__)
    main()
