def email_list(domains):
	emails = []
	for users in domains:
	  for user in domains[users]:
	    emails.append(user+"@"+users)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))