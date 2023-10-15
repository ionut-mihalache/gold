parser grammar GOLDParser;

options {
    tokenVocab = GOLDLexer;
}

description: (blocks += descriptionBlock)* EOF;

descriptionBlock: DESCBLK name=NAME BLKSTART header=headerBlock body=bodyBlock BLKEND LINEEND;

headerBlock: HBLK BLKSTART (lblocks+=languageBlock)+ BLKEND LINEEND;

languageBlock: LBLK langname=LANGUAGE BLKSTART filesBlock typesBlock BLKEND LINEEND;

filesBlock: FBLK BLKSTART (files+=file)+ BLKEND LINEEND;

file: LSTSTART filename=STRINGVALUE COMMA startblock=NAME COMMA endblock=NAME LSTEND LINEEND;

typesBlock: TBLK BLKSTART (types+=type)+ BLKEND LINEEND;

type: goldtype=NAME EQ langtype=TYPEDEF LINEEND;

bodyBlock: BBLK BLKSTART (constants+=commonConst)+ BLKEND LINEEND;

commonConst: typeId=NAME varName=NAME EQ varValue=VALUEDEF LINEEND;
