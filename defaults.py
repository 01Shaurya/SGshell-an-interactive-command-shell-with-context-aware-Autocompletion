####################################################################################
                               ##TOKEN LIST ##
####################################################################################
DIGITS="1234567890"
COMMANDS=["assoc","attrib",
          "break","call","cd","chdir","cls","cmd","color","comp","copy",
          "date","dir","doskey",
          "echo","exit",
          "fc","find","findstr","for","ftype",
          "goto",
          "help","hostname",
          "if",
          "label",
          "md","mkdir","mklink","more","move",
          "path","pause","popd","prompt","pushd",
          "rd","rem","ren","rename","replace","rmdir",
          "set","setlocal","shift","sort","start","subst",
          "tasklist","taskkill","time","title","tree","type",
          "ver","verify","vol",
          "whoami",
          "xcopy"]


SYMBOLS=["\'"
         ,'\"'
         ,")"
         ,"("
         ,">"
         ,"^"
         ,"!"
         ,"&"
         ,"<"
         ,"|"
         ,"%"
         ,"*"
         ,"+"
         ,"-"
         ,"?"
         ,"\\"
         ,"."
         ,"/"
         ,":"]

SYMBOL_TOKENS={
    "\'": "SQUOTE",
    '\"': "DQUOTE",
    ")": "RPARAN",
    "(": "LPARAN",
    ">": "OUTREDIRECT",
    ">>": "APPENDREDIRECT",
    "^": "ESCAPE",
    "!": "DELAYEDEXPANSION",
    "&": "CMDSEPARATOR",
    "&&": "ANDTHEN",
    "<": "INREDIRECT",
    "|": "PIPE",
    "||": "ORELSE",
    "%": "VARIABLE",
    "*": "WILDCARD",
    "+": "PLUS",
    "-": "MINUS",
    "?": "SINGLEWILDCARD",
    "\\": "BACKSLASH",
    ".": "DOT",
    "..": "PARENTDIR",
    "/": "OPTIONPREFIX",
    ":": "COLON"
}
EOF="EOF"


####################################################################################
                               ##STANDARD TOKEN TYPE ##
####################################################################################

COMMAND="COMMAND"
SYMBOL="SYMBOL"
LITERAL="LITERAL"
INVALID="INVALID"