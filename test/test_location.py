
import easyply
import ply.lex as lex
import ply.yacc as yacc


class Lexer(object):
  tokens = ('A', )

  t_A = r'\w+'

  lexer = lex.lex()

class Parser(Lexer):

  def px_test(self, a):
    '''production: {A}'''
    global _parser
    assert self is _parser
    loc = easyply.location('a')
    return a, loc

  def parse(self, text):
    easyply.process_all(self)
    self.parser = yacc.yacc(module=self)
    return self.parser.parse(text, tracking=True)

def test_delegate():
  global _parser
  _parser = Parser()
  result = _parser.parse('Hello')
  assert result == ('Hello', {'lineno': 1, 'lexpos': 0, 'linespan':(1,1), 'lexspan':(0,0)})


if __name__ == '__main__':
  test_delegate()
#  import unittest
#  unittest.main()
