import random
import math
print("T20 Match Predictor")

tier1=["IND","SA","WI","AUS","ENG","NZ","PAK","RR","RCB","PBKS","SRH"]
tier2=["CSK","GT","KKR","BAN","AFG","SL","ZIM","USA","IRE"]
tier3=["MI","LSG","DC","SCO","NEP","NED","NAM","CAN","OMA","UAE"]    

print("Innings")
ins=int(input())
if ins==1 or ins==2:
    
  
    
    team1=input("Batting Team (in short) ").upper()
    team2=input("Bowling Team (in short)").upper()
    
  
    runs=int(input("Runs "))
    wics=int(input("Wickets "))
    ovr=float(input("Overs (format Ovs.balls)"))
    ovr1=math.floor(ovr)
    balls=round((ovr-ovr1)*10)
    ovs=ovr1+(balls/6)
    if wics!=0:
     fow=int(input("Score at latest fall of wicket : "))
     part=runs-fow
    else:
       part=runs
    
    ovsrem=20-ovs
    wicsrem=10-wics
    
    if ovs!=0:
     runrate=runs/ovs
    else:
       runrate=0
else:
    print("Input Invalid ")
cap=round(80+((ovs/20)*18),1)
if ins==1:
  if ovsrem!=0:
    hist=int(input("Average team Score  in this ground ")) 
    if team1 in tier1 and team2 in tier3:  
      cf=0.42       
      #cf means chasing factor , based on past observations
    elif team1 in tier1 and team2 in tier2:
      cf=0.46
    elif team1 in tier1 and team2 in tier1:
      cf=0.50
    elif team1 in tier2 and team2 in tier1:
      cf=0.54
    elif team1 in tier2 and team2 in tier2:
      cf=0.50
    elif team1 in tier2 and team2 in tier3:
      cf=0.46
    elif team1 in tier3 and team2 in tier1:
     cf=0.58
    elif team1 in tier3 and team2 in tier2:
     cf=0.54
    elif team1 in tier3 and team2 in tier3:
     cf=0.50
    #Base case of 0.5 for equal tiers and +-0.04 for difference in each tier
    #pro1,2,3,4 means projected score after end of 20 overs based on different math logic
    pro1=round((runrate)*20) #projected total score if innings goes at current runrate
    if wics!=0:
      avg=runs/wics #runs scored per wicket 
    else:
      avg=runs 
    pro2=0
    pro4=0
    if (avg*10)<pro1:  #if runs are less compared to wicket fall and team can get all out before 20 overs
      pro2= round(avg*10)  #counting runs per remaining wickets
      if wicsrem==1:
        pro2=runs+5 #last batter scores less 
    
    pro3=0 #initialized value
    
    if ovs>=3:
     rnew=int(input("Runs scored in last 3 overs "))
     wnew=int(input("Wickets lost in last 3 overs "))
     ratenew=rnew/3
    else:
      ratenew=runrate
      rnew=runs
      wnew=wics 
    pro3=round(runs+((ratenew)*ovsrem))
   

    if wnew>=2 and ovs>=5:
      m=0.27  #derived from graphical analysis
      x=wnew/(wicsrem+1)
      pro4=runs+((ratenew*ovsrem)*(1-(m*x)))  #if wickets lost then runs will slow similar to the graph of capacitor charging q=q0(1-e^-t)
    elif wnew==1 and ovs>=5:
      m=0.23
      x=wnew/(wicsrem+1)
      pro4=runs+((ratenew*ovsrem)*(1-(m*x)))
 
    if pro2==0 and pro4==0:
     if(ovs>=10):
      promax=round(0.3*pro1+0.7*pro3)  #weightage assigned from observation results across matches
     elif(ovs<10 and ovs>5):
       promax=round(0.4*pro1+0.6*pro3)
     else:
       promax=round(0.5*pro1+0.5*pro3)
       
    elif pro4==0:
      promax=round(0.2*pro1+0.5*pro2+0.3*pro3)
    elif pro2==0:
      promax=round(0.2*pro1+0.3*pro3+0.5*pro4)
   

    
    
   
  print("Projected Score at the end of the first innings ",promax)
  
  
  if(promax>hist):
      win1=round(min( 50+((promax-hist)/cf),cap),1)  #winning probability of current batting team
      

      #minimum defending probability and cap , rounded off upto 1 decimal
      win2=round(100-win1,1)

  else:
      win1=round(max(50+((promax-hist)/cf),100-cap),1)
      #if batting total is low team2 has higher chances of winning
      win2=round(100-win1,1)
  print(team1)
  print(win1)
  print(team2)
  print(win2)
