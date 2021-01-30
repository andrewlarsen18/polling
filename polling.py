#polling 1,000 friends for their votes and primary issues

#creating a dictionary where users responses are stored together 
#subject1 = {'vote' : "trump" , "sex" : "male" , "KeyIssue" : "Economy"}

all_respondents = []
respondent_data = {'2020 Vote' : '' , "Sex" : '' , "KeyIssue" : '' , "Age" : }   
	
	while len(all_respondents) <= 1000:
		for respondent in all_respondents
		RSVP = input("Would like you to be asked a few questions about your political positions?")
    	if RSVP == "yes" or RSVP == "Yes" or RSVP == "YES":
      		general_election = input("Who did you vote for in the 2020 Election: ")
        	respondent_data['2020 Vote'] = general_election
        	SexQuestion = input("What gender are you: ")
        	respondent_data["Sex"] = SexQuestion
        	concern = input("Out of these issues, which was your biggest concern when selecting a candidate in 2020 (Economy, COVID-19, Candidate's Character, Immigration, Foreign Policy) ")
        	respondent_data["KeyIssue"] = concern
        	AgeQuestion = input("What is your age? ")
        	respondent_data["Age"] = AgeQuestion
        	print ("Thank you! Your answers have been recorded.")
        	all_respondents = len(x+1)
    	else:
        	continue


