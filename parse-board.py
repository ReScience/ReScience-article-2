import re

authors = [ # "rougier", "khinsen",
           "otizonaizit", "pdebuyl", "emmanuelle",
           "ctb", "ThomasA", "tpoisot", "karthik", "oliviaguest",
           "labarba", "MehdiKhamassi", "benoit-girard", "vitay",
           "gdetor", "dmcglinn", "yoavram", "FedericoV", "jsta",
           "heplesser", "apdavison", "neuronalX", "piero-le-fou",
           "mstimberg", "rossant", "eroesch", "damiendr", "delsuc",
           "soolijoo", "benureau", "rth", "almarklein", "pietromarchesi",
           "aaronshifman", "anyaevostinar","ozancaglayan", "ogrisel"]

name_re = re.compile("""\* \[(?P<name>.+)\]\(https://github.com/(?P<handle>.+)\)""")
orcid_re= re.compile("""  ORCID: \[(?P<orcid>.+)\]""")
handle_re = re.compile("""""")

board = {}
names = []
with open("../ReScience.github.io/04-board.md") as file:
    for line in file.readlines():
        match = name_re.match(line)
        if match:
            name  = match.group("name")
            handle = match.group("handle")
        match = orcid_re.match(line)
        if match:
            orcid = match.group("orcid")
            board[name] = [handle, orcid]
            if handle in authors:
                names.append(name)

names.sort(key=lambda s: s.split()[-1])
names = ["Nicolas P. Rougier", "Konrad Hinsen"] + names

for i,name in enumerate(names):
    orcid = board[name][1]
#    if orcid != "---":
#        print ("\\textbf{%s}$^{%d}$ \href{http://orcid.org/%s}{\includegraphics[width=10pt]{iD-icon.pdf}}," % (name, i+1, orcid))
#    else:
    print ("\\textbf{%s}$^{%d}$," % (name, i+1))

for i,name in enumerate(names):
    orcid = board[name][1]
    print("$^{%d}$ \includegraphics[width=10pt]{iD-icon.pdf} \\href{http://orcid.org/%s}{orcid.org/%s} |" % (i+1, orcid, orcid))
