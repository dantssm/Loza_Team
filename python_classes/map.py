from python_classes.wine import Wine

class Map:
    all_regions:dict[str:dict[str:Wine]] = {} #{country:{region_1:[wine_1_1, wine_1_2]...}}

    def __init__(self, user, img='', color = 'white') -> None:
        self.user = user
        self.unlocked_regions:dict[str:dict[str:Wine]] = {} #{country:{region_1:[wine_1_1, wine_1_2]...}}
        self.background = color
        self.image = img


    def add_wine_to_the_map(self, wine:'Wine'):
        if self.all_regions[wine.region]:
            self.all_regions[wine.region][wine.country] = wine
            # регіон вже підсвічений
        else: #перше вино з цього регіону
            self.highlight_the_region(wine.region)
            self.all_regions[wine.region][wine.country] = wine

    def highlight_the_region(self, new_region):
        """У якийсь спосіб візуально підсвічуємо регіон"""
        pass
            
