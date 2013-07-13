def getNYTHeadLines():
    stories = {}
    print "Getting latest stories..."
    for i in range(len(nytimesFeed.entries)):
        date = nytimesFeed['entries'][i].published
        link = nytimesFeed['entries'][i].link
        title = nytimesFeed.entries[i].title
        title = title.replace("'","")
        summary_detail = nytimesFeed.entries[i].summary_detail.value
        summary = summary_detail[:summary_detail.find('<img')]
        summary = list(summary)
        for j in range(len(summary)):
            if summary[j] == "'":
                summary[j] = ""
        summary = "".join(summary)
        #print summary + '\n\n'
        #print str(i) + ': ' + nytimesFeed.entries[i].title + ','
        stories[i-1] = {'title' : title, 'summary' : summary, 'link' : link, 'date': date}

    return stories
