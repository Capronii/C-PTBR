import sys
import re

reserved_words = ["imprime", "se", "senao", "e", "ou", "entrada"]

class PrePro:
    @staticmethod
    def filter(code):
        res = code
        for i in range(len(code)):
            if i < len(code) and code[i] =='/':
                if code[i+1] == '/':
                    for j in range(i, len(code)):
                        if code[j] == '\n':
                            code = code[:i] + code[j:]
                            break
        return code

class SymbolTable:
    def __init__(self):
        self.table = {}

    def setter(self, key, value):
        self.table[key] = value
    
    def getter(self, key):
        if key in self.table.keys():
            return self.table[key]
        else:
            sys.stderr.write('[ERRO]\n')
            sys.exit()

class Node:
    def __init__(self, value: str, children: list = []):
        self.value = value 
        self.children = children 

    def Evaluate(self, ST) -> int:
        pass 
    
class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self, ST):
        left_value = self.children[0].Evaluate(ST)
        right_value = self.children[1].Evaluate(ST)

        if self.value == '+':
            return left_value + right_value
        elif self.value == '-':
            return left_value - right_value
        elif self.value == '*':
            return left_value * right_value
        elif self.value == '/':
            return left_value // right_value
        elif self.value == '==':
            return left_value == right_value
        elif self.value == '<':
            return left_value < right_value
        elif self.value == '>':
            return left_value > right_value
        elif self.value == 'e':
            return left_value and right_value
        elif self.value == 'ou':
            return left_value or right_value
        else:
            sys.stderr.write('[ERRO]\n')
            sys.exit()

class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self, ST):
        value = self.children[0].Evaluate(ST)

        if self.value == '-':
            return -value
        elif self.value == '!':
            return not value
        else:
            return value

class IntVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self, ST):
        return int(self.value)

class NoOp(Node):
    def __init__(self):
        super().__init__(0, [])
    
    def Evaluate(self, ST):
        return 0

class Identifier(Node):
    def __init__(self, value: str, children: list = []):
        super().__init__(value, children)

    def Evaluate(self, ST):
        return ST.getter(self.value)
    
class Assignment(Node): 
    def __init__(self, value: str, children: list = []):
        super().__init__(value, children)

    def Evaluate(self, ST):
        value = self.children[1].Evaluate(ST)
        ST.setter(self.children[0].value, value)
    
class Block(Node):
    def __init__(self, children: list = []):
        super().__init__("", children)

    def Evaluate(self, ST):
        for child in self.children:
            res = child.Evaluate(ST)
            if isinstance(child, Return):
                return res

class Print(Node):
    def __init__(self, value: str, children: list = []):
        super().__init__(value, children)

    def Evaluate(self, ST):
        print(self.children[0].Evaluate(ST))
    
class If(Node):
    def __init__(self, value: str, children: list = []):
        super().__init__(value, children)

    def Evaluate(self, ST):
        conditional = self.children[0].Evaluate(ST)
        if conditional:
            self.children[1].Evaluate(ST)
        else:
            if len(self.children) == 3:
                self.children[2].Evaluate(ST)

class Read(Node):
    def __init__(self, value: str = None, children: list = []):
        super().__init__(value, children)

    def Evaluate(self, ST):
        return input()

class VarDecl(Node):
    def __init__(self, value: str, children: list):
        super().__init__(value, children)

    def Evaluate(self, ST):
        identifier = self.children[0]
        value = self.children[1]

        if isinstance(value, Node):
            value = value.Evaluate(ST)[0]

        ST.declarator(identifier.value, value)

class StringVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self, ST):
        return str(self.value)'

class Token:
    def __init__(self, type: str, value: int):
        self.type = type
        self.value = value

