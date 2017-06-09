import re

authors = [ # "rougier", "khinsen",
           "otizonaizit", "pdebuyl", "emmanuelle", 
           "ctb", "ThomasA", "tpoisot", "karthik", "oliviaguest",
           "labarba", "MehdiKhamassi", "benoit-girard", "vitay",
           "gdetor", "dmcglinn", "yoavram", "FedericoV", "AdamRTomkins",
           "heplesser", "apdavison", "neuronalX", "piero-le-fou",
           "mstimberg", "rossant", "eroesch", "damiendr", "delsuc",
           "soolijoo", "benureau", "rth", "almarklein", "pietromarchesi",
           "aaronshifman", "anyaevostinar","ozancaglayan", "ogrisel",
           "jsta", "opetchey", "aaronshifman"]


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
            # Hack for sorting without taking care of unicode
            if name == "Ozan Çağlayan": name = "Ozan CÇağlayan"
            
        match = orcid_re.match(line)
        if match:
            orcid = match.group("orcid")
            board[name] = [handle, orcid]
            if handle in authors:
                names.append(name)

# Adding authors by hand (they're not part of the board)
board["Guillaume Viejo"] = ["gviejo", "---"]
board["Andrei Maksimov"] = ["andruhamax", "---"]
board["Erwan Le Masson"] = ["maekclena", "---"]
board["Rafael Neto Henriques"] = ["RafaelNH", "---"]
board["Vahid Rostami"] = ["Vahidrostami", "---"]

names.extend(["Guillaume Viejo", "Andrei Maksimov", "Erwan Le Masson",
              "Rafael Neto Henriques", "Vahid Rostami"])

names.sort(key=lambda s: s.split()[-1])
names = ["Nicolas P. Rougier", "Konrad Hinsen"] + names

for i,name in enumerate(names):
    handle, orcid = board[name]

    # Hack for sorting without taking care of unicode
    if name == "Ozan CÇağlayan":
        name = "Ozan Çağlayan"
    
    print("\\textbf{%s}$^{%d}$" % (name, i+1), end="") 
    if orcid != "---":
        print ("\href{http://orcid.org/%s}{\includegraphics[width=10pt]{orcid}}"
               % orcid, end="")
#    print ("\href{https://github.com/%s}{\includegraphics[width=10pt]{github}},"
#               % handle)
    if i < len(names)-1:
        print(",\n%%")
    else:
        print("\\\\")

#for i,name in enumerate(names):
#    orcid = board[name][1]
#    print("""$^{%d}$ \includegraphics[width=10pt]{iD-icon.pdf}
#             \\href{http://orcid.org/%s}{orcid.org/%s} |"""" % (i+1, orcid, orcid))
