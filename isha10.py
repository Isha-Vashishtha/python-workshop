#Global High Score Using Functions:
high_score=0
def update_high_score(score):
    global high_score
    if score>high_score:
        high_score=score
update_high_score(50)
print("High Score:",high_score)
#non_local variable in function:
def game_round():
    score=0
    def increase_score(points):
        nonlocal score
        score += points
    increase_score(10)
    return score
round_score=game_round()
print("Round Score:",round_score)

#Global player stats in
player_stats={
    "name":"Player 1",
    "score":100,
    "level":5
}
def display_player_info():
    print(f"Name:{player_stats['name']}")
    print(f"Score:{player_stats['score']}")
    print(f"Level:{player_stats['level']}")
display_player_info()
