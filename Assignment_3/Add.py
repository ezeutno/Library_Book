import random
class Add:
    def __init__(self,content):
        self.__content = content

    def addAccount(self,fname,lname,gender,email,birthday,p):
        while True:
            username = fname.upper()[0]+lname.upper()[0]+birthday.split('/')[0]+str(random.randint(0,999))
            count = 0
            for i in self.__content:
                if username == i[0]:
                    continue
                else:
                    count += 1
            if count == len(self.__content):
                break
        while True:
            password = input('Please input password ')
            ver_password = input('Please input password verification ')
            if password == ver_password and len(password)>= 8:
                break
            else:
                print('Error, Either your password less than 8 or Couldn\'t verified password!')
        self.__content.append([username,password,[fname,lname,gender,email],birthday,[],p])
        print('Your username is {0}\nYour password is {1}'.format(username,'*'*(len(password)-2)+password[-2:]))

    def addBook(self,book_name,qty):
        path_book = 'Book_List\\{0}'.format(book_name+'.txt')
        print('Please input the content of {0}'.format(book_name))
        print('When your done, Please write ENDLINE!')
        while True:
            book_write = open(path_book, 'a')
            book_checker = open(path_book, 'r').read().split()
            input_word = input()
            if input_word.upper() == 'ENDLINE':
                break
            elif book_checker == []:
                book_write.write(input_word)
            else:
                book_write.write('\n' + input_word)
            book_write.close()
        self.__content.append([book_name,book_name+'.txt',str(qty)])
        print(book_name + ' has been submitted')

#Testing Bases
#print(Add([]).addAccount('Name','Last','Male','name.last@gmail.com','24/09/99'))
#print(Add([]).addBook('Lazada',2))