if ins==2: 
  target=int(input("Target "))
  hist=int(input("Average score batting second in this ground "))
  if team2 in tier1 and team1 in tier3:  
      cf=0.42       
      #cf means chasing factor , based on past observations
  elif team2 in tier1 and team1 in tier2:
      cf=0.46
  elif team2 in tier1 and team1 in tier1:
      cf=0.50
  elif team2 in tier2 and team1 in tier1:
      cf=0.54
  elif team2 in tier2 and team1 in tier2:
      cf=0.50
  elif team2 in tier2 and team1 in tier3:
      cf=0.46
  elif team2 in tier3 and team1 in tier1:
     cf=0.58
  elif team2 in tier3 and team1 in tier2:
     cf=0.54
  elif team1 in tier3 and team2 in tier3:
     cf=0.50
    #Base case of 0.5 for equal tiers and +-0.04 for difference in each tier
  reqruns=target-runs
  if ovsrem!=0:
   reqrate=reqruns/ovsrem
  
   gap=reqrate-runrate
   pro1=round((runrate)*20)
   if wics!=0:
      avg=runs/wics #runs scored per wicket 
   else:
      avg=runs 
   pro2=0
   pro4=0
   if runs+(avg*wicsrem)<pro1: 
      pro2= round(runs+(avg*wicsrem))  
      if wicsrem==1:
        pro2=runs+5 
    
   if ovs>=3:
     rnew=int(input("Runs scored in last 3 overs "))
     wnew=int(input("Wickets lost in last 3 overs "))
     ratenew=rnew/3
   else:
    ratenew=runrate
    rnew=runs
    wnew=wics
      
   pro3=round(runs+(ratenew*ovsrem))

   if wnew>=2 and ovs>=5:
      m=0.27  
      x=wnew/(wicsrem+1)
      pro4=runs+((ratenew*ovsrem)*(1-(m*x))) 
   elif wnew==1 and ovs>=5:
      m=0.23
      x=wnew/(wicsrem+1)
      pro4=runs+((ratenew*ovsrem)*(1-(m*x)))
 
   if pro2==0 and pro4==0:
     if(ovs>=10):
      promax=round(0.3*pro1+0.7*pro3) 
     elif(ovs<10 and ovs>5):
       promax=round(0.4*pro1+0.6*pro3)
     else:
       promax=round(0.5*pro1+0.5*pro3)
       
   elif pro4==0:
      promax=round(0.2*pro1+0.4*pro2+0.4*pro3)
   elif pro2==0:
      promax=round(0.2*pro1+0.3*pro3+0.5*pro4)
   elif pro3==0:
      promax=pro1
   
   print("Projected Score at the end of the second innings ",promax)

   closing_factor=0 #initialized 
   if part>=50 or ratenew>=reqrate:
   #part means partnership and ratenew means run rate in last 3 overs
    closing_factor=round((reqrate-ratenew)*ovsrem)
   elif part>=50 or ratenew>=runrate:
    temp=pro1+round((ratenew-runrate)*ovsrem)
    closing_factor=target-temp

   diff1=target-promax  
   diff2=closing_factor
   print("Projected difference in runs ",diff1)
   print("Difference based on current momentum ",diff2)

   # Present scenario probability instead of projection if less balls are left
   
   if ovsrem<=1:
     

 
     #Monte-Carlo Simulation
     Balls=int(input("Balls remaining "))

     r= target-runs   # runs required
     trials=10000
     success=0

     for _ in range(trials):
      total_runs = 0
      for _ in range(Balls):
        # Possible outcomes per ball
        wickets = wicsrem  # wickets remaining at start
        for _ in range(Balls):
            if wickets == 0:
                break  # innings over

            # Possible outcomes per ball (runs + wicket)
            if wickets >= 5:
                outcome = random.choices(
                    [0, 1, 2, 4, 6, "W"],
                    [0.15, 0.15, 0.20, 0.20, 0.20, 0.10]  # wicket prob = 0.10
                )[0]
            elif wickets >= 3:
                outcome = random.choices(
                    [0, 1, 2, 4, 6, "W"],
                    [0.25, 0.20, 0.20, 0.10, 0.05, 0.20]  # wicket prob = 0.20
                )[0]
            else:  # last wicket
              outcome = random.choices(
                    [0, 1, 2, 4, 6, "W"],
                    [0.25, 0.10, 0.05, 0.05, 0.05, 0.50]  # wicket prob = 0.50
                )[0]
        if outcome == "W":
                wickets -= 1
        else:
                total_runs += outcome
      if total_runs >= r:
       success += 1

     win1 = round(min((success / trials)*100,95),1) #current batting team
     win2=round(100-win2,1)

   else:
     if(ovsrem<=10):
       p_factor=max(ovsrem/20,0.05) #pressure is higher as overs remaining are less 
       cfx=cf*(0.5+p_factor)  #chase factor changes with overs reducing
     else:
       cfx=cf
     avgdiff=(diff1+diff2)/2
      #capping for one sided scenarios
     if avgdiff>0 and reqrate>30:
        win2=99.5
        win1=0.5
     elif (target-runs)<30 and reqrate<4 and wicsrem>=4:
        win1=99.5
        win2=0.5
     elif (target-runs)>30 and wicsrem<=2:
        win2=97.5
        win1=2.5
      #normal scenarios
     if avgdiff>0:
       #batting team is expected to stay behind the target
       
       win2=round(min(50+(avgdiff/cfx),95),1)  #current bowling team
       win1=round(100-win2,1) #batting team
     else:
       win2=round(max(50+(avgdiff/cfx),5),1) #since avgdiff is negative bowling team expected to lose
       win1=round(100-win2,1)
   print("Winning Probability ")
   print(team1)
   print(win1)
   print(team2)
   print(win2)
  else:
    print("Match Completed") 
     
    
