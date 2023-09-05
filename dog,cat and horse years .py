'''
Part 1 ; 

Task No:  a and b

'''

human_age = float(input())    # suppose it's 4.56 years

dog_age = human_age * 7       # 31.91999

dog_years_actual = dog_age //1       # 31

remaining_years = dog_age - dog_years_actual   # 0.91999

dog_months_total = remaining_years * 12    #11.03999

dog_months_actual = dog_months_total // 1    #11

remaining_days = dog_months_total - dog_months_actual #0.399

dog_days_total = remaining_days * 30 #1.19

dog_days_actual = dog_days_total // 1               #1.0


'''

Till this point was dog related research

'''



'''

Part 2;

Task 1 and 2 

'''

cat_age = human_age / 9   # suppose cat age is 1.88 when human is 17

cat_years_actual = cat_age // 1  # cat year is 1 year

cat_remaining_years = cat_age - cat_years_actual # 0.88 years

cat_months_total = cat_remaining_years * 12     #10.6666

cat_months_actual = cat_months_total // 1      #10

cat_remaining_months = cat_months_total - cat_months_actual   # 0.666

cat_days_total = cat_remaining_months * 30   #19.99999

cat_days_actual = cat_days_total // 1 #19 



'''

Till this point it was research about cats 

'''




'''


Part 3;
Task 1 and 2 

'''


horse_age = ((((((human_age)**2)-47) / 7 )+12)*3)  # Suppose horse age is 77.57 when human age is 12

horse_years_actual = horse_age // 1     # 77

horse_remainin_years = horse_age - horse_years_actual   #0.5714

horse_months_total = horse_remainin_years * 12   #6.857

horse_months_actual = horse_months_total // 1    #6

horse_remaining_months = horse_months_total - horse_months_actual   #0.857

horse_days_total = horse_remaining_months * 30  #25.714

horse_days_actual = horse_days_total // 1     # 25



'''

finally the research about the aliens are over

'''



print('Enter your age:', human_age)

print('Your age in dog years is', f'{dog_years_actual:.1f}','years',f'{dog_months_actual:.1f}','months',f'{dog_days_actual:.1f}','days')

print('Your age in cat years is', f'{cat_years_actual:.1f}','years',f'{cat_months_actual:.1f}','months',f'{cat_days_actual:.1f}','days')

print('Your age in horse years is', f'{horse_years_actual:.1f}','years',f'{horse_months_actual:.1f}','months',f'{horse_days_actual:.1f}','days')




