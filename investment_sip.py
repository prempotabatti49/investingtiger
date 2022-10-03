# SIP calculator
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def get_total_invested(monthly_sip_: int, yearly_raise_: float, total_years: int):
    total_invested_ = monthly_sip_
    for month_ in range(1, 12 * total_years):
        if month_ % 12 == 0:
            monthly_sip_ = monthly_sip_ * (1.0 + yearly_raise_/100)
        total_invested_ = total_invested_ + monthly_sip_
    return total_invested_
 

def calculate_sip_returns(
    start_sip: int=30000, 
    total_years: int=30, 
    roi_list: list=[10, 12, 20, 25], 
    yearly_raise_list: list=[0, 10]
    ) -> np.array:

    # Initialization
    year = [i + 1 for i in range(total_years)]
    monthly_sip = start_sip
    total_fund = monthly_sip
    money_invested = monthly_sip
    total_fund_at_each_year = {}
    total_fund_combination = {}
    yearly_sip_amount = {}

    # Calculation
    for roi in roi_list:
        print(f"{roi}%")
        for yearly_raise in yearly_raise_list:
            total_fund = start_sip
            monthly_sip = start_sip
            money_invested = start_sip

            total_invested = get_total_invested(start_sip, yearly_raise, total_years)
            condition_key = f"roi_{roi}%__yearly_raise_{yearly_raise}%__total_invested_Rs.{round(total_invested):,}"

            #Total fund at the end of each year for the condition_key
            total_fund_at_each_year[condition_key] = []
            #Total fund at the end of entire tenure for this condition_key
            total_fund_combination[condition_key] = []
            #Yearly SIP amount, changes in case there is yearly increment
            yearly_sip_amount[condition_key] = []

            for month in range(1, total_years * 12):
                if month % 12 == 0:
                    monthly_sip = monthly_sip * (1.0 + yearly_raise/100)
                    total_fund_at_each_year[condition_key].append(total_fund)
                    yearly_sip_amount[condition_key].append(monthly_sip)
                total_fund = total_fund * (1.0 + (roi/100) / 12) + monthly_sip
                money_invested = money_invested + monthly_sip

            total_fund_at_each_year[condition_key].append(total_fund)
            total_fund_combination[condition_key].append(total_fund)
            yearly_sip_amount[condition_key].append(monthly_sip)

            print(f"----ROI: {roi}% AND Yearly_Raise: {yearly_raise}%----")
            print(f"total value of investment after {total_years} years at {roi}% CAGR would be {round(total_fund)}")
            print(f"Total money invested: Rs. {round(money_invested)}, with last monthly SIP = {monthly_sip}")
            print("------------------------------------------")
    return pd.DataFrame(total_fund_at_each_year).round()


# for combination in pd.DataFrame(total_fund_at_each_year).columns:
#     plt.plot(year, total_fund_at_each_year[combination])
# plt.title(f"Start SIP: Rs.{start_sip}")
# plt.xlabel("Years completed")
# plt.ylabel("Total fund value")
# plt.legend(pd.DataFrame(total_fund_at_each_year).columns.tolist())
# plt.show()
