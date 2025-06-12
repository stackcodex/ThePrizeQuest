#DAY6
#Creating who wants to be a milionaire
# creating a list of questions 
# a list of options
# use conditional statements
name = (input("Enter you name:"))
prize = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]
questions = ["1. Who wrote the Mahabharata?", "2. Who is the central character who gives the Bhagavad Gita discourse?", "3. How many Pandava brothers were there?",
                  " 4. Who was the wife of all five Pandavas?", "5. Which battle is the central event of the Mahabharata?", "6. Who was the biological father of Karna?",
                  "7. Which weapon did Arjuna receive from Lord Shiva?", "8. Who killed Dronacharya in the war?",
                    "9. What was the name of the game that led to the Pandavas’ exile?", "10. Who was the charioteer(sarthi) of Arjuna in the Kurukshetra war?",
                    "11. Which Pandava was known for his immense strength?", "12. Who was the only Kaurava to survive the Kurukshetra war?", 
                    "13. Who cursed Karna that his knowledge of Brahmastra would fail when he needed it most?", 
                    "14. What was name of Arjuna’s son who was killed by Ashwatthama?", "15. Who disguised themselves as dance teacher (brihanlalla) during the agyadvas?", 
                    "16. Who gave the Akshaya Patra to the Pandavas during their agyadvas?"]
options = ["A) Valmiki\nB) Vyasa\nC) Kalidasa\nD) Tulsidas", "A) Arjuna\nB) Bhishma\nC) Krishn\nD) Yudhishthira", "A) 3\nB) 4\nC) 5\nD) 6", 
           "A) Kunti\nB) Satyavati\nC) Draupadi\nD) Gandhari", "A) Lanka War\nB) Kurukshetra War\nC) Ramayana War\nD) Panchala War", "A) Drona\nB) Pandu\nC) Surya\nD) Vyasa",
           "A) Sudarshana Chakra\nB) Brahmastra\nC) Pashupatastra\nD) Trishula", "A) Arjuna\nB) Bhima\nC) Yudhishthira\nD) Dhrishtadyumna", 
           "A) Snakes and Ladders\nB) Ludo\nC) Chess\nD) Dice (Dyutakrida)", "A) Krishna\nB) Bhishma\nC) Karna\nD) Shalya","A) Arjuna\nB) Yudhishthira\nC) Sahadeva\nD) Bhima",
           "A) Duryodhana\nB) Dushasana\nC) Yuyutsu\nD) Shakuni","A) Parashurama\nB) Krishna\nC) Bhishma\nD) Indra","A) Abhimanyu\nB) Ghatotkacha\nC) Prativindhya\nD) Uttara",
           "A) Bhima\nB) Arjuna\nC) Sahadeva\nD) Nakula", "A) Indra\nB) Surya\nC) Krishna\nD) Yudhishthira"]
