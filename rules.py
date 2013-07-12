rules = {   'S'  :{'NP VP' : 1.0},
            'VP' :{'V NP' : 0.1, 'VP PP' : 0.9},
            'NP' :{'N' : .6, 'NP PP' : .4},
            'PP' :{'P NP' : 1.0},
            'N'  :{'Ted' : .25, 'Jill': .15, 'town' : .6},
            'V'  :{'saw' : 1.0},
            'P'  :{'in'  : 1.0}
        }
        
def printRules():        
    for key in rules.keys():
        innerDict = rules[key]
        for key2 in innerDict.keys():
            print(key + '=>' + key2 + ' : ' + str(innerDict[key2]))
        
def lookUpRule(label, overall):
    if label in rules.keys():
        toAdd = list(rules[label].keys())
        newList = []
        
        #getting new labels
        for item in toAdd:
            tList = item.split()
            for item2 in tList:
                if item2 in rules.keys():
                    newList.append(item2)
                else:
                    #adding to sentence as we have a word that is not a label
                    overall[1].append(item)
       
        
        for item4 in newList:
            overall[0].append(item4)
        del overall[0][0]
       
        print(overall[0])


labels = rules.keys()
stack = ['S']
sentence = []
overall = [stack, sentence]
i = 0
while i < 2: 
    lookUpRule(overall[0][0], overall)            
    i += 1
