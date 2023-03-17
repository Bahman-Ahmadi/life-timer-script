from jdatetime import datetime as DT
from rich import print

havingJob = (DT(1404,5,15) - DT.now()).days
havingHome = (DT(1406,7,1) - DT.now()).days

university = (DT(1404,7,1) - DT.now()).days
globalTest = (DT(1404,4,20) - DT.now()).days # konkoor
currentStudyingYearsEnd = (DT(DT.now().year+1 if DT.now().month >= 7 else DT.now().year,3,30) - DT.now()).days
getUniversityCredit = (DT(1406,7,1) - DT.now()).days # lisans
startTermTests = (DT(DT.now().year if 7 <= DT.now().month < 10 else DT.now().year+1, 10 if 7 <= DT.now().month < 10 else 3, 1) - DT.now()).days
getSchoolCredit = (DT(1404,3,30) - DT.now()).days

endingWeek = 7 - DT.now().weekday()
monthEnd = (29 if DT.now().month == 12 else 31 if DT.now().month <= 6 else 30)
endingMonth = monthEnd - DT.now().day
endingYear = (12 - DT.now().month) * monthEnd + endingMonth
endingDay = 24 - DT.now().hour

birthday = (DT(DT.now().year if DT.now().month < 10 or (DT.now().month == 10 and DT.now().day < 18) else DT.now().year+1,10,18) - DT.now()).days

print("[b][red]🧬 Life Map... 🗺️[/red][/b]\n\n")
print(

"[b][green]    • Calendar Events[/green][/b]\n",
"        ⛅ [b]ending today :[/b]", endingDay, " hours\n",
"        🔢  [b]ending week :[/b]", endingWeek, " days\n",
"        📆  [b]ending month :[/b]", endingMonth, " days\n",
"        🎆  [b]ending year :[/b]", endingYear, " days\n",
"        🎂  [b]birthday :[/b]", birthday, " days\n\n"

"[b][green]    • School Events[/green][/b]\n",
"         🔘  [b]starting term tests :[/b]", startTermTests, " days\n",
"         🔚  [b]ending school year :[/b]", currentStudyingYearsEnd, " days\n",
"         🎓  [b]get school credit :[/b]", getSchoolCredit, " days\n",
"         📝  [b]country test :     [/b]", globalTest, " days\n",
"         👨‍🎓 [b]going university :[/b]", university, " days\n",
"         🎓  [b]get univ. credit : [/b]", getUniversityCredit, " days\n\n"

"[b][green]    • Money Events[/green][/b]\n",
"          🛄 [b]Hiring for job :[/b]", havingJob, " days\n",
"          🏠 [b]Buying a Home :[/b]", havingHome, " days"
)
