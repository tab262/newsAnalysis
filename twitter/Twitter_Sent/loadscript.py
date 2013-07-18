import json

def dataLoad(fileObj):
    results = json.load(tweet_file) 
    for i in range(100):
        if 'user' in results[i]:
            print results[i]['user']['location']
  
    
    
def processData(fileName):
    newContent = file(fileName, "r").read().replace("\r", "").replace("\n", ", ")
    #print type(newContent)
    newContent = newContent[:len(newContent)-2] #cuts of tailend comma that throws json formatter
    open(('p_'+fileName), "w").write(newContent)
    
    
fileName = "output.json"
processData(fileName)
tweet_file = open('p_'+fileName)    
dataLoad(tweet_file)





