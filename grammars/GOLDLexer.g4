lexer grammar GOLDLexer;

@members{
def raiseError(msg):
    setText(msg)
    setType(ERROR)
}

LINEEND: ';';
EQ: '=';
BLKSTART: '{';
BLKEND: '}';
LSTSTART: '[';
LSTEND: ']';
COMMA: ',';
fragment TAGSTART: '<';
fragment TAGEND: '>';
fragment COMMENTLIMIT: '%';

DESCBLK: 'description';
HBLK: 'header';
BBLK: 'body';
LBLK: 'language';
FBLK: 'files';
TBLK: 'types';
NULL: 'null';

LANGUAGE
    : 'php'
    | 'js'
    ;

NUMBER: [0-9][0-9]*;
NAME: [a-zA-Z0-9_]+;

STRINGVALUE: '"' ('\\"' | .)*? '"';

TYPEDEF: 't' TAGSTART .*? TAGEND;
VALUEDEF: 'v' TAGSTART .*? TAGEND;
COMMENT: COMMENTLIMIT (COMMENT | .)*? COMMENTLIMIT -> skip;

NL: [(\r)?\n]+ -> skip;
WS: [ \t]+ -> skip;

INVALID
    : '%' {self.raiseError("Unmatched %")}
    | . {self.raiseError("Bad character: " + getText())};
