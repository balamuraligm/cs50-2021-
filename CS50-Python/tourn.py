# Simulate a sports tournament

import csv
import sys
import random
import math

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    counts = {}
    # TODO: Read teams into memory from file

    with open (sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for team in reader:
            teams.append(team)
            counts[team['team']] = 0

    # initilization of count to Zero

    for team in teams:
        team['rating'] = int(team['rating'])
    print (teams)
    print (counts)

    # TODO: Simulate N tournaments and keep track of win counts
    for tournament in range(N):
        winner = simulate_tournament(teams)

        final_winner = winner[0]['team']
        print ("final winner is ", final_winner)
       
        counts[final_winner] = counts [final_winner] +1


    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    rounds = int(math.sqrt(len(teams)))
    for round in range(rounds):
        winners = simulate_round(teams)
        teams = winners

    print("inside tourna     ", winners)
    

    return winners


if __name__ == "__main__":
    main()
