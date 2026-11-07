"""ILLUSTRATIVE assumptions only. No financial inputs are estimated from Findex."""
from pathlib import Path
import json,csv,math
O=Path('Group_31/revised'); O.mkdir(parents=True,exist_ok=True)
projection=[]
for scenario,price,ends in [('Conservative',.4,[4,10,18]),('Base',.5,[8,20,40]),('Optimistic',.6,[12,32,65])]:
    start=0
    for year,end in enumerate(ends,1):
        avg=(start+end)/2; new=end-start; fixed=36*1.2**(year-1); variable=avg*12*.1; acquisition=new*2
        rev=avg*12*price; cost=fixed+variable+acquisition
        projection.append(dict(scenario=scenario,year=year,price_monthly_lakh=price,start_institutions=start,end_institutions=end,average_institutions=avg,new_institutions=new,revenue_lakh=round(rev,2),fixed_cost_lakh=round(fixed,2),variable_cost_lakh=round(variable,2),acquisition_cost_lakh=round(acquisition,2),total_cost_lakh=round(cost,2),surplus_lakh=round(rev-cost,2)))
        start=end
sensitivity=[]
for variable in [.08,.10,.15]:
    for price in [.4,.5,.6]:
        sensitivity.append(dict(price_lakh=price,variable_cost_lakh=variable,breakeven_institutions=math.ceil(3/(price-variable)),monthly_surplus_at_10_lakh=round(10*(price-variable)-3,2)))
funding={'Year 1 base operating deficit':32.8,'Prelaunch product and integration':10.,'Prelaunch pilot and evaluation':5.,'Working capital reserve':12.,'Contingency and runway reserve':15.2}
assert sum(funding.values())==75
out={'notice':'ILLUSTRATIVE ASSUMPTIONS TO BE VALIDATED; NOT SURVEY FINDINGS OR FORECASTS','unit':'INR lakh; 1 lakh = INR 100,000','projection':projection,'sensitivity':sensitivity,'seed_uses_lakh':funding,'seed_total_lakh':sum(funding.values()),'base_contribution_monthly_lakh':.4,'base_contribution_margin_percent':80,'base_CAC_lakh':2,'base_CAC_payback_months':5,'base_steady_state_breakeven_institutions':8,'base_breakeven_with_one_new_customer_per_month':13}
(O/'financial_model.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
for name,rows in [('financial_projection.csv',projection),('financial_sensitivity.csv',sensitivity)]:
    with (O/name).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
print('Illustrative financial model verified: 9 projection rows, 9 sensitivity cells, seed total INR 75 lakh.')
