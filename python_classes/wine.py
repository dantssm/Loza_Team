# from user import User

class Wine:
    __rating = {}

    def __init__(self, name) -> None:
        self.name = name
        # self.region = data.Wine_data[name]['region']
        # self.country = data.Wine_data[name]['country']
        # self.taste = data.Wine_data[name]['taste']
        # self.color = data.Wine_data[name]['color']
        # self.attribute = data.Wine_data[name]['atribute']
        # self.recomendations:dict[User:str] = {}
        # self.reviews:dict[User:str] = {}
        # self.user_ratings:dict[User:float] = {}
        # Wine.__rating[self] = 0

    # def rated_by_user(self, user):
    #     return self.user_ratings[user]

    # def find_out_which_glass(self):
    #     for el, lst in data.Glass_data.items():
    #         if self.name in lst:
    #             return el

    # def find_out_which_snack(self):
    #     for wine, snacks in data.Snacks_data.items():
    #         if self.name == wine:
    #             return snacks

    # def is_highly_rated(self):
    #     return sum(self.user_ratings.values())/len(self.user_ratings.values()) >= 4.1
