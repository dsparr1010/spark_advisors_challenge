


THOUGHT PROCESS
- Read PDF and make sure I understand the problem and what is being asked of me.
    - ATFQ
    - Look at provided materials to create mental mapping of work to be done
- Manually find a all applicable plans with given state and rate area code
    - This is to test one so that I know my code is working as expected
    - Helps in extracting patterns


FLOW EXAMPLE:

64148 -> 
    zips.csv -> use zip to find state, rate area
        - if QS>1, return blank (use 65556 for this test case)
        - else: continue
    use state & rate area to find Silver plan
        - if QS>1, grab all rates in "rate" column, find the second lowest
        - elif QS == 0 || QS == 1: return blank
            - plan not found or there is only 1 plan found (so cannot find second lowest)

zip code ingested: 64148
zip code found in zips.csv: 64148,MO,29095,Jackson,3
 - From there we gather the state and rate_area

Take that info to look for *second lowest silver plan* in plans.csv. Found instances:
 - 78421VV7272023,MO,Silver,290.05,3
 - 35866RG6997149,MO,Silver,234.6,3
 - 28850TB6621800,MO,Silver,265.82,3
 - 53546TY7687603,MO,Silver,251.08,3
 - 26631YR3384683,MO,Silver,351.6,3
 - 03665WJ8941702,MO,Silver,312.06,3
 - 02345TB1383341,MO,Silver,245.2,3 **
 - 40205HK1927400,MO,Silver,265.25,3
 - 57237RP9645446,MO,Silver,253.65,3
 - 64618UJ3132146,MO,Silver,319.57,3
 - 43868JA2737085,MO,Silver,271.64,3
 - 44945VH6426537,MO,Silver,298.87,3
 - 39063JC7040427,MO,Silver,341.24,3


PLAN OF ACTION:

1. Before slcsp.csv is even opened, we can open plans.csv -> filter out all plans that are not silver.
    - More performant, less unrelated data to sift through, less complexity, highly tuned to problem's need.

2. 





Notes:
 - Because 65556 contains multiple found instances for MO in zips.csv, this is too ambiguous and should be left blank. EX:
    - 65556,MO,29029,Camden,5
    - 65556,MO,29105,Laclede,8
    - 65556,MO,29169,Pulaski,9

- Ingest plans.csv first.
- Ingest zips.csv, go row by row to query for plans by state and rate area. EX:
    - Row shows 36749,AL,01001,Autauga,11
    - Plans.objects.filter(state="AL", rate_area=11, metal_level="Silver")
    - Cannot related zip with plan because there are different levels for a state/rate area combo. Example:
        99471AK3918170,MO,Gold,298.24,3
        72591EC9187565,MO,Gold,277.65,3
        74585TY2651921,MO,Gold,422.32,3
        80249XE7892892,MO,Gold,358.96,3

    - Returned Plan instance:
        ManyToMany FK field on 