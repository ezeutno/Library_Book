class Edit:
    def __init__(self, content):
        self.__content = content

    def editTitle(self, newTitle):
        self.__content[0] = newTitle
        self.__content[1] = newTitle + '.txt'
        return 'The book name has changed to {0}'.format(self.__content[0])

    def editContent(self):
        openBook = open('Book_List\\{0}'.format(self.__content[1]), 'r')
        list_ob = openBook.read().split('\n')
        for i in range(len(list_ob)):
            print('[{0}] {1}'.format(i + 1, list_ob[i]))
        lineInput = int(input('Which line you want to change?')) - 1
        print(list_ob[lineInput])
        list_ob[lineInput] = input('Write down the changes!\n')
        open('Book_List\\{0}'.format(self.__content[1]), 'w')
        openBook_A = open('Book_List\\{0}'.format(self.__content[1]), 'a')
        for i in range(len(list_ob)):
            if i == 0:
                openBook_A.write('{0}'.format(list_ob[i]))
            else:
                openBook_A.write('\n{0}'.format(list_ob[i]))

    def editQty(self, amt):
        self.__content[2] = amt

    def editPassword(self,newPassword):
        self.__content[1] = newPassword

    def editName(self,fname,lname):
        self.__content[2][0] = fname
        self.__content[2][1] = lname

    def editEmail(self,email):
        self.__content[2][3] = email

#Testing Bases
#Edit(['Peresmian 2 Ruas Tol', 'Peresmian 2 Ruas Tol.txt', '1000']).editContent()
