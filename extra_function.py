class extra_function:

    def __init__(self):

        self.values : list = []
    
    def hold_values(self, values: list):

        self.values = values
    
    def literal_type(self, val):

        if val in self.values:
            return val
        
        else:
            return None
        
    def element_itself(self, element : any, list : list):

        if element in list:
            return element
        
        else:
            return None
        
    def ternary_operator(self, condition : any, value1 : any, value2 : any):

        return value1 if condition else value2



extra_function = extra_function()