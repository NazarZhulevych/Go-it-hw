import re

def normalize_phone(raw_numbers):
      
    new_numbers = ()
    
    pattern = r'[\s\\()\D\\-]+'  
    cleaned_number = re.sub(pattern, "", raw_numbers)  #remove symbols and letters

    if not cleaned_number.startswith("38"): #check if started with "38", if not add
        cleaned_number = "38" + cleaned_number  

    return "+" + cleaned_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#Нормалізовані номери телефонів для SMS-розсилки: ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']



