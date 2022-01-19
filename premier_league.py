# This program will simulate a Fifa manager career
import random


class Team:
    """Class used to create a team."""

    def __init__(self):
        """Initialize attributes of Team"""
        # Create a variable that holds player's points
        self.points = 0
        self.is_winner: False
        self.is_loser: False

    def update(self, team):
        """Update points in tournament"""
        if team.is_winner:
            self.points += 3
        elif team.is_loser:
            self.points += 0
        else:
            self.points += 1


class League:
    """Class that simulates the Barclays premier league"""

    def __init__(self):
        """Initialize attributes of league"""
        # Create list of teams that will be used in the tournament, declare their overall (skills)
        self.teams = {"Arsenal": 79, "Chelsea": 83, "Manchester United": 84, "Manchester City": 85, "Liverpool": 84,
                      "West Ham": 79, "Tottenham": 82, "Wolves": 78, "Brighton": 76, "Leicester City": 80,
                      "Crystal Palace": 76, "Southampton": 76, "Aston Villa": 78, "Brentford": 73, "Leeds": 77,
                      "Everton": 79, "Watford": 75, "Norwich City": 74, "Newcastle": 76, "Burnley": 76}
        self.rounds = 1
        self.matches = []
        self.matched = True

    def overall(self):
        """Randomize Overall of Teams"""
        # Update values of self.teams dic by a random value up to 10 points more than its initial value
        for squad, overall in self.teams.items():
            # If team's overall is better than 80, team can grow by 10 overall points
            if overall >= 80:
                self.teams.update({squad: random.randint(overall, overall + 10)})
            # If team's overall is less than 80, team can grow by 5 overall points, this way segregating it.
            elif overall <= 80:
                self.teams.update({squad: random.randint(overall, overall + 5)})

    def create_round(self):
        """Method that makes the rounds of a league"""
        self.matched = False
        # Create list of teams gotten from dictionary self.teams
        team_list = list(self.teams.keys())

        # Shuffle the list, so it's always gonna give random rounds
        random.shuffle(team_list)

        # Use first 10 teams in team_list for home teams, and last 10 for visitor teams
        home = team_list[:10]
        visitor = team_list[10:]

        # Create list to append matches
        lst = []
        for i in range(len(home)):
            lst.append([home[i], visitor[i]])

        # Append list of one round matches to list that holds all matches of the tournament
        for i in lst:
            if i in self.matches:
                self.matched = True

        if not self.matched:
            for i in lst:
                self.matches.append(i)

        # Display round
        if not self.matched:
            print(f"\nPremier League Round {self.rounds}")
            print("--------------------------------")
            for i in range(10):
                print(home[i] + " X " + visitor[i])

            self.rounds += 1

    def odds_of_winning(self):
        """"""

    def competition_stats(self):
        """"""


class Game:
    """"""


league = League()
while True:
    league.create_round()