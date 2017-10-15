from Library_Book.Assignment_3.Add import Add
from Library_Book.Assignment_3.Edit import Edit


class Account_Class(Add, Edit):
    def __init__(self, content):
        self.__content = content
        Add.__init__(self, self.__content)
        Edit.__init__(self, self.__content)

    def accountAdd(self,p):
        fname = input('First Name          : ')
        lname = input('Last Name           : ')
        gender = input('Gender              : ')
        email = input('Email               : ')
        birth = input('Birthday DD/MM/YYYY : ')
        Add.addAccount(self, fname, lname, gender, email, birth,p)

    def updateAccount(self):
        open('Data_Base\\List_Account.txt', "w").write('')
        up_date = open('Data_Base\\List_Account.txt', "a")
        for i in range (len(self.__content)):
            a = ''
            z = self.__content[i]
            for b in range(1,len(z[-2])):
                if i == 0:
                    a = z[-2][b]
                else:
                    a = a +','+ str(z[-2][b])
            if i == 0:
                up_date.write(
                    '{0};{1};{2}|{3}|{4}|{5};{6};{7};{8}'.format(z[0], z[1], z[2][0], z[2][1], z[2][2], z[2][3], z[3],
                                                                 a, z[5]))
            else:
                up_date.write(
                    '\n{0};{1};{2}|{3}|{4}|{5};{6};{7};{8}'.format(z[0], z[1], z[2][0], z[2][1], z[2][2], z[2][3], z[3],
                                                                   a, z[5]))
        up_date.close()

    def editAccount(self):
        fname = input('First Name          : ')
        lname = input('Last Name           : ')
        pasw = input('Password            : ')
        email = input('Email               : ')
        self.__content[2][0] = fname
        self.__content[2][1] = lname
        self.__content[1] = pasw
        self.__content[2][3] = email

    def passwordEdit(self):
        password_old = input('Please input password ')
        while password_old == self.__content[1]:
            password_new = input('Please input new password ')
            ver_password_new = input('Please input new password verification ')
            if password_new == ver_password_new and len(password_new) >= 8:
                self.__content[1] = password_new
                break
            else:
                print('Error, Either your password less than 8 or password can\'t be verified!')

    def displayAccount(self):
        count = len(self.__content)
        while count != 0:
            if count >= 5:
                for i in range(5):
                    print('[{0}]'.format(len(self.__content) - count + 1), self.__content[-count][0], end=' ')
                    count -= 1
                print('')
            else:
                for i in range(count):
                    print('[{0}]'.format(len(self.__content) - count + 1), self.__content[-count][0], end=' ')
                    count -= 1
        print('\n')
