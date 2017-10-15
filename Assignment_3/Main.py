from Account_Class import Account_Class
from Book_Class import BookClass

display = {
    'MENU' : ['Log in','Create Account','EXIT'],
    'MENU MASTER': ['Display Book','Display Account','Add Book','Edit Book','Add Master Account','Edit Password',
                    'Edit Account','EXIT'],
    'LIBRARY MENU' : ['Display Book','Read on Spot','Borrow Book','Book\'s you borrow','Return Books',
                      'Change your password','EXIT'],
}

def display_output(menu_type):
    x = int((22 - len(menu_type)) / 2)
    print('\n', '-' * x, menu_type.upper(), '-' * x)
    for i,j in display.items():
        if menu_type.upper() == i:
            for a in range(len(j)):
                print('[{0}] {1}'.format(a+1,j[a]))
    print('#'*(x*2+len(menu_type)+3))

def buffer_zone():
    input('Press enter to continue! ')

all_book = []
open_lbook = open('Data_Base\\List_Book.txt', "r")
for i in open_lbook.read().split('\n'):
    z = i.split(',')
    all_book.append(z)

all_acc = []
open_lacc = open('Data_Base\\List_Account.txt', "r")
for i in open_lacc.read().split('\n'):
    z = i.split(';')
    all_acc.append(z)
for i in all_acc:
    i[2] = i[2].split('|')
for i in all_acc:
    i[-2] = i[-2].split(',')

while True:
    try :
        display_output('MENU')
        x = input('Input your command!')
        if x == '1':
            display_output('LOGIN')
            print('Please enter!')
            username = input('Username   : ').upper()
            for i in all_acc:
               if username == i[0]:
                    password = input('Password   : ')
                    if password == i[1]:
                        print('Log in successful!')
                        if i[-1] == '1':
                            while True:
                                display_output('Menu Master')
                                l = input('Input your command!')
                                num = 0
                                for i in range(len(all_acc)):
                                    if username.upper() == all_acc[i][0]:
                                        num = i
                                if l == '1':
                                    display_output('Display Book')
                                    BookClass(all_book).displayBook()
                                    buffer_zone()
                                elif l == '2':
                                    display_output('Display Account')
                                    Account_Class(all_acc).displayAccount()
                                    buffer_zone()
                                elif l == '3':
                                    display_output('Add Book')
                                    BookClass(all_book).bookAdd()
                                    BookClass(all_book).updateBook()
                                    buffer_zone()
                                elif l == '4':
                                    display_output('Edit Book')
                                    y = input('Which book do you want to update?')
                                    for i in all_book:
                                        if y.title() == i[0]:
                                            BookClass(i).bookEdit()
                                    BookClass(all_book).updateBook()
                                    buffer_zone()
                                elif l == '5':
                                    display_output('Add Master Account')
                                    Account_Class(all_acc).accountAdd('1')
                                    Account_Class(all_acc).updateAccount()
                                    buffer_zone()
                                elif l == '6':
                                    display_output('Edit Password')
                                    Account_Class(all_acc[num]).passwordEdit()
                                    Account_Class(all_acc).updateAccount()
                                elif l == '7':
                                    display_output('Edit Account')
                                    z = input('Which username you wish to edit?')
                                    for i in all_acc:
                                        if z.upper()==i[0]:
                                            Account_Class(i).editAccount()
                                            Account_Class(all_acc).updateAccount()
                                    buffer_zone()
                                elif l == '8':
                                    break
                                else :
                                    print('Wrong input!')
                        else:
                            while True:
                                display_output('Library Menu')
                                s = input('Input your command!')
                                num = 0
                                for i in range (len(all_acc)):
                                    if username.upper()==all_acc[i][0]:
                                        num = i
                                if s == '1':
                                    display_output('Display Book')
                                    BookClass(all_book).displayBook()
                                    buffer_zone()
                                elif s == '2':
                                    display_output('Read on spot')
                                    y = input('Which book do you want to read on spot?')
                                    for i in all_book:
                                        if y.title() == i[0]:
                                            BookClass(i).readOnspot()
                                    buffer_zone()
                                elif s == '3':
                                    display_output('Borrow Book')
                                    BookClass(all_book).borrowBook(all_acc[num])
                                    Account_Class(all_acc).updateAccount()
                                    buffer_zone()
                                elif s == '4':
                                    display_output('Borrowed Book')
                                    BookClass(all_book).displayBook_Acc(all_acc[num])
                                    buffer_zone()
                                elif s == '5':
                                    display_output('Returning Book')
                                    BookClass(all_book).returnBook(all_acc[num])
                                    Account_Class(all_acc).updateAccount()
                                    buffer_zone()
                                elif s == '6':
                                    display_output('Edit Password')
                                    Account_Class(all_acc[num]).passwordEdit()
                                    Account_Class(all_acc).updateAccount()
                                    buffer_zone()
                                elif s == '7':
                                    break
                                else :
                                    print('Wrong input!')
                                    buffer_zone()
                    else:
                        print('Wrong password!')
                        buffer_zone()
        elif x == '2':
            display_output('Create Account')
            Account_Class(all_acc).accountAdd('0')
            Account_Class(all_acc).updateAccount()
            buffer_zone()
        elif x == '3':
            print('Thank you for visiting')
            input('Press enter to exit!')
            break
        else :
            print('Wrong input!')
            buffer_zone()
    except:
        print('Error, Please try Again!')
        buffer_zone()
