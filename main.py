import random

def cl():
  teams = ["PSG", "Real Madrid", "Club Brugge", "Galatasaray", "Bayern Munich", "Tottenham", "Olympiacos", "Crvena zvezda", "Manchester City", "Atalanta", "Shakhtar Donetsk", "Dinamo Zagreb", "Juventus", "Atletico Madrid", "Bayer", "Lokomotiv Moscow", "Liverpool", "Napoli", "Red Bull", "Genk", "Barcelona", "Dortmund", "Inter", "Slavia Praha", "RB Leipzig", "Lyon", "Benfica", "Zenit", "Valencia", "Chelsea", "Ajax", "Lille"]
  #List of all current teams in the Champions League
  
  print ("welcome to the Champions league simulator.\n")#introduce what the program is about
  print teams # allow the user to see their options of the soccer teams
  
  a = raw_input("\nChoose which team you would like to choose to reign victory? ") #ask the user for his team
 
  teams.remove(a) #take out chosen team so you won't face yourself

  wins = [] #keeps score of wins

  group = [] #the group stage
  s = random.choice(teams) #chooses 1 team to later face in the group
  d = random.choice(teams) #chooses 1 team to later face in the group
  w = random.choice(teams) #chooses 1 team to later face in the group
  group += [s,d,w]

  teams.remove(s)
  teams.remove(d)
  teams.remove(w) #20-22 takes the teams out of list for next stage if the user advances

  print ("You will be facing " + s,d,w)

  for x in group:
    q = random.randint(1,100) #runs on probability
    aa = ["Home game", "Away game"]
    ab = random.choice(aa) #chooses home or away game
    #Great idea on the probability factor - Mason Moreno
    if (q > 50):  
      print("You won your first " + ab + " against " + x)
      wins += [1] #add one win to the list
      if ab == "Home game": 
        aa.remove("Home game")  #Pretty smart idea, so the teams are out of the list. This helps so that one team doesn't play itself, which is impossible. - Aiden Pasillas
      else: 
        aa.remove("Away game") # eliminates first game to let the second game happen
    elif q < 50:
      print("You lost your first " + ab + " against " + x) #first option of first game of group stage
      if ab == "Home game":
        aa.remove("Home game")
      else:
        aa.remove("Away game")
  
    q = random.randint(1,100) #probability factor again
    ab = random.choice(aa) # the only option left of location for the match
  
    if q > 50:
      print("You won your first " + ab + " against " + x)
      wins += [1]
    elif q < 50:
      print("You lost your first " + ab + " against " + x)

  '''continues to advance in games closer to the final. for ex. quarter final, semi-final, final'''

  if wins > 3:
    print("Congratulations you advance to the round of 16") #round of 16 game
    g = random.choice(teams)
    teams.remove(g)
    q = random.randint(1,100)
    if q > 50: #quarter finals game if advances
      print("You won against "+ g + " in your first round of 16 game")
      print("Now you move on to quarter finals.")
      g = random.choice(teams)
      teams.remove(g)
      q = random.randint(1,100)
      if q > 50:#win in the 1/4 final moving on to semi-final probability
        print("You won against "+ g + ". Now you will play the semifinal, good luck.")#advances to next level
        g = random.choice(teams)
        teams.remove(g)
        q = random.randint(1,100)
        if q > 50:#win from semifinal going to final probability
          print("Wow. you made it this far! You won against " + g + " in the semi final. Now you will play the one that really counts. The final.")
          g = random.choice(teams)
          teams.remove(g)
          q = random.randint(1,100)
          if q > 50:#final win if advances from semifinal
            print("YESS!!! You won the final against " + g + ". It was a tough and good game but you made it through.")
          else:#ending if lost the final
            print("NOOOO!! You lost. This is terrible, but if you made it this far, that means next year you will win it.")
        else:#ending if lost the semifinal
          print("sorry you lost the semi final, you can make it next year.")  
    else:#ending if lost the quarter final
      print("You lost the quarter final. I'm sorry. Better train for next year")
  else:#ending if didn't advance to the round of 16
    print("I'm sorry. You can't play any further. You will be placed in the Europa League group stage.")
    print("Good Luck.")

cl() # automatically goes to function cl()