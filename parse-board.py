import re

chiefs = ["rougier", "khinsen"]
editors = ["otizonaizit", "pdebuyl", "emmanuelle", "ctb", "ThomasA", "tpoisot",
           "karthik", "oliviaguest", "labarba"]
reviewers = ["MehdiKhamassi", "benoit-girard", "vitay", "gdetor", "dmcglinn",
             "yoavram", "FedericoV", "AdamRTomkins", "heplesser", "apdavison",
             "neuronalX", "piero-le-fou", "mstimberg", "rossant", "eroesch",
             "damiendr", "delsuc", "ogrisel", "soolijoo", "benureau", "rth",
             "almarklein", "pietromarchesi", "anyaevostinar","ozancaglayan",
             "aaronshifman"]
replicators = ["gviejo", "gdetor", "MehdiKhamassi", "benoit-girard", "opetchey",
               "Vahidrostami", "jsta", "Fjanks", "ChristophMetzner", "vitay",
               "andruhamax", "falex33", "aaronshifman", "RafaelNH"]

# Adding names that are not part of the board
board = {}
board["Guillaume Viejo"] = ["gviejo", "---"]
board["Andrei Maksimov"] = ["andruhamax", "---"]
board["Erwan Le Masson"] = ["maekclena", "---"]
board["Frédéric Alexandre"] = ["falex33", "0000-0002-6113-1878"]
board["Rafael Neto Henriques"] = ["RafaelNH", "---"]
board["Vahid Rostami"] = ["Vahidrostami", "---"]
board["Frank Stollmeier"] = ["Fjanks", "0000-0003-4858-0895"]

authors = list(set(editors+reviewers+replicators))
fullnames = list(board.keys())
replicators = replicators + ["rougier"]

# authors = [ # "rougier", "khinsen",
#            "otizonaizit", "pdebuyl", "emmanuelle", 
#            "ctb", "ThomasA", "tpoisot", "karthik", "oliviaguest",
#            "labarba", "MehdiKhamassi", "benoit-girard", "vitay",
#            "gdetor", "dmcglinn", "yoavram", "FedericoV", "AdamRTomkins",
#            "heplesser", "apdavison", "neuronalX", "piero-le-fou",
#            "mstimberg", "rossant", "eroesch", "damiendr", "delsuc",
#            "soolijoo", "benureau", "rth", "almarklein", "pietromarchesi",
#            "aaronshifman", "anyaevostinar","ozancaglayan", "ogrisel",
#            "jsta", "opetchey", "aaronshifman"]


name_re = re.compile("""\* \[(?P<name>.+)\]\(https://github.com/(?P<handle>.+)\)""")
orcid_re= re.compile("""  ORCID: \[(?P<orcid>.+)\]""")
handle_re = re.compile("""""")

# names = []
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
                fullnames.append(name)
                
#names.extend(["Guillaume Viejo", "Andrei Maksimov", "Erwan Le Masson",
#              "Rafael Neto Henriques", "Vahid Rostami"])

fullnames.sort(key=lambda s: s.split()[-1])
fullnames = ["Nicolas P. Rougier", "Konrad Hinsen"] + fullnames

for i,name in enumerate(fullnames):
    handle, orcid = board[name]

    # Hack for sorting without taking care of unicode
    if name == "Ozan CÇağlayan":
        name = "Ozan Çağlayan"
    
    print("\\textbf{%s}" % (name), end="")
    print("$^{%d" % (i+1), end="")
    if handle in editors or handle in chiefs:
        print("\dagger", end="")
    if handle in reviewers:
        print("\ddagger", end="")
    if handle in replicators:
        print("\S", end="")
    if handle == "rougier":
        print("\star", end="")
    print("}$", end="")
    
    if orcid != "---":
        print ("\href{http://orcid.org/%s}{\includegraphics[width=8pt]{orcid}}"
               % orcid, end="")
    if i < len(fullnames)-1:
        print(",\n%%")
    else:
        print("\\\\")

#for i,name in enumerate(names):
#    orcid = board[name][1]
#    print("""$^{%d}$ \includegraphics[width=10pt]{iD-icon.pdf}
#             \\href{http://orcid.org/%s}{orcid.org/%s} |"""" % (i+1, orcid, orcid))
