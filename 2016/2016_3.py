#DENUMIRE^CUI^COD_INMATRICULARE^EUID^STARE_FIRMA^ADRESA
import csv
import time

#situatii_file = open('situatii1.txt')
#situatii_csv = csv.reader(situatii_file, delimiter=',')

def match_code(code_cui):
    with open('situatii_2016.txt') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            result = []
            if len(row) is 22:
                if (row[0] == code_cui):
                    try:
                        caen = row[1]
                    except IndexError:
                        caen = 'none'
                    try:
                        active_imobilizate = row[2]
                    except IndexError:
                        active_imobilizate = 'none'

                    try:
                        active_circulante = row[3]
                    except IndexError:
                        active_circulante = 'none'
                    try:        
                        stocuri = row[4]
                    except IndexError:
                        stocuri = 'none'                        

                    try:
                        creante = row[5]
                    except IndexError:
                        creante = 'none'

                    try:        
                        casa_conturi = row[6]
                    except IndexError:
                        casa_conturi = 'none'

                    cheltuieli_avans = row[7]
                    datorii = row[8]
                    venituri_avans = row[9]
                    provizioane = row[10]
                    capitaluri_total = row[11]
                    capital_subscris_varsat = row[12]
                    patrimoniu_regie = row[13]
                    cifra_afaceri_neta = row[14]
                    venituri_totale = row[15]
                    cheltuieli_totale = row[16]
                    profit_brut = row[17]
                    pierdere_bruta = row[18]                    
                    profit_net = row[19]
                    pierdere_neta = row[20]
                    nr_salariati = row[21]

                    result.append(caen)
                    result.append(active_imobilizate)
                    result.append(active_circulante)
                    result.append(stocuri)
                    result.append(creante)
                    result.append(casa_conturi)
                    result.append(cheltuieli_avans)
                    result.append(datorii)
                    result.append(venituri_avans)
                    result.append(provizioane)
                    result.append(capitaluri_total)
                    result.append(capital_subscris_varsat)
                    result.append(patrimoniu_regie)
                    result.append(cifra_afaceri_neta)
                    result.append(venituri_totale)
                    result.append(cheltuieli_totale)
                    result.append(profit_brut)
                    result.append(pierdere_bruta)
                    result.append(profit_net)
                    result.append(pierdere_neta)
                    result.append(nr_salariati)
                    return result

