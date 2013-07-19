import MySQLdb

def uploadToDatabase(stories, user1, passwd1):
    loginInfo = open('login','r').read().split('\n')
    for i in range(len(loginInfo)):
        start = loginInfo[i].find('=')+1
        loginInfo[i] = loginInfo[i][start:]
    
	print(loginInfo)
	print('Attempting to connect to database...')
	#conn  =  MySQLdb.connect(host=loginInfo[0], user=loginInfo[1],passwd=loginInfo[2],db=loginInfo[3])
	conn = MySQLdb.connect('mysql.casey-orourke.com','caseyorourkecom','','casey_orourke_news')
	print('Database connection successful!')
    
	
    sqlString ='TRUNCATE TABLE news;'
    for i in range(-1,24):
        source = 'NYT'
        summary = stories[i]['summary']
        headline  = stories[i]['title']
        link = stories[i]['link']
        date  = stories[i]['date']
        
        
        query = "INSERT INTO news (source,headline,summary,link,date) VALUES ("
        query = query + "'" + source + "','" + headline + "','" + summary + "','" + link + "','" + date + "');"
        sqlString+= query

        #print query + "\n\n"

	
    sqlString = sqlString.encode('utf-8')
    #print sqlString
    
    x = conn.cursor()
    x.execute(sqlString)
