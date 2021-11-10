#zachary blackwell 1941472

class Team:
    def init(self):
        self.teamname = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins/(self.team_wins+self.team_losses)

if __name__ == "__main__":
    student_team = Team()

    name = input()
    wins = int(input())
    losses = int(input())

    student_team.team_wins = wins
    student_team.team_losses = losses
    student_team.teamname = name


    win_percentage = student_team.get_win_percentage()

    avg = .5

    if win_percentage >= avg:
        print('Congratulations, Team', name, 'has a winning average!')
    else:
        print('Team', name, 'has a losing average.')