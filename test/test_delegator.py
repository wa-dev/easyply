
import easyply
import ply.lex as lex
import ply.yacc as yacc


class Lexer(object):
  tokens = ('A', )

  t_A = r'\w+'

  lexer = lex.lex()

def Location(term_name, p, i):
  loc = {
       'line' : p.lineno(i),
       'pos'  : p.lexpos(i),
        }
  return (p[i], loc, term_name)

class Parser(Lexer):
  @easyply.delegate(Location)
  def px_test(self, a):
    '''production: {A}'''
    global _parser
    assert self is _parser
    return a

  def parse(self, text):
    easyply.process_all(self)
    self.parser = yacc.yacc(module=self)
    return self.parser.parse(text, tracking=True)

def test_delegate():
  global _parser
  _parser = Parser()
  result = _parser.parse('Hello')
  assert result == ('Hello', {'line': 1, 'pos': 0}, 'a')

