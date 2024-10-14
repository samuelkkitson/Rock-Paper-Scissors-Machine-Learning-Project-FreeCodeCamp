import random
def player(prev_play, opponent_history=[], my_history=[], my_history_abbey=[], mrugesh_pattern=[], kris_pattern=[], abbey_pattern=[]):
    # Track both the opponent's and our own history
    
    if prev_play != "":
        opponent_history.append(prev_play)

    
    # print(opponent_history)
    # Define counter moves
    counter_moves = {"R": "P", "S": "R", "P": "S"}
    # Define Quincys Pattern
    quincy_pattern = ["R", "P", "P", "S", "R"]
    
    

    if len(opponent_history) % 999 == 0:
            my_history.clear()
            opponent_history.clear()
            quincy_pattern.clear()
            mrugesh_pattern.clear()
            kris_pattern.clear()
            abbey_pattern.clear()
            my_history_abbey.clear()
    
    
    mrugesh_next_move, mrugesh_counter = mrugesh(my_history, counter_moves)
    kris_next_move, kris_counter = kris(my_history, counter_moves)
    abbey_next_move, abbey_counter = abbey(my_history_abbey, counter_moves)
    # Handling the first five moves and recording potential patterns
    if len(opponent_history) < 5:
        moves = ["R", "P", "S"]
    
        move = moves[len(opponent_history) % 3]
        
        mrugesh_pattern.append(mrugesh_next_move)
        kris_pattern.append(kris_next_move)
        abbey_pattern.append(abbey_next_move)
        my_history.append(move)
        my_history_abbey.append(move)
        # print("pattern", abbey_pattern)
        return move
    
    

    
    
    # Check for Quincy's Pattern, if detected counter it
    if opponent_history[:5] == quincy_pattern:
        quincy_next_move = quincy_pattern[(len(opponent_history)) % len(quincy_pattern)]
        return counter_moves[quincy_next_move]
    
    elif opponent_history[:5] == mrugesh_pattern[:5]:
        my_history.append(mrugesh_counter)
        return mrugesh_counter
    
    elif opponent_history[:5] == kris_pattern[:5]:
        my_history.append(kris_counter)
        return kris_counter
            
    elif opponent_history[:4] == abbey_pattern[:4]:
        my_history_abbey.append(abbey_counter)
        return abbey_counter
    
    else:
        return random.choice(['R', 'P', 'S'])

def mrugesh(my_history, counter_moves, last_ten_lst=['']):
    # Define here instead of default argument
    last_ten = my_history[-10:]
    last_ten = last_ten_lst + last_ten
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "S"

    next_move = counter_moves[most_frequent]
    counter_mrugesh = counter_moves[next_move]
    
    return next_move, counter_mrugesh

def kris(my_history, counter_moves):
    
    if len(my_history) == 0:
        my_prev_play = "R"
    else: 
        my_prev_play = my_history[-1]
    next_move =  counter_moves[my_prev_play]
    counter_kris = counter_moves[next_move]

    return next_move, counter_kris

def abbey(my_history_abbey, 
          counter_moves,
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    # Creating an own history list, so that it doesnt interfere with other patterns

    
    if len(my_history_abbey) == 0:
        my_prev_play = "R"
        my_history_abbey.append(my_prev_play)
        play_order[0] = {  # Resetting play order
            "RR": 0,
            "RP": 0,
            "RS": 0,
            "PR": 0,
            "PP": 0,
            "PS": 0,
            "SR": 0,
            "SP": 0,
            "SS": 0,
        }
    else: 
        my_prev_play = my_history_abbey[-1]
    # print("Play order", play_order)
    # print("My history", my_history_abbey)
    last_two = "".join(my_history_abbey[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1
    
    potential_plays = [
        my_prev_play + "R",
        my_prev_play + "P",
        my_prev_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }
    # print("Sub order", sub_order)

    prediction = max(sub_order, key=sub_order.get)[-1:]
    next_move = counter_moves[prediction]
    counter_abbey = counter_moves[next_move]

    return next_move, counter_abbey