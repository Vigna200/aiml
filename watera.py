# -----DFA-----------------------------
KEYWORDS = {"int", "float", "char", "if", "else", "while", "return", "true", "false", "print"}
OPERATORS = {"+", "-", "*", "/", "=", "<", ">"}
DOUBLE_OPERATORS = {"==", "<=", ">=", "!="}
SPECIAL_SYMBOLS = {";", ",", "(", ")", "{", "}", ":"}
def tokenize(code):
    tokens = []
    i = 0
    n = len(code)
    while i < n:
        ch = code[i]
        if ch.isspace():
            i += 1
            continue
        if ch == '/' and i + 1 < n and code[i + 1] == '/':
            while i < n and code[i] != '\n':
                i += 1
            continue
        if ch.isalpha() or ch == "_":
            start = i
            i += 1
            while i < n and (code[i].isalnum() or code[i] == "_"):
                i += 1
            lexeme = code[start:i]
            if lexeme in KEYWORDS:
                token_type = "KEYWORD"
            else:
                token_type = "IDENTIFIER"
            tokens.append((lexeme, token_type))
            continue
        if ch.isdigit():
            start = i
            has_dot = False
            i += 1
            while i < n and (code[i].isdigit() or (code[i] == "." and not has_dot)):
                if code[i] == ".":
                    has_dot = True
                i += 1
            tokens.append((code[start:i], "CONSTANT"))
            continue
        if i + 1 < n and code[i:i + 2] in DOUBLE_OPERATORS:
            tokens.append((code[i:i + 2], "OPERATOR"))
            i += 2
            continue
        if ch in OPERATORS:
            tokens.append((ch, "OPERATOR"))
            i += 1
            continue
        if ch in SPECIAL_SYMBOLS:
            tokens.append((ch, "SPECIAL SYMBOL"))
            i += 1
            continue
        if ch == '"':
            start = i
            i += 1
            while i < n:
                if code[i] == '"' and code[i - 1] != '\\':
                    i += 1
                    break
                i += 1
            tokens.append((code[start:i], "STRING"))
            continue
        tokens.append((ch, "INVALID"))
        i += 1
    return tokens
def display_dfa(lexeme, token_type):
    print(f"\nLexeme: {lexeme}")
    print("Start State: q0")
    current_state = "q0"
    for i, ch in enumerate(lexeme):
        next_state = f"q{i + 1}"
        print(f"{current_state} -- {ch} --> {next_state}")
        current_state = next_state
    print(f"Final State: {current_state} ({token_type})")
def lexical_analyzer(code):
    tokens = tokenize(code)
    print("\nTokens:")
    for lexeme, token_type in tokens:
        print(f"{lexeme}  ->  {token_type}")
    print("\nDFA Representation:")
    for lexeme, token_type in tokens:
        display_dfa(lexeme, token_type)
print("Enter your code (finish input with an empty line):")
lines = []
while True:
    try:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    except EOFError:
        break
source_code = "\n".join(lines)
lexical_analyzer(source_code)
#-----------------------------------hexadecimal/octal---------------
%{
#include <stdio.h>
%}
KEYWORD     int|float|char|double|if|else|while|for|return
ID          [a-zA-Z_][a-zA-Z0-9_]*
NUMBER      [0-9]+
OPERATOR    [+-*/=<>]
SEPARATOR   [(),;{}]
%%
{KEYWORD}      { printf("KEYWORD : %s\n", yytext); }
{ID}           { printf("IDENTIFIER : %s\n", yytext); }
{NUMBER}       { printf("NUMBER : %s\n", yytext); }
{OPERATOR}     { printf("OPERATOR : %s\n", yytext); }
{SEPARATOR}    { printf("SEPARATOR : %s\n", yytext); }
[ \t\n]+       ;        /* Ignore whitespace */
.              { printf("UNKNOWN : %s\n", yytext); }
%%
int yywrap()
{
return 1;
}

int main()
{
printf("Enter the code:\n");
yylex();
return 0;
}
#-----------------------------------------capitalize an entire string---
%{
#include <stdio.h>
#include <ctype.h>
%}
%%
[a-z]      { putchar(toupper(yytext[0])); }   /* convert lowercase to uppercase */
[A-Z]      { putchar(yytext[0]); }            /* keep uppercase as it is */
\n         { putchar('\n'); }                 /* print newline */
.          { putchar(yytext[0]); }            /* print other characters */
%%
int main()
{
printf("Enter a string:\n");
yylex();
return 0;
}

int yywrap()
{
return 1;
}
#-------------------------------------Capitalize First Letter
%{
#include <stdio.h>
#include <ctype.h>
int newword = 1;
%}
%%
[ \t\n]   { putchar(yytext[0]); newword = 1; }
[a-zA-Z]
{
if(newword)
{
putchar(toupper(yytext[0]));
newword = 0;
}
else
putchar(yytext[0]);
}
.   { putchar(yytext[0]); newword = 0; }
%%
int main()
{
printf("Enter text:\n");
yylex();
return 0;
}
int yywrap()
{
return 1;
}
#------------------Integer or Real Number
%{
#include <stdio.h>
%}
%%
^[0-9]+$            { printf("Integer\n"); }
^[0-9]+.[0-9]+$    { printf("Real Number\n"); }
.|\n                { }
%%
int main()
{
printf("Enter a number:\n");
yylex();
return 0;
}
int yywrap()
{
return 1;
}
#-----------------Even or Odd Number
%{
#include <stdio.h>
#include <stdlib.h>
%}
%%
[0-9]+
{
int num = atoi(yytext);
```
if(num % 2 == 0)
    printf("Even\n");
else
    printf("Odd\n");
```
}
\n      { }
%%
int main()
{
printf("Enter a number:\n");
yylex();
return 0;
}
int yywrap()
{
return 1;
}
#-----------------------Vowel or Consonant
%{
#include <stdio.h>
#include <ctype.h>
%}
%%
[a-zA-Z]
{
char ch = tolower(yytext[0]);
```
if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')
    printf("Vowel\n");
else
    printf("Consonant\n");
```
}
\n      { }
.       { }
%%
int main()
{
printf("Enter a character:\n");
yylex();
return 0;
}
int yywrap()
{
return 1;
}
#----------------------------------------------Parse Tree from XML and a List.
import xml.etree.ElementTree as ET
class ParseTreeNode:
def **init**(self, value, children=None):
self.value = value
self.children = children if children is not None else []
```
def __repr__(self):
    return f"ParseTreeNode(value={self.value}, children={self.children})"
```
def parse_xml(input_xml):
tree = ET.ElementTree(ET.fromstring(input_xml))
root = tree.getroot()
```
def recursive_parse_element(element):
    children = [recursive_parse_element(child) for child in element]
    if children:
        return ParseTreeNode(element.tag, children)
    else:
        return ParseTreeNode(element.tag, [element.text])
return recursive_parse_element(root)
```
def parse_list(input_list):
if isinstance(input_list, list):

```
    if len(input_list) == 3 and isinstance(input_list[0], int) and isinstance(input_list[2], int):
        return ParseTreeNode(
            input_list[1],
            [
                ParseTreeNode(str(input_list[0])),
                ParseTreeNode(str(input_list[2]))
            ]
        )
    else:
        return ParseTreeNode("Unknown", [ParseTreeNode(str(item)) for item in input_list])

else:
    return ParseTreeNode("Invalid", [])
```
xml_input = """ <expr> <num>3</num> <op>+</op> <num>5</num> </expr>
"""
list_input = [3, "+", 5]
xml_tree = parse_xml(xml_input)
print("XML Parse Tree:")
print(xml_tree)
list_tree = parse_list(list_input)
print("\nList Parse Tree:")
print(list_tree)
#-----------------------Parser Without Scanner
%{
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
%}
%token NUMBER
%%
input : expr '\n'          { printf("Result = %d\n", $1); }
;
expr  : expr '+' term      { $$ = $1 + $3; }
| expr '-' term      { $$ = $1 - $3; }
| term               { $$ = $1; }
;
term  : term '*' factor    { $$ = $1 * $3; }
| term '/' factor    { $$ = $1 / $3; }
| factor             { $$ = $1; }
;
factor : NUMBER            { $$ = $1; }
| '(' expr ')'      { $$ = $2; }
;
%%
int yylex()
{
int c;
```
while ((c = getchar()) == ' ' || c == '\t');
if (isdigit(c))
{
    ungetc(c, stdin);
    scanf("%d", &yylval);
    return NUMBER;
}
if (c == '\n')
    return '\n';
return c;   /* operators: + - * / ( ) */
```
}
void yyerror(const char *s)
{
printf("Syntax Error\n");
}
int main()
{
printf("Enter expression: ");
yyparse();
return 0;
}
#-----------------------------Parser With Scanner
#calc.l
%{
#include "y.tab.h"
#include <stdlib.h>
%}
%%
[0-9]+      { yylval = atoi(yytext); return NUMBER; }
"+"         { return PLUS; }
"-"         { return MINUS; }
"*"         { return MUL; }
"/"         { return DIV; }
"("         { return LPAREN; }
")"         { return RPAREN; }
\n          { return '\n'; }
[ \t]       { }   /* ignore whitespace */
.           { printf("Invalid character: %s\n", yytext); }
%%
int yywrap() {
    return 1;
}
#calc.y
%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
%}
%token NUMBER PLUS MINUS MUL DIV LPAREN RPAREN
%%
input : expr '\n'        { printf("Result = %d\n", $1); }
      ;
expr  : expr PLUS term    { $$ = $1 + $3; }
      | expr MINUS term   { $$ = $1 - $3; }
      | term              { $$ = $1; }
      ;
term  : term MUL factor   { $$ = $1 * $3; }
      | term DIV factor   { $$ = $1 / $3; }
      | factor            { $$ = $1; }
      ;
factor : NUMBER           { $$ = $1; }
       | LPAREN expr RPAREN { $$ = $2; }
       ;
%%
int main() {
    printf("Enter expression: ");
    yyparse();
    return 0;
}
void yyerror(const char *s) {
    printf("Syntax Error\n");
}
#--------------------------------ll(1)parser
from collections import defaultdict
G = {
    "E": [["T","E'"]],
    "E'":[["+", "T", "E'"], ["ε"]],
    "T": [["F","T'"]],
    "T'":[["*", "F", "T'"], ["ε"]],
    "F":[["(","E",")"], ["id"]]
}
non_terminals = list(G.keys())
terminals = ["id","+","*","(",")","$"]
FIRST = defaultdict(set)
FOLLOW = defaultdict(set)
def first(X):
    if X not in G:
        return {X} # terminal
    if FIRST[X]:
        return FIRST[X]
    for p in G[X]:
        for s in p:
            f = first(s)
            FIRST[X] |= f - {"ε"}
            if "ε" not in f:
                break
        else:
            FIRST[X].add("ε")
    return FIRST[X]
for nt in non_terminals:
    first(nt)
FOLLOW["E"].add("$")
change = True
while change:
    change = False
    for A in G:
        for p in G[A]:
            for i, B in enumerate(p):
                if B in G:
                    beta = p[i+1:]
                    fb = set()
                    if beta:
                        for s in beta:
                            f = FIRST[s] if s in G else {s}
                            fb |= f - {"ε"}
                            if "ε" not in f:
                                break
                        else:
                            fb.add("ε")
                    else:
                        fb.add("ε")
                    old = len(FOLLOW[B])
                    FOLLOW[B] |= fb - {"ε"}
                    if "ε" in fb:
                        FOLLOW[B] |= FOLLOW[A]
                    if len(FOLLOW[B]) > old:
                        change = True
table = {A:{t:None for t in terminals} for A in non_terminals}
for A in G:
    for prod in G[A]:
        first_prod = set()
        for s in prod:
            f = FIRST[s] if s in G else {s}
            first_prod |= f - {"ε"}
            if "ε" not in f:
                break
        else:
            first_prod.add("ε")
        for t in first_prod - {"ε"}:
            table[A][t] = prod
        if "ε" in first_prod:
            for t in FOLLOW[A]:
                table[A][t] = ["ε"]
print("\nLL(1) Parsing Table:")
col_widths = {}
for t in ["NT"] + terminals:
    col_widths[t] = max(len(t), 5)
for nt in non_terminals:
    for t in terminals:
        prod = table[nt][t]
        prod_str = "".join(prod) if prod else ""
        col_widths[t] = max(col_widths[t], len(prod_str))
header = ["NT"] + terminals
header_row = " | ".join(h.center(col_widths[h]) for h in header)
print(header_row)
print("-"*len(header_row))
for nt in non_terminals:
    row = [nt.center(col_widths["NT"])]
    for t in terminals:
        prod = table[nt][t]
        prod_str = "".join(prod) if prod else ""
        row.append(prod_str.center(col_widths[t]))
    print(" | ".join(row))
def is_valid_expression(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isalpha():
            tokens.append("id")
            i += 1
        elif expr[i] in "+*()":
            tokens.append(expr[i])
            i += 1
        elif expr[i] == " ":
            i += 1
        else:
            return False
    tokens.append("$") # end marker
    stack = ["$", "E"]
    idx = 0
    while stack:
        top = stack.pop()
        current = tokens[idx]
        if top in terminals:
            if top == current:
                idx += 1
            else:
                return False
        else:
            prod = table[top].get(current)
            if not prod:
                return False
            if prod != ["ε"]:
                for symbol in reversed(prod):
                    stack.append(symbol)
    return idx == len(tokens)
while True:
    expr = input("\nEnter an expression (or 'exit' to quit): ")
    if expr.lower() == "exit":
        break
    if is_valid_expression(expr):
        print(f"Expression '{expr}' is VALID ")
    else:
        print(f"Expression '{expr}' is INVALID ")