print("Welcome,", name, "to who wants to be a millionaire!!")
print("Are you ready to play and win?")
agreement = (input("Yes/No: "))
if agreement == "Yes" or agreement == "yes" or agreement == "YES":
    print("Here, is your first question on your screen for", prize[0], "rupees")
    print(questions[0])
    print(options[0])
    answer = (input("Enter your answer:"))
    if answer == "B) Vyasa" or answer == "B" or answer == "vyasa" or answer == "Vyasa":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[0], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was B) Vyasa\nYou won 0 rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your second question on your screen for", prize[1], "rupees")
    print(questions[1])
    print(options[1])
    answer = (input("Enter your answer:"))
    if answer == "C) Krishn" or answer == "C" or answer == "krishn":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[1], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was C) Krishn\nYou won",prize[0], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your third question on your screen for", prize[2], "rupees")
    print(questions[2])
    print(options[2])
    answer = (input("Enter your answer:"))
    if answer == "C) 5" or answer == "C" or answer == "5":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[2], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was C) 5\nYou won",prize[1], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your fourth question on your screen for", prize[3], "rupees")
    print(questions[3])
    print(options[3])
    answer = (input("Enter your answer:"))
    if answer == "C) Draupadi" or answer == "C" or answer == "draupadi":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[3], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was C) Draupadi\nYou won",prize[2], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your fifth question on your screen for", prize[4], "rupees")
    print(questions[4])
    print(options[4])
    answer = (input("Enter your answer:"))
    if answer == "B) Kurukshetra War" or answer == "B" or answer == "Kurukshetra War":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[4], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was B) Kurukshetra War\nYou won",prize[3], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your sixth question on your screen for", prize[5], "rupees")
    print(questions[5])
    print(options[5])
    answer = (input("Enter your answer:"))
    if answer == "C) Surya" or answer == "C" or answer == "Surya":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[5], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was C) Surya\nYou won",prize[4], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your seventh question on your screen for", prize[6], "rupees")
    print(questions[6])
    print(options[6])
    answer = (input("Enter your answer:"))
    if answer == "C) Pashupatastra" or answer == "C" or answer == "Pashupatastra":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[6], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was C) Pashupatastra\nYou won",prize[5], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your eighth question on your screen for", prize[7], "rupees")
    print(questions[7])
    print(options[7])
    answer = (input("Enter your answer:"))
    if answer == "D) Dhrishtadyumna" or answer == "D" or answer == "Dhrishtadyumna":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[7], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was D) Dhrishtadyumna\nYou won",prize[6], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your ninth question on your screen for", prize[8], "rupees")
    print(questions[8])
    print(options[8])
    answer = (input("Enter your answer:"))
    if answer == "D) Dice (Dyutakrida)" or answer == "D" or answer == "Dice":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[8], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was D) Dice (Dyutakrida)\nYou won",prize[7], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your tenth question on your screen for", prize[9], "rupees")
    print(questions[9])
    print(options[9])
    answer = (input("Enter your answer:"))
    if answer == "A) Krishna" or answer == "A" or answer == "Krishna":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[9], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was A) Krishna\nYou won",prize[8], "rupees.\nThank you for playing with us!!")
        quit()   
    print("Here, is your eleventh question on your screen for", prize[10], "rupees")
    print(questions[10])
    print(options[10])
    answer = (input("Enter your answer:"))
    if answer == "D) Bhima" or answer == "D" or answer == "Bhima":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[10], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was D) Bhima\nYou won",prize[9], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your twelfth question on your screen for", prize[11], "rupees")
    print(questions[11])
    print(options[11])
    answer = (input("Enter your answer:"))
    if answer == "C) Yuyutsu" or answer == "C" or answer == "Yuyutsu":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[11], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was C) Yuyutsu\nYou won",prize[10], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your thirteenth question on your screen for", prize[12], "rupees")
    print(questions[12])
    print(options[12])
    answer = (input("Enter your answer:"))
    if answer == "A) Parashurama" or answer == "A" or answer == "Parashurama":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[12], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was A) Parashurama\nYou won",prize[11], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your fourteenth question on your screen for", prize[13], "rupees")
    print(questions[13])
    print(options[13])
    answer = (input("Enter your answer:"))
    if answer == "C) Prativindhya" or answer == "C" or answer == "Prativindhya":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[13], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was C) Prativindhya\nYou won",prize[12], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your fifteenth question on your screen for", prize[14], "rupees")
    print(questions[14])
    print(options[14])
    answer = (input("Enter your answer:"))
    if answer == "B) Arjuna" or answer == "B" or answer == "Arjuna":
        print("That was a correct answer!!")
        print("Congratulation,", name, "you won", prize[14], "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was B) Arjuna\nYou won",prize[13], "rupees.\nThank you for playing with us!!")
        quit()
    print("Here, is your sixteenth question on your screen for", prize[15], "rupees")
    print(questions[15])
    print(options[15])
    answer = (input("Enter your answer:"))
    if answer == "B) Surya" or answer == "B" or answer == "Surya":
        print("That was a correct answer!!")
        amount = 1000 + 2000 + 3000 + 5000 + 10000 + 20000 + 40000 + 80000 + 160000 + 320000 + 640000 + 1250000 + 2500000 + 5000000 + 10000000 + 70000000
        print("Congratulation,", name, "you won", amount, "rupees")
    else:
        print("Oops! Unfortunatly that was the wrong answer.\nThe correct answer was B) Surya\nYou won",prize[14], "rupees.\nThank you for playing with us!!")
        quit()    
      
elif agreement == "No" or agreement == "no" or agreement == "NO":
    print("Oops! You unfortunatly lost a chance to be a millionaire.")
else:
    print("There is a Typo/Typing misktake on you agreement")