class Tokenizer:
    def __init__(self, source: str, position: int, next: Token):
        self.source = source
        self.position = 0 
        self.next = None 
        
    def selectNext(self):
        while self.position < len(self.source) and self.source[self.position] == " ":
            self.position += 1
            
        if self.position >= len(self.source):
            self.next = Token("EOF", None)
            return

        elif self.source[self.position].isdigit():
            token = self.source[self.position]
            i = 1
            while token.isdigit():
                i += 1
                if self.position + i > len(self.source):
                    break
                token = self.source[self.position : self.position + i]

            self.next = Token("INT", int(self.source[self.position : self.position + i - 1]))
            self.position += i - 1
        
        elif self.source[self.position] == "+":
            self.next = Token("MAIS", "+")
            self.position += 1
        
        elif self.source[self.position] == "-":
            self.next = Token("MENOS", "-")
            self.position += 1

        elif self.source[self.position] == "/":
            self.next = Token("DIVIDIDO", "/")
            self.position += 1
        
        elif self.source[self.position] == "*":
            self.next = Token("VEZES", "*")
            self.position += 1

        elif self.source[self.position] == "(":
            self.next = Token("ABRE_PARENTESES", "(")
            self.position += 1

        elif self.source[self.position] == ")":
            self.next = Token("FECHA_PARENTESES", ")")
            self.position += 1

        elif self.source[self.position] == "{":
            self.next = Token("ABRE_CHAVES", "{")
            self.position += 1
        
        elif self.source[self.position] == "}":
            self.next = Token("FECHA_CHAVES", "}")
            self.position += 1

        elif self.source[self.position] == ";":
            self.next = Token("SEMICOLON", ";")
            self.position += 1

        elif self.source[self.position] == "=":
            if self.source[self.position + 1] == "=":
                self.next = Token("IGUAL", "==")
                self.position += 2
            else:
                self.next = Token("ASSIGNMENT", "=")
                self.position += 1
        
        elif self.source[self.position] == "\n":
            self.next = Token("FIM", "\n")
            self.position += 1

        elif self.source[self.position] == ">":
            self.next = Token("MAIOR", ">") 
            self.position += 1
        
        elif self.source[self.position] == "<":
            self.next = Token("MENOR", "<")
            self.position += 1

        elif self.source[self.position] == "!":
            self.next = Token("NOT", "!")
            self.position += 1

        elif self.source[self.position] == ",":
            self.next = Token("COMMA", ",")
            self.position += 1

        elif self.source[self.position] == "\"":
            token = self.source[self.position]
            i = 1
            while self.position + i < len(self.source) and self.source[self.position + i] != "\"":
                i += 1
                token = self.source[self.position : self.position + i]

            if self.position + i >= len(self.source):
                sys.stderr.write('[ERRO]\n')
                sys.exit()

            self.next = Token("STRING", self.source[self.position + 1 : self.position + i])
            self.position += i + 1

        elif self.source[self.position].isalnum() or self.source[self.position] == "_":
            token = self.source[self.position]
            i = 1
            while self.position + i < len(self.source) and (self.source[self.position + i].isalnum() or self.source[self.position + i] == "_"):
                i += 1
                token = self.source[self.position : self.position + i]

            self.next = Token("IDENTIFIER", token)
            self.position += i

            if self.next.value in reserved_words:
                if self.next.value == "imprime":
                    self.next = Token("PRINTLN", self.next.value)
                elif self.next.value == "se":
                    self.next = Token("IF", self.next.value)
                elif self.next.value == "senao":
                    self.next = Token("ELSE", self.next.value)
                elif self.next.value == "e":
                    self.next = Token("AND", self.next.value)
                elif self.next.value == "ou":
                    self.next = Token("OR", self.next.value)

        else:
            sys.stderr.write('[ERRO]\n')
            sys.exit()

class Parser:
    def __init__(self, tokenizer: Tokenizer = None):
        self.tokenizer = tokenizer

    def run(self, code: str):
        self.tokenizer = Tokenizer(code, 0, None)
        self.tokenizer.selectNext()
        resultado = self.parseBlock()

        if self.tokenizer.next.type != "EOF":
            sys.stderr.write('[ERRO]\n')
            sys.exit()

        ST = SymbolTable()

        return resultado.Evaluate(ST)
    
    def parseExpression(self):
        resultado = self.parseTerm()
        while self.tokenizer.next.type == "MAIS" or self.tokenizer.next.type == "MENOS" or self.tokenizer.next.type == "OR":
            if self.tokenizer.next.type == "MAIS":
                self.tokenizer.selectNext()
                resultado = BinOp('+', [resultado, self.parseTerm()])
            elif self.tokenizer.next.type == "MENOS":
                self.tokenizer.selectNext()
                resultado = BinOp('-', [resultado, self.parseTerm()])
            elif self.tokenizer.next.type == "OR":
                self.tokenizer.selectNext()
                resultado = BinOp('ou', [resultado, self.parseTerm()])
        return resultado 

    def parseTerm(self):
        resultado = self.parseFactor()
        while self.tokenizer.next.type == "VEZES" or self.tokenizer.next.type == "DIVIDIDO" or self.tokenizer.next.type == "AND":
            if self.tokenizer.next.type == "VEZES":
                self.tokenizer.selectNext()
                resultado = BinOp('*', [resultado, self.parseFactor()])
            elif self.tokenizer.next.type == "DIVIDIDO":
                self.tokenizer.selectNext()
                resultado = BinOp('/', [resultado, self.parseFactor()])
            elif self.tokenizer.next.type == "AND":
                self.tokenizer.selectNext()
                resultado = BinOp('e', [resultado, self.parseFactor()])
            else:
                sys.stderr.write('[ERRO]\n')
                sys.exit()
        return resultado

    def parseFactor(self):
        if self.tokenizer.next.type == "INT":
            resultado = self.tokenizer.next.value
            resultado = IntVal(resultado, [])
            self.tokenizer.selectNext()
            return resultado
        elif self.tokenizer.next.type == "IDENTIFIER":
            func_name = self.tokenizer.next.value
            resultado = Identifier(func_name, [])
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "ABRE_PARENTESES":
                args_list = []
                self.tokenizer.selectNext()
                if self.tokenizer.next.type != "FECHA_PARENTESES":
                    args_list.append(self.RelExpr())
                    while self.tokenizer.next.type == "COMMA":
                        self.tokenizer.selectNext()
                        args_list.append(self.RelExpr())
                if self.tokenizer.next.type == "FECHA_PARENTESES":
                    self.tokenizer.selectNext()
                    resultado = FuncCall(func_name, args_list)
                else:
                    sys.stderr.write('[ERRO]\n')
                    sys.exit()
                resultado = FuncCall(func_name, args_list)
            return resultado
        elif self.tokenizer.next.type == "STRING":
            resultado = self.tokenizer.next.value
            resultado = StringVal(resultado, [])
            self.tokenizer.selectNext()
            return resultado
        elif self.tokenizer.next.type == "MAIS" or self.tokenizer.next.type == "MENOS" or self.tokenizer.next.type == "NOT":
            if self.tokenizer.next.type == "MAIS":
                self.tokenizer.selectNext()
                resultado = self.parseFactor()
                resultado = UnOp('+', [resultado])
                return resultado
            elif self.tokenizer.next.type == "MENOS":
                self.tokenizer.selectNext()
                resultado = self.parseFactor()
                resultado = UnOp('-', [resultado])
                return resultado
            elif self.tokenizer.next.type == "NOT":
                self.tokenizer.selectNext()
                resultado = self.parseFactor()
                resultado = UnOp('!', [resultado])
                return resultado
        elif self.tokenizer.next.type == "ABRE_PARENTESES":
            self.tokenizer.selectNext()
            resultado = self.RelExpr()
            if self.tokenizer.next.type == "FECHA_PARENTESES":
                self.tokenizer.selectNext()
                return resultado
            else:
                sys.stderr.write('[ERRO]\n')
                sys.exit()
        elif self.tokenizer.next.type == "FECHA_PARENTESES":
            sys.stderr.write('[ERRO]\n')
            sys.exit()
        elif self.tokenizer.next.type == "READLINE":
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "ABRE_PARENTESES":
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == "FECHA_PARENTESES":
                    self.tokenizer.selectNext()
                    return Read()
                else:
                    sys.stderr.write('[ERRO]\n')
                    sys.exit()
        else:
            sys.stderr.write('[ERRO]\n')
            sys.exit()
        
    def RelExpr(self):
        resultado = self.parseExpression()
        while self.tokenizer.next.type == "IGUAL" or self.tokenizer.next.type == "MENOR" or self.tokenizer.next.type == "MAIOR":
            if self.tokenizer.next.type == "IGUAL":
                self.tokenizer.selectNext()
                resultado = BinOp('==', [resultado, self.parseExpression()])
            elif self.tokenizer.next.type == "MENOR":
                self.tokenizer.selectNext()
                resultado = BinOp('<', [resultado, self.parseExpression()])
            elif self.tokenizer.next.type == "MAIOR":
                self.tokenizer.selectNext()
                resultado = BinOp('>', [resultado, self.parseExpression()])
        return resultado

    def parseBlock(self):
        nodes = []
        while self.tokenizer.next.type != "EOF":
            nodes.append(self.parseStatement())
            self.tokenizer.selectNext()
        self.tokenizer.selectNext()
        return Block(nodes)
    
    def parseStatement(self):
        if self.tokenizer.next.type == "IDENTIFIER":
            identifier = Identifier(self.tokenizer.next.value, [])
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "ASSIGNMENT":
                self.tokenizer.selectNext()
                resultado = Assignment("=" , [identifier, self.RelExpr()])
            elif self.tokenizer.next.type == "ABRE_PARENTESES":
                self.tokenizer.selectNext()
                args_list = []
                if self.tokenizer.next.type != "FECHA_PARENTESES":
                    args_list.append(self.RelExpr())
                    while self.tokenizer.next.type == "COMMA":
                        self.tokenizer.selectNext()
                        args_list.append(self.RelExpr())
                if self.tokenizer.next.type == "FECHA_PARENTESES":
                    resultado = FuncCall(identifier.value, args_list)
                    self.tokenizer.selectNext()
                else:
                    sys.stderr.write('[ERRO]\n')
                    sys.exit()
            else: 
                sys.stderr.write('[ERRO]\n')
                sys.exit()
            if self.tokenizer.next.type == "SEMICOLON":
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == "FIM":
                    return resultado
                else:
                    sys.stderr.write('[ERRO]\n')
                    sys.exit()
            else:
                sys.stderr.write('[ERRO]\n')
                sys.exit()
        elif self.tokenizer.next.type == "PRINTLN":
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "ABRE_PARENTESES":
                self.tokenizer.selectNext()
                resultado = Print("PRINTLN", [self.RelExpr()])
                if self.tokenizer.next.type == "FECHA_PARENTESES":
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == "SEMICOLON":
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.type == "FIM":
                            return resultado
                        else:
                            sys.stderr.write('[ERRO]\n')
                            sys.exit()
                    else:
                        sys.stderr.write('[ERRO]\n')
                        sys.exit()
                else:
                    sys.stderr.write('[ERRO]\n')
                    sys.exit()
        elif self.tokenizer.next.type == "IF":
            self.tokenizer.selectNext()
            condition = self.RelExpr()
            if self.tokenizer.next.type == "ABRE_CHAVES":
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == "FIM":
                    if_children = []
                    self.tokenizer.selectNext()
                    while self.tokenizer.next.type != "FECHA_CHAVES" and self.tokenizer.next.type != "ELSE":
                        if_children.append(self.parseStatement())
                        self.tokenizer.selectNext()
                    if_block = Block(if_children)
                    if self.tokenizer.next.type == "FECHA_CHAVES":
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.type == "ELSE":
                            self.tokenizer.selectNext()
                            if self.tokenizer.next.type == "ABRE_CHAVES":
                                self.tokenizer.selectNext()
                                if self.tokenizer.next.type == "FIM":   
                                    else_children = []
                                    self.tokenizer.selectNext()
                                    while self.tokenizer.next.type != "FECHA_CHAVES":
                                        else_children.append(self.parseStatement())
                                        self.tokenizer.selectNext()
                                    else_block = Block(else_children)
                                    if self.tokenizer.next.type == "FECHA_CHAVES":
                                        self.tokenizer.selectNext()
                                        return If("IF", [condition, if_block, else_block])
                                    else:
                                        sys.stderr.write('[ERRO]\n')
                                        sys.exit()
                        elif self.tokenizer.next.type == "FIM":
                            self.tokenizer.selectNext()
                            return If("IF", [condition, if_block])
                    else:
                        sys.stderr.write('[ERRO]\n')
                        sys.exit()
            else:
                sys.stderr.write('[ERRO]\n')
                sys.exit()
        elif self.tokenizer.next.type == "FIM":
            return NoOp()
        else:
            sys.stderr.write('[ERRO]\n')
            sys.exit()

if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        input = f.read()
    filtered = PrePro.filter(input)
    parser = Parser()
    parser.run(filtered)
