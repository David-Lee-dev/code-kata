# 달리기 경주
# https://school.programmers.co.kr/learn/courses/30/lessons/178871?language=python3

from collections import deque

def solution(players, callings):
    player_rank_table = {player : idx for idx, player in enumerate(players)}
    
    for call in callings:
        called_player_rank = player_rank_table[call]
        called_player = call
        
        overtaken_player_rank = player_rank_table[call] - 1
        overtaken_player = players[overtaken_player_rank]
        
        players[overtaken_player_rank] = call
        players[called_player_rank] = overtaken_player
        
        player_rank_table[called_player] = overtaken_player_rank
        player_rank_table[overtaken_player] = called_player_rank
    
    return players