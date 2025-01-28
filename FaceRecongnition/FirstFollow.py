class Grammar:
    def __init__(self):
        self.productions = {
            # 'S': [['A', 'B', 'c'], ['B', 'C', 'D'] , ['X' , 'D']],
            # 'A': [['A', 'd'],['A', 'C'] , ['A', 'r'] ,  ['d']],
            # 'B': [['C', 'A', 'X'], ['ε']],
            # 'C': [['id']],
            # 'D': [['B', 'c'], ['ε']],
            # 'X': [['e']]
            
            S' -> S
S -> A 1
A -> a B
A -> b C
A -> B d
B -> c B C
B -> r
C -> c
            
        }
        self.first_sets = {}
        self.follow_sets = {}
        self.start_symbol = 'S'
   
    def compute_first(self):
        for key in self.productions:
            self.first_sets[key] = set()
        changed = True
       
        while changed:
            changed = False
            for key, rules in self.productions.items():
                for rule in rules:
                    for symbol in rule:
                        if symbol not in self.productions:  
                            if symbol not in self.first_sets[key]:
                                self.first_sets[key].add(symbol)
                                changed = True
                            break
                        else:
                            before_size = len(self.first_sets[key])
                            self.first_sets[key].update(self.first_sets[symbol])
                            if len(self.first_sets[key]) > before_size:
                                changed = True
                        if 'ε' not in self.first_sets[symbol]:
                            break
 
    def compute_follow(self):
        for key in self.productions:
            self.follow_sets[key] = set()
        self.follow_sets[self.start_symbol].add('$')  
        changed = True
       
        while changed:
            changed = False
            for key, rules in self.productions.items():
                for rule in rules:
                    for i, symbol in enumerate(rule):
                        if symbol in self.productions:  
                           
                            following_symbols = rule[i + 1:] if i + 1 < len(rule) else []
                            if following_symbols:
                                first_of_following = self.first_of_sequence(following_symbols)
                                before_size = len(self.follow_sets[symbol])
                                self.follow_sets[symbol].update(first_of_following - {'ε'})
                                if 'ε' in first_of_following:
                                    self.follow_sets[symbol].update(self.follow_sets[key])
                                if len(self.follow_sets[symbol]) > before_size:
                                    changed = True
                            else:  
                                before_size = len(self.follow_sets[symbol])
                                self.follow_sets[symbol].update(self.follow_sets[key])
                                if len(self.follow_sets[symbol]) > before_size:
                                    changed = True
 
    def first_of_sequence(self, symbols):
        first = set()
        for symbol in symbols:
            if symbol in self.productions:
                first.update(self.first_sets[symbol])
                if 'ε' not in self.first_sets[symbol]:
                    break
            else:
                first.add(symbol)
                break
        return first
 
    def print_sets(self):
        print("FIRST sets:")
        for key, value in self.first_sets.items():
            print(f"FIRST({key}) = {value}")
       
        print("\nFOLLOW sets:")
        for key, value in self.follow_sets.items():
            print(f"FOLLOW({key}) = {value}")
 
grammar = Grammar()
grammar.compute_first()
grammar.compute_follow()
grammar.print_sets()
