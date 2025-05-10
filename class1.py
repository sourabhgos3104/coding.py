questions= []
questions.append("Q1:python was devloped in")
questions.append("Q2:c++ was devloped in")
questions.insert(2,"Q3:html was devloped in")
questions.insert(3,"Q4:when one is not a valid keyword in python")
questions.append("Q5:full form of css")
questions.append("Q5:full form of css")
questions.pop()


options=[

("A:1990","B:1991","C:1999","D:2000" ),
("A:1991","B:1992","C:1998","D:2001" ),
("A:1992","B:1994","C:1998","D:2003" ),
("A:1998","B:1993","C:1996","D:2004" ),
("A:CASCADING STYLE SHEET","B:CASCADING SHEET","C:CASCADING CARD","D:CASCARDING STYLE SHEET" )

]

answers =["B","C","A","A","A"]


ans=[]
points=0

print(questions[0])
print(options[0])
ans.append(input("select the correct option:").upper())
points=points+1 if ans[0] == answers[0] else points


print(questions[1])
print(options[1])
ans.append(input("select the correct option:").upper())
points=points+1 if ans[1] == answers[1] else points


print(questions[2])
print(options[2])
ans.append(input("select the correct option:").upper())
points=points+1 if ans[2] == answers[2] else points


print(questions[3])
print(options[3])
ans.append(input("select the correct option:").upper())
points=points+1 if ans[3] == answers[3] else points




print(questions[4])
print(options[4])
ans.append(input("select the correct option:").upper())
points=points+1 if ans[4] == answers[4] else points


print()
print(f" total points are: {points}")
print(f" your selected options are: {ans}")
print(f" the correct answers are: {answers}")