def match_code_1():
    with open('final2016_1.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            if len(row) is 6:
                result = []
                nume = row[0]
                code_cui = int(row[1])
                cod_matr = row[2]
                euid = row[3]
                stare_firma = row[4]
                adresa = row[5]
                find_result = match_code(code_cui)
                if find_result:
                    caen = find_result[1]
                    active_imobilizate = find_result[1]
                    active_circulante = find_result[2]
                    stocuri = find_result[3]
                    creante = find_result[4]
                    casa_conturi = find_result[5]
                    cheltuieli_avans = find_result[6]
                    datorii = find_result[7]
                    venituri_avans = find_result[7]
                    provizioane = find_result[9]
                    capitaluri_total = find_result[10]
                    capital_subscris_varsat = find_result[11]
                    patrimoniu_regie = find_result[12]
                    cifra_afaceri_neta = find_result[13]
                    venituri_totale = find_result[14]
                    cheltuieli_totale = find_result[15]
                    profit_brut = find_result[16]
                    pierdere_bruta = find_result[17]                    
                    profit_net = find_result[18]
                    pierdere_neta = find_result[19]
                    nr_salariati = find_result[20]
                    
                    result.append(nume)
                    result.append(code_cui)
                    result.append(cod_matr)
                    result.append(euid)
                    result.append(stare_firma)
                    result.append(adresa)

                    result.append(caen)
                    result.append(active_imobilizate)
                    result.append(active_circulante)
                    result.append(stocuri)
                    result.append(creante)
                    result.append(casa_conturi)
                    result.append(cheltuieli_avans)
                    result.append(datorii)
                    result.append(venituri_avans)
                    result.append(provizioane)
                    result.append(capitaluri_total)
                    result.append(capital_subscris_varsat)
                    result.append(patrimoniu_regie)
                    result.append(cifra_afaceri_neta)
                    result.append(venituri_totale)
                    result.append(cheltuieli_totale)
                    result.append(profit_brut)
                    result.append(pierdere_bruta)
                    result.append(profit_net)
                    result.append(pierdere_neta)
                    result.append(nr_salariati)
                    before_csv = time.time()
                    with open('2016.csv', 'a+', newline='') as myfile:
                        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                        wr.writerow(result)
                    myfile.close()
                    after_csv = time.time()

def match_code_2():
    with open('final2016_2.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:            
            if len(row) is 6:
                result = []
                nume = row[0]
                code_cui = int(row[1])
                cod_matr = row[2]
                euid = row[3]
                stare_firma = row[4]
                adresa = row[5]
                find_result = match_code(code_cui)
                if find_result:
                    caen = find_result[1]
                    active_imobilizate = find_result[1]
                    active_circulante = find_result[2]
                    stocuri = find_result[3]
                    creante = find_result[4]
                    casa_conturi = find_result[5]
                    cheltuieli_avans = find_result[6]
                    datorii = find_result[7]
                    venituri_avans = find_result[7]
                    provizioane = find_result[9]
                    capitaluri_total = find_result[10]
                    capital_subscris_varsat = find_result[11]
                    patrimoniu_regie = find_result[12]
                    cifra_afaceri_neta = find_result[13]
                    venituri_totale = find_result[14]
                    cheltuieli_totale = find_result[15]
                    profit_brut = find_result[16]
                    pierdere_bruta = find_result[17]                    
                    profit_net = find_result[18]
                    pierdere_neta = find_result[19]
                    nr_salariati = find_result[20]
                    
                    result.append(nume)
                    result.append(code_cui)
                    result.append(cod_matr)
                    result.append(euid)
                    result.append(stare_firma)
                    result.append(adresa)

                    result.append(caen)
                    result.append(active_imobilizate)
                    result.append(active_circulante)
                    result.append(stocuri)
                    result.append(creante)
                    result.append(casa_conturi)
                    result.append(cheltuieli_avans)
                    result.append(datorii)
                    result.append(venituri_avans)
                    result.append(provizioane)
                    result.append(capitaluri_total)
                    result.append(capital_subscris_varsat)
                    result.append(patrimoniu_regie)
                    result.append(cifra_afaceri_neta)
                    result.append(venituri_totale)
                    result.append(cheltuieli_totale)
                    result.append(profit_brut)
                    result.append(pierdere_bruta)
                    result.append(profit_net)
                    result.append(pierdere_neta)
                    result.append(nr_salariati)

                    with open('2016.csv', 'a+', newline='') as myfile:
                        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                        wr.writerow(result)
                    myfile.close()

def match_code_3():
    with open('final2016_3.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            if len(row) is 6:
                result = []
                nume = row[0]
                code_cui = int(row[1])
                cod_matr = row[2]
                euid = row[3]
                stare_firma = row[4]
                adresa = row[5]
                find_result = match_code(code_cui)
                if find_result:
                    caen = find_result[1]
                    active_imobilizate = find_result[1]
                    active_circulante = find_result[2]
                    stocuri = find_result[3]
                    creante = find_result[4]
                    casa_conturi = find_result[5]
                    cheltuieli_avans = find_result[6]
                    datorii = find_result[7]
                    venituri_avans = find_result[7]
                    provizioane = find_result[9]
                    capitaluri_total = find_result[10]
                    capital_subscris_varsat = find_result[11]
                    patrimoniu_regie = find_result[12]
                    cifra_afaceri_neta = find_result[13]
                    venituri_totale = find_result[14]
                    cheltuieli_totale = find_result[15]
                    profit_brut = find_result[16]
                    pierdere_bruta = find_result[17]                    
                    profit_net = find_result[18]
                    pierdere_neta = find_result[19]
                    nr_salariati = find_result[20]
                    
                    result.append(nume)
                    result.append(code_cui)
                    result.append(cod_matr)
                    result.append(euid)
                    result.append(stare_firma)
                    result.append(adresa)

                    result.append(caen)
                    result.append(active_imobilizate)
                    result.append(active_circulante)
                    result.append(stocuri)
                    result.append(creante)
                    result.append(casa_conturi)
                    result.append(cheltuieli_avans)
                    result.append(datorii)
                    result.append(venituri_avans)
                    result.append(provizioane)
                    result.append(capitaluri_total)
                    result.append(capital_subscris_varsat)
                    result.append(patrimoniu_regie)
                    result.append(cifra_afaceri_neta)
                    result.append(venituri_totale)
                    result.append(cheltuieli_totale)
                    result.append(profit_brut)
                    result.append(pierdere_bruta)
                    result.append(profit_net)
                    result.append(pierdere_neta)
                    result.append(nr_salariati)

                    with open('2016.csv', 'a+', newline='') as myfile:
                        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                        wr.writerow(result)
                    myfile.close()

def match_code_4():
    with open('final2016_4.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            if len(row) is 6:
                result = []
                nume = row[0]
                code_cui = int(row[1])
                cod_matr = row[2]
                euid = row[3]
                stare_firma = row[4]
                adresa = row[5]
                find_result = match_code(code_cui)
                if find_result:
                    caen = find_result[0]
                    active_imobilizate = find_result[1]
                    active_circulante = find_result[2]
                    stocuri = find_result[3]
                    creante = find_result[4]
                    casa_conturi = find_result[5]
                    cheltuieli_avans = find_result[6]
                    datorii = find_result[7]
                    venituri_avans = find_result[8]
                    provizioane = find_result[9]
                    capitaluri_total = find_result[10]
                    capital_subscris_varsat = find_result[11]
                    patrimoniu_regie = find_result[12]
                    cifra_afaceri_neta = find_result[13]
                    venituri_totale = find_result[14]
                    cheltuieli_totale = find_result[15]
                    profit_brut = find_result[16]
                    pierdere_bruta = find_result[17]                    
                    profit_net = find_result[18]
                    pierdere_neta = find_result[19]
                    nr_salariati = find_result[20]
                    
                    result.append(nume)
                    result.append(code_cui)
                    result.append(cod_matr)
                    result.append(euid)
                    result.append(stare_firma)
                    result.append(adresa)

                    result.append(caen)
                    result.append(active_imobilizate)
                    result.append(active_circulante)
                    result.append(stocuri)
                    result.append(creante)
                    result.append(casa_conturi)
                    result.append(cheltuieli_avans)
                    result.append(datorii)
                    result.append(venituri_avans)
                    result.append(provizioane)
                    result.append(capitaluri_total)
                    result.append(capital_subscris_varsat)
                    result.append(patrimoniu_regie)
                    result.append(cifra_afaceri_neta)
                    result.append(venituri_totale)
                    result.append(cheltuieli_totale)
                    result.append(profit_brut)
                    result.append(pierdere_bruta)
                    result.append(profit_net)
                    result.append(pierdere_neta)
                    result.append(nr_salariati)

                    with open('2016.csv', 'a+', newline='') as myfile:
                        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                        wr.writerow(result)
                    myfile.close()

if __name__ == "__main__":
    print("Start file 3")
    match_code_3()
    print("End file 3")
   