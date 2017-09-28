import re
import collections

affiliations = {
    "eroesch" : "Centre for Integrative Neuroscience, School of Psychology, University of Reading, UK",
    "ThomasA" : "Department of Electronic Systems, Faculty of Engineering and Science, Aalborg University, Denmark",
    "ChristophMetzner" : "Centre for Computer Science and Informatics Research, University of Hertfordshire, UK",
    "apdavison" : "Unité de Neurosciences, Information et Complexité, CNRS FRE 3693, Gif sur Yvette, France",
    "MehdiKhamassi":  "Institut des Systèmes Intelligent et de Robotique, Sorbonne Universités, UPMC Univ Paris 06, CNRS, Paris, France",
    "benoit-girard" : "Institut des Systèmes Intelligent et de Robotique, Sorbonne Universités, UPMC Univ Paris 06, CNRS, Paris, France",    
    "Vahidrostami": "Institute of Neuroscience \\& Medicine (INM-6) and Institute for Advanced Simulation (IAS-6) -- JARA-Brain Institute I (INM-10), Jülich Research Center, Jülich, Germany",
    "neuronalX" : "INRIA Bordeaux Sud-Ouest Talence, France – Institut des Maladies Neurodégénératives, Université de Bordeaux, CNRS UMR 5293, Bordeaux, France – LaBRI, Université de Bordeaux, Bordeaux INP, CNRS UMR 5800, Talence, France",
    "pietromarchesi" : "Swammerdam Institute for Life Sciences, Center for Neuroscience, Faculty of Science, University of Amsterdam, Amsterdam, the Netherlands",
    "vitay" :"Professorship for Artificial Intelligence, Department of Computer Science, Chemnitz University of Technology, Chemnitz, Germany",
    "rossant" : "Institute of Neurology, University College London, UK",
    "soolijoo" : "UCL Great Ormond St Institute of Child Health. University College London, London, UK",
    "oliviaguest" : "Experimental Psychology, University College London, UK",
    "mstimberg" : "Sorbonne Universités, UPMC Univ Paris 06, INSERM, CNRS, Institut de la Vision, Paris, France",
    "heplesser" : "Faculty of Science and Technology, Norwegian University of Life Sciences, Aas, Norway -- Institute of Neuroscience and Medicine (INM-6), Jülich Research Centre, Jülich, Germany",
    "rth" : "Symerio, Palaiseau, France",
    "delsuc" : "Institut de Génétique et de Biologie Moléculaire et Cellulaire, INSERM U964, CNRS UMR 7104, Université de Strasbourg, Illkirch, France",
    "dmcglinn" : "Department of Biology, College of Charleston, Charleston, SC, USA",
    "labarba" : "Department of Mechanical and Aerospace Engineering, the George Washington University, Washington DC, USA",
    "pdebuyl" : "Instituut voor Theoretische Fysica, KU Leuven, Belgium -- PdB is a postdoctoral fellow of the Research Foundation -- Flanders (FWO)",
    "jsta" : "Department of Fisheries and Wildlife, Michigan State University, MI, USA",     
    "Fjanks" : "Network Dynamics, Max Planck Institute for Dynamics and Self-Organization, Germany",
    "damiendr" : "Department of Computer Science, Humboldt-Universität zu Berlin",
    "gviejo" : "Montreal Neurological Institute, McGill University, Montreal, Canada",
    "otizonaizit" : "Neural Information Processing Group, University of Tübingen, Germany",
    "gdetor" : "Department of Cognitive Sciences, University of California Irvine, USA",
    "aaronshifman" : "Department of Biology, University of Ottawa, Ottawa, Ontario, Canada",
    "piero-le-fou" : "Friedman Brain Institute, Icahn School of Medicine at Mount Sinai, NY, USA",
    "almarklein" : "Independent scholar, Enschede, The Netherlands",
    "benureau" : "INRIA Bordeaux Sud-Ouest Talence, France – Institut des Maladies Neurodégénératives, Université de Bordeaux, CNRS UMR 5293, Bordeaux, France – LaBRI, Université de Bordeaux, Bordeaux INP, CNRS UMR 5800, Talence, France",
    "khinsen" : "Centre de Biophysique Moléculaire, CNRS UPR4301, Orléans, France -- Synchrotron SOLEIL, Division Expériences, Gif sur Yvette, France",
    "rougier" : "INRIA Bordeaux Sud-Ouest Talence, France – Institut des Maladies Neurodégénératives, Université de Bordeaux, CNRS UMR 5293, Bordeaux, France – LaBRI, Université de Bordeaux, Bordeaux INP, CNRS UMR 5800, Talence, France",
    "karthik" : "Berkeley Institute for Data Science, University of California Berkeley, Berkeley, CA, USA",
    "ozancaglayan" : "Laboratoire d'Informatique de l'Université du Maine (LIUM), Le Mans, France",
    "falex33" : "INRIA Bordeaux Sud-Ouest Talence, France – Institut des Maladies Neurodégénératives, Université de Bordeaux, CNRS UMR 5293, Bordeaux, France – LaBRI, Université de Bordeaux, Bordeaux INP, CNRS UMR 5800, Talence, France",    
    "RafaelNH" : "MRC Cognition and Brain Sciences Unit, Cambridge, UK",
    "yoavram" : "Department of Biology, Stanford University, Stanford, CA, USA",
    "anyaevostinar" : "Department of Computer Science, Grinnell College, IA, USA",
    "tpoisot" : "Département de Sciences Biologiques, Université de Montréal, Montréal, Canada",
    "ctb":  "Department of Population Health and Reproduction, University of California Davis, Davis, CA, USA",
    "opetchey" : "Department of Evolutionary Biology and Environmental Studies, University of Zurich, Switzerland",
    "FedericoV" : "Amazon, Seattle, USA",
    "akdiem" : "Computational Engineering and Design, Faculty of Engineering and the Environment, University of Southampton, UK",
    "KamilSJaron" : "Department of Ecology and Evolution, University of Lausanne, Lausanne, Switzerland",
    "TiinaManninen" : "BioMediTech Institute and Faculty of Biomedical Sciences and Engineering, Tampere University of Technology, Tampere, Finland"
}

# Commented names have declined or not answered yet
chiefs = ["rougier", "khinsen"]
editors = ["otizonaizit", "pdebuyl", "ctb", "ThomasA", "tpoisot",
           "benoit-girard", "karthik", "oliviaguest", "labarba"]
reviewers = ["benoit-girard", "MehdiKhamassi", "vitay", "gdetor", "dmcglinn",
             "yoavram",  "FedericoV", "heplesser", "apdavison",
             "neuronalX", "piero-le-fou", "mstimberg", "rossant", "eroesch",
             "damiendr", "delsuc", "soolijoo", "benureau", "rth", "KamilSJaron",
             "TiinaManninen", "ChristophMetzner", "almarklein", "pietromarchesi",
             "anyaevostinar","ozancaglayan", "aaronshifman"]
replicators = ["gviejo", "gdetor", "MehdiKhamassi", "benoit-girard", "opetchey",
               "Vahidrostami", "jsta", "Fjanks", "ChristophMetzner", "vitay",
               "akdiem", "falex33", "aaronshifman", "RafaelNH"]


# Adding names that are not part of the board
board = {}
board["Guillaume Viejo"] = ["gviejo", "---"]
board["Frédéric Alexandre"] = ["falex33", "0000-0002-6113-1878"]
board["Rafael Neto Henriques"] = ["RafaelNH", "---"]
board["Frank Stollmeier"] = ["Fjanks", "0000-0003-4858-0895"]
# board["Alexandra K. Diem"] = ["akdiem", "0000-0003-1719-1942"]

authors = list(set(editors+reviewers+replicators))
fullnames = list(board.keys())
replicators = replicators + ["rougier"]

name_re = re.compile("""\* \[(?P<name>.+)\]\(https://github.com/(?P<handle>.+)\)""")
orcid_re= re.compile("""  ORCID: \[(?P<orcid>.+)\]""")
handle_re = re.compile("""""")

# names = []
with open("/Users/rougier/GitHub/ReScience/ReScience.github.io/04-board.md") as file:
    for line in file.readlines():
        match = name_re.match(line)
        if match:
            name  = match.group("name")
            handle = match.group("handle")
#            print(name, handle)
        match = orcid_re.match(line)
        if match:
            orcid = match.group("orcid")
            board[name] = [handle, orcid]
            if handle in authors:
                fullnames.append(name)

# Sort authors (but rougier and hinsen)
fullnames.sort(key=lambda s: s.split()[-1])
fullnames = ["Nicolas P. Rougier", "Konrad Hinsen"] + fullnames


txt_authors  = ""
tex_authors  = ""
tex_affiliations  = ""
indexed_affiliations = collections.OrderedDict()

counter = 0
for i,name in enumerate(fullnames):
    handle, orcid = board[name]
    affiliation = affiliations[handle]

    # Handle author with same affiliation
    if affiliation not in indexed_affiliations.values():
        counter += 1
        index = counter
        indexed_affiliations[index] = affiliation

        tex_affiliations += "\\affil[%d]{" % index
        tex_affiliations += affiliation
        tex_affiliations +="}\n"
    else:
        index = 1+list(indexed_affiliations.values()).index(affiliation)

    txt_authors += "%s; " % (name)
    tex_authors +=  "\\author[%d" % (index)
    if handle in editors or handle in chiefs:
        tex_authors +=  ",$\\dagger$"
    if handle in reviewers:
        tex_authors +=  ",$\\ddagger$"
    if handle in replicators:
        tex_authors +=  ",$\S$"
    if handle in ["rougier", "khinsen"]:
        tex_authors += ",$\star$"

#    tex_authors +=  "{" % (index)
    tex_authors += "]{%s}\n" % name
    
#    if orcid != "---":
#        tex_authors += "\href{http://orcid.org/%s}{\includegraphics[width=8pt]{orcid}}" % orcid
#    if i < len(fullnames)-1:
#        tex_authors += ",\n"
#    else:
#        tex_authors +="\\\\\n"
tex_affiliations += "\par"


with open("authors-overleaf.tex", "w") as file:
    file.write(tex_authors)

with open("affiliations-overleaf.tex", "w") as file:
    file.write(tex_affiliations)

with open("authors.txt", "w") as file:
    file.write(txt_authors)
