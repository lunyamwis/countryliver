class Schedule:
    """
    a schedule is a very important record keeping
    tool that helps run operations within the firm
    and what we want to do is ensure that everything
    falls in place
    """
    def __init__(self,date_of_implementation,
                action,season,effect,skills,tools):
        self.date_of_implementation = date_of_implementation
        self.action = action
        self.season = season
        self.effect = effect
        self.skills = skills
        self.tools = tools


"""
below is the testing procedure of the above class
"""
if __name__ == '__main__':
    day_1 = Schedule('2020-10-26','clearing of the land',
                    'planting',0.75,['slashing','cutting trees'],
                    ['slasher','panga'])
    print(day_1.date_of_implementation)