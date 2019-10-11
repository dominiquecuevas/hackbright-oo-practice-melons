############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

    # def __repr__(self):
    #     return f'<MelonType code={self.code}>'

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')  # output = instance
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren',1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # loop through list of melon_type objects
    # for each melon, save object.pairings in a variable --> list
        # for each pairing in the pairings list, print the item

    for melon_object in melon_types:
        print(f"{melon_object.name} pairs with")
        melon_pairings = melon_object.pairings
        for food in melon_pairings:
            print(f"- {food}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # initialize empty dict
    # loop through list of melon_type objects
    # for each melon
        # save object.code in a variable (key) --> string
        # add key + value (object) to dict
    # return dict

    melons_by_code = {}

    for melon_object in melon_types:
        code_key = melon_object.code
        melons_by_code[code_key] = melon_object

    return melons_by_code

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Needs __init__ and is_sellable methods

    def __init__(self, code, shape_rating, color_rating, field, harvested_by):
        """Initialize a melon."""
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by

    # define method is_sellable
        # if statements for shape & color rating > 5 to be sellable
        # and if statment for not in field 3
        # return Boolean
    def is_sellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 and self.field != 3

def make_melons(melon_types=make_melon_types()):
    """Returns a list of Melon objects."""

    # use make_melon_type_lookup to look through it's dictionary based on .code attr as key
    # instantiate the melons
    melon_1 = Melon(make_melon_type_lookup(melon_types)['yw'], 8, 7, 'Harvested from Field 2', 'Harvested by Sheila')
    melon_2 = Melon(make_melon_type_lookup(melon_types)['yw'], 3, 4, 'Harvested from Field 2', 'Harvested by Sheila')
    melon_3 = Melon(make_melon_type_lookup(melon_types)['yw'], 9, 8, 'Harvested from Field 3', 'Harvested by Sheila')
    melon_4 = Melon(make_melon_type_lookup(melon_types)['cas'], 10, 6, 'Harvested from Field 35', 'Harvested by Sheila')
    melon_5 = Melon(make_melon_type_lookup(melon_types)['cren'], 8, 9, 'Harvested from Field 35', 'Harvested by Michael')
    melon_6 = Melon(make_melon_type_lookup(melon_types)['cren'], 8, 2, 'Harvested from Field 35', 'Harvested by Michael')
    melon_7 = Melon(make_melon_type_lookup(melon_types)['cren'], 2, 3, 'Harvested from Field 4', 'Harvested by Michael')
    melon_8 = Melon(make_melon_type_lookup(melon_types)['musk'], 6, 7, 'Harvested from Field 4', 'Harvested by Michael')
    melon_9 = Melon(make_melon_type_lookup(melon_types)['yw'], 7, 10, 'Harvested from Field 3', 'Harvested by Sheila')
    
    melons = []
    melons.extend([melon_1,melon_2,melon_3,melon_4,melon_5,melon_6,melon_7,melon_8,melon_9])
    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    
    for melon in melons:
        sellable = "(CAN BE SOLD)" if melon.is_sellable() else "(NOT SELLABLE)"
        print(f"{melon.harvested_by} from {melon.field} {sellable}")
    # Fill in the rest 
    # function takes in melons list 




all_melon_types = make_melon_types()

melons_by_code_dictionary = make_melon_type_lookup(all_melon_types)

melons_list = make_melons(all_melon_types)

get_sellability_report(melons_list)