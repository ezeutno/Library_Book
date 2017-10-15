from Library_Book.Assignment_3.Add import Add
from Library_Book.Assignment_3.Edit import Edit

class BookClass(Add,Edit):
    def __init__(self,book_content):
        self.__content = book_content
        Add.__init__(self,self.__content)
        Edit.__init__(self,self.__content)

    def updateBook(self):
        open('Data_Base\\List_Book.txt', "w").write('')
        up_date = open('Data_Base\\List_Book.txt', "a")
        for i in range (len(self.__content)):
            z = self.__content[i]
            if i == 0:
                up_date.write('{0},{1},{2}'.format(z[0],z[1],z[2]))
            else :
                up_date.write('\n{0},{1},{2}'.format(z[0], z[1], z[2]))
        up_date.close()

    def bookAdd(self):
        book_name = input('Please input book name ').title()
        book_qty = input('Please input book quantity ')
        Add.addBook(self,book_name,book_qty)

    def displayBook(self):
        count = len(self.__content)
        while count != 0 :
            if count >= 5:
                for i in range (5):
                    print('[{0}]'.format(len(self.__content)-count+1),self.__content[-count][0],end=' ')
                    count -=1
                print('')
            else :
                for i in range (count):
                    print('[{0}]'.format(len(self.__content)-count+1),self.__content[-count][0],end=' ')
                    count -= 1
        print('\n')

    def bookEdit(self):
        choose = input('Please choose between\n[1] Edit Title\n[2] Edit Content\n[3] Edit Quantity\n')
        if choose == '1':
            newTitle = input('Please input the Title Name! ')
            Edit.editTitle(self,newTitle)
        elif choose == '2':
            Edit.editContent(self)
        elif choose == '3':
            print('{0}\'s Quantity is {1}.'.format(self.__content[0],self.__content[-1]))
            while True:
                amt = input('Change the quantity to ')
                if amt.isdigit():
                    break
            Edit.editQty(self,amt)

    def borrowBook(self,account):
        book = input('Which book do you want to borrow?')
        for i in self.__content:
            if book.title() == i[0]:
                while True:
                    amt = int(input('How many book you want to borrow?'))
                    if amt <= int(i[-1]):
                        Edit(i).editQty(str(int(i[-1])-amt))
                        for a in range (amt):
                            account[-2].append(i[0])
                        break
                    else :
                        print('Sorry, We only got {0}.'.format(i[-1]))
        print('The book you have borrow is {0}.'.format(book.upper()))

    def displayBook_Acc(self,account):
        count = len(account[-2])
        while count != 0:
            if count >= 5:
                for i in range(5):
                    print('[{0}]'.format(len(account[-2]) - count + 1), account[-2][-count], end=' ')
                    count -= 1
                print('')
            else:
                for i in range(count):
                    print('[{0}]'.format(len(account[-2]) - count + 1), account[-2][-count], end=' ')
                    count -= 1
        print('\n')

    def returnBook(self,account):
        BookClass(self.__content).displayBook_Acc(account)
        book = int(input('\nWhich book do you want to return?'))
        account[-2].pop(book-1)
        for i in self.__content:
            if account[book-1] == i[0]:
                Edit(i).editQty(str(int(i[2])+1))

    def readOnspot(self):
        path = 'Book_List\\{0}'.format(self.__content[1])
        x = open(path, 'r')
        print(x.read())
        x.close()
