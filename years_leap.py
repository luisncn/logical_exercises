def years_leap(years):
    bisiesto = []
    
    if isinstance(years, int):
        if years % 4 == 0 and (years % 100 != 0 or years % 400 == 0):
            return f"{years} es un año bisiesto."
        else:
            return f"{years} no es un año bisiesto."
            
    elif isinstance(years, list):
        for year in years:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                bisiesto.append(year)
        return f"Años Bisiestos: {bisiesto}"

    else:
        return "Entrada no válida. Proporcione un año o una lista de años."


result_single = years_leap(2000)
result_list = years_leap([2000, 2012, 2008, 2009])
result_invalid = years_leap("2022")

print(result_single)
print(result_list)
print(result_invalid)
