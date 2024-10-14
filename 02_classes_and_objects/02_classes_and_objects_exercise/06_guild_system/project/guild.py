from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for current_player in self.players:
            if current_player.name == player_name:
                current_player.guild = "Unaffiliated"
                self.players.remove(current_player)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        info = [f"Guild: {self.name}"]
        for player_ in self.players:
            info.append(player_.player_info())
        return '\n'.join(info)


# player = Player('Gosho', 100, 50)
# print(player.add_skill('Magic', 50))
# print(player.add_skill('Magic', 100))
# print(player.player_info())
# guild = Guild('Bloods')
# print(guild.assign_player(player))
# print(guild.assign_player(player))
# print(guild.kick_player('Gosho'))
# print(guild.kick_player('Gosho'))
# print(player.guild)
