'''
- query object has one attribute: list of query terms which are strings
- query object is created from single string or list of strings
'''

class Query:

    def __init__(self, query_term):
        self.list_of_query_terms = []
        assert type(query_term) is str or type(query_term) is list, 'require string or list as input'
        if type(query_term) is str:
            self.list_of_query_terms.append(query_term)
        else:
            for i in query_term:
                type_of_queryterm_in_list = type(i)
                assert type_of_queryterm_in_list is str, "if input is a list, every list element has to be string"
            self.list_of_query_terms += query_term # concatenating two lists

    def return_query(self):
        return self.list_of_query_terms
