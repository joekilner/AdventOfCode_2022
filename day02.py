data = open("day02.txt").readlines()

#look-ups
fomatter= ["Rock", "Paper", "Scissors"]
outcome_formatter = ["Draw","They Win", "I win"]
their_decoder = {"A":0, "B":1, "C":2}
outcome_score = [3, 0, 6]
choice_score = [1, 2, 3]

# Part 1
my_decoder = {"X":0, "Y":1, "Z":2}
scores = []
for (theirs, space, mine, newline) in data:
    their_move = their_decoder[theirs]
    my_move = my_decoder[mine]
    scores.append(outcome_score[(their_decoder[theirs] - my_decoder[mine]) % 3] + choice_score[my_move])

print(sum(scores))
    
# Part 2
outcome_decoder = {"X":1, "Y":0, "Z":2}
scores = []
for (theirs, space, outcome, newline) in data:
    their_move = their_decoder[theirs]
    desired_outcome = outcome_decoder[outcome]
    scores.append(outcome_score[desired_outcome] + choice_score[(their_move - desired_outcome) % 3])

print(sum(scores))
