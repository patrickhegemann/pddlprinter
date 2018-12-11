from pddlprinter.model import Domain, TypeHierarchy, ObjectType, Predicate, PDDLObject


class PDDLParser:
    @staticmethod
    def parse_direct(string):
        t = PDDLParser.tokenize(string)
        lists = PDDLParser.read_from_tokens(t)

        # print(lists)
        d = Domain()
        for l in lists:
            if l[0] == "domain":
                # Read domain name
                d.name = l[1]
            elif l[0] == ":types":
                # Extract type hierarchy
                d.type_hierarchy = PDDLParser.parse_types(l[1:])
            elif l[0] == ":predicates":
                # Extract predicates
                d.predicates = PDDLParser.parse_predicates(l[1:], d.type_hierarchy)
            elif l[0] == ":constants":
                # Get constants
                d.constants = PDDLParser.parse_constants(l[1:], d.type_hierarchy)

        # Return nested lists representing the PDDL domain
        return d

    @staticmethod
    def parse(filename):
        # Read and tokenize file contents
        f = open(filename, 'r')
        content = f.read()
        f.close()
        return PDDLParser.parse_direct(content)

    @staticmethod
    def tokenize(string):
        lines = []
        for line in string.split("\n"):
            # Filter out comments
            a, _, _ = line.partition(";")
            # Remove whitespace
            effective_line = a.strip()
            if effective_line is not "":
                lines.append(effective_line)
        chars = " ".join(lines)
        return chars.replace('(', ' ( ').replace(')', ' ) ').split()

    @staticmethod
    def read_from_tokens(tokens):
        if len(tokens) == 0:
            raise SyntaxError('unexpected EOF')
        token = tokens.pop(0)
        if token == '(':
            inner_list = []
            while tokens[0] != ')':
                inner_list.append(PDDLParser.read_from_tokens(tokens))
            # Remove closing bracket
            tokens.pop(0)
            return inner_list
        elif token == ')':
            raise SyntaxError('unexpected )')
        else:
            return token

    @staticmethod
    def parse_types(type_list):
        h = TypeHierarchy()
        cur_types = []
        next_is_parent = False
        for t in type_list:
            if next_is_parent:
                # Found parent type
                h.update_type(t, children=cur_types)
                next_is_parent = False
                cur_types.clear()
            elif t is '-':
                # Dash marks separation between children and parent types
                next_is_parent = True
            else:
                # Add/Update the type
                cur_types.append(h.update_type(t, []))
        return h

    @staticmethod
    def parse_predicates(predicate_list, types):
        predicates = []
        for p_tokens in predicate_list:
            name = p_tokens[0]
            p_tokens = p_tokens[1:]
            counter = 0
            predicate_types = []
            for t in p_tokens:
                if t.startswith("?"):
                    # One more parameter
                    counter += 1
                elif t == "-":
                    pass
                else:
                    # Type of the previous parameters
                    predicate_types = predicate_types + [types.get_type_from_name(t)] * counter
                    counter = 0
            predicates.append(Predicate(name, predicate_types))
        return predicates

    @staticmethod
    def parse_constants(constants_list, types):
        constants = []
        cur_constants = []
        next_is_type = False
        for t in constants_list:
            if next_is_type:
                # Found type of the previous names -> Create all of them and add them
                for constant_name in cur_constants:
                    c = PDDLObject(constant_name, types.get_type_from_name(t), type_flexible=False)
                    constants.append(c)
                next_is_type = False
                cur_constants.clear()
            elif t is '-':
                # Dash marks separation between children and parent types
                next_is_type = True
            else:
                # Add this constant to the list of names
                cur_constants.append(t)
        return constants
