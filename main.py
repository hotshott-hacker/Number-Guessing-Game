import random

greeting_msg = "HEY PLAYER... WELCOME TO NUMBER GUESSING GAME"
player_online = True

def choose_difficulty():
      difficulty = int(input('''Choose the difficulty : \n1) easy, 2) medium, 3) hard  : '''))
      if difficulty == 1:
            main_game_easy()
      elif difficulty == 2:
            main_game_medium()
      else:
            main_game_hard()

def main_game_easy():
      i = 0
      print('\n', greeting_msg, '\n')
      while player_online:
            rand_num = random.randint(1, 4)
            user_input = int(input("Guess a number from 1 to 3 : "))
            i += 1

            if user_input == rand_num:
                  print(f"You got it correct in {i} tries!!! Congratulations!!!!!!")
                  break
            else:
                  pass


def main_game_medium():
      i = 0
      print(greeting_msg)
      while player_online:
            rand_num = random.randint(1, 7)
            user_input = int(input("Guess a number from 1 to 6 : "))
            i += 1

            if user_input == rand_num:
                  print(f"You got it correct in {i} tries!!! Congratulations!!!!!!")
                  break
            else:
                  pass

def main_game_hard():
      i = 0
      print(greeting_msg)
      while player_online:
            rand_num = random.randint(1, 11)
            user_input = int(input("Guess a number from 1 to 10 : "))
            i += 1

            if user_input == rand_num:
                  print(f"You got it correct in {i} tries!!! Congratulations!!!!!!")
                  break
            else:
                  pass

choose_difficulty()


while True:
      retry_test = int(input("Do you wanna retry ? (1) Yes  (2) no)"))
      if retry_test == 1:
            choose_difficulty()
      else:
            break

#Source --> DK
