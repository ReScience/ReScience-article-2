chiefs = ["rougier", "khinsen"]
editors = ["otizonaizit", "pdebuyl", "ctb", "ThomasA", "tpoisot",
#          "emmanuelle"
           "benoit-girard", "karthik", "oliviaguest", "labarba"]
reviewers = ["benoit-girard", "MehdiKhamassi", "vitay", "gdetor", "dmcglinn",
             "yoavram",  "FedericoV", "heplesser", "apdavison",
             "neuronalX", "piero-le-fou", "mstimberg", "rossant", "eroesch",
             "damiendr", "delsuc", "soolijoo", "benureau", "rth", "KamilSJaron",
             "TiinaManninen",
#             "ogrisel",
             "almarklein", "pietromarchesi", "anyaevostinar","ozancaglayan",
             "aaronshifman"]
replicators = ["gviejo", "gdetor", "MehdiKhamassi", "benoit-girard", "opetchey",
               "Vahidrostami", "jsta", "Fjanks", "ChristophMetzner", "vitay",
               "akdiem", # "andruhamax",
               "falex33", "aaronshifman", "RafaelNH"]

authors = chiefs + editors + reviewers + replicators

for author in authors:
    print("@%s, " % author, end="")
print()
print(len(authors))
