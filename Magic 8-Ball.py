# required info:
import random
Name = "Emre"
Q = "Evet mi Hayır mı"
answer = ""
random_number = random.randint(1, 9)
print (random_number, "\n")

# the core logic of the program
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now." 
elif random_number == 7:
  answer = "My sources say no." 
elif random_number == 8:
  answer = "Outlook not so good." 
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "dkslfjlkasjdfkls." 
elif random_number == 11:
  answer = "hahahahahaha"     
else:
  answer = "Error"  

# Name: N/A, Q: N/A
if Name == "" and Q == "":
  print("Lütfen bir soru sorun")
# Name: Yes, Q: N/A
elif Q == "":
  print("Lütfen bir soru sor", Name)
# Name: N/A, Q: Yes  
elif Name == "":
  print("Question:",Q,"\n")
  print("Magic 8-Ball answers:", answer)
else:
  print(Name, "asks:", Q)
  print("Magic 8-Ball answers:", answer)