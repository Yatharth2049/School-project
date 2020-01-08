def hangman():
      print('''INSTRUCTIONS: (READ BEFORE STARTING)
               1.please enter right no. of vovels i.e. a,e,i,o,u
               2.please type in only lowercase format
               3.user1 should enter movie name without noticied by user2
               4.user2 is not allowed to scroll up
                 YOU HAVE 10 Guesses ENJOY  ^^     ''')
      j=1
      guess_no=0
      wins=0
      dict_name=dict()
      name=list(input('USER_1 ENTER THE NAME OF THE MOVIE: '))
      vovels=int(input('ENTER THE NO OF VOVELS: '))
      for i in range(0,len(name)):
           dict_name[j]=(name[i])
           j=j+1
      for i in range(0,60):#this only done so that user2 cannot look at the name entered by user1
             print('\n')
      for i in range(0,len(name)):
         if ord(name[i])== 97:
            print('a',end=' ')
         elif ord(name[i])== 101:
            print('e',end=' ')
         elif ord(name[i])== 105:
            print('i',end=' ')
         elif ord(name[i])== 111:
            print('o',end=' ')
         elif ord(name[i])== 117:
            print('u',end=' ')
         else:
            print('_',end=' ')
      while guess_no<10:
         no_guess=int(input('ENTER THE LETTER NO YOU WANT TO GUESS: '))
         guess=input('USER_2 TAKE YOUR GUESS: ')
         a=dict_name[no_guess]
         b=str(a)
         if b == guess:
            print('YOU GOT THAT ONE RIGHT')
            wins=wins+1
            guess_no=guess_no-1
         else:
            print('WRONNGGGG -_-')
         guess_no=guess_no+1
         if wins==(len(name)-vovels):
            print('YOU WON ^^')
            break
         if guess_no==10:
            print('YOU LOST :|')
hangman()
