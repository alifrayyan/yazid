#pyhton quiz game
print("QUIZ TEKA LAGU")

question=("siapakah pembuat lagu'adakah ini mimpi'?:",
          "group manakah yang membuat lagu'taman rashidah utama?:",
          "apakah lagu kebangsaan malaysia?:",)

options=(("A.reedzwan ","B.P.Ramlee ","C.Siti Nurhaliza ","D.Sudirman Arshad "),
         ("A.XPDC","B.black pink","C.wings","D.bts"),
         ("A.Keranamu Malaysia ","B.Tentang Bulan ","C.Jalur Gemilang ","D.Negaraku "))
         
answers =("A","C","D")
guesses=[]
score=0
question_num=0

for question in question:
        print("===================================")
        print(question)
        for option in options[question_num]:
            print(option)

        guess=input("Enter (A,B,C,D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score +=1
            print("niceeeee!!!")
        else:
            print("salah!!!!!!!!")
            print(f"jawapan yang betul adalah {answers[question_num]}")
        question_num +=1

print("===================================")
print("               RESULT              ")
print("===================================")

print("ANSWER: ", end="")

for answer in answers:
    print(answer, end="")
print()


print("guesses: ", end="")
for guess in guesses:
     print(guess, end="")
print()

markah = (score / question_num )* 100
print(f"YOUR SCORE IS: ", round (markah,2), "%")
