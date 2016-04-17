import os
import json
import re
from email.parser import HeaderParser


def extract_data(rootdir='/home/pablo/Documents/otros/got-your-back-0.30/GYB-GMail-Backup-pablo.fernandez@bigdeal.com.ar/2015'):
    with open('data.txt', 'a') as dest_file:
        for root, subdirs, files in os.walk(rootdir):
            for f in files:
                if not f.endswith('.eml'):
                    continue
                date_string = root.split('/')
                mydate = date_string[-1] + '/' + date_string[-2] + '/' + date_string[-3]
                file_path = root + '/' + f
                my_dictionary = extract_email_data(file_path, {'date': mydate,})
                json.dump(my_dictionary, dest_file)
                dest_file.write('\n')


def extract_email_data(file_path, my_dictionary):
    print file_path
    myfile = open(file_path)
    msg = myfile.read()
    myfile.close()
    parser = HeaderParser()
    h = parser.parsestr(msg)
    if h.get('To'):
        my_dictionary['to'] = clean_emails_list(h.get('To'))   
    else:
        my_dictionary['to'] = 'pablo.fernandez@bigdeal.com.ar'
    my_dictionary['from'] = clean_emails_list(h.get('From'))
    if 'pablo.fernandez@bigdeal.com.ar' in h.get('From'):
        my_dictionary['sent'] = 'True'
    else:
        my_dictionary['sent'] = 'False'
    return my_dictionary


def clean_emails_list(email_list):
    split_list = email_list.split(',')
    ans = []
    for _email in split_list:
        aux = clean_email(_email)
        if aux:
            ans.append(aux)
    return ans


def clean_email(_email):
    match = re.search(r'[+\w\.-]+@[\w\.-]+', _email)
    if match:
        return match.group(0)
    else:
        return None



def replace_names(source_file='data.txt', destination_file='final_data.txt'):
    replacements = { "gaston.parisier@bigbox.com.ar": "gaston.pena@newcompany.com.ar",
                     "cristian.prieto@bigbox.com.ar": "cristian.peralta@newcompany.com.ar",
                     "biogenesisbago": "client1",
                     "oslpasteur": "client2" ,
                     "melany.vidal@bigcorp.info": "melany.vidal@oldcompany.com.ar",
                     "josefina.avale@bigdeal.com.ar": "josefina.abad@oldcompany.com.ar",
                     "gonzalo.castro.penia@bigdeal.com.ar": "gonzalo.cabrera@newcompany.com.ar",
                     "gonzalo.castro.penia@bigbox.com.ar": "gonzalo.cabrera@newcompany.com.ar",
                     "matias@bigdeal.com.ar": "matias@oldcompany.com.ar",
                     "martin.aizaga@bigdeal.com.ar": "martin.arcos@oldcompany.com.ar",
                     "federico.casanova@bigdeal.com.ar": "federico.carmona@oldcompany.com.ar",
                     "caugusto.ojeda@hungrymachine.com": "caugusto.olmedo@oldcompany.com.ar",
                     "gisela.rovella@letsbonus.com": "gisela.rocha@oldcompany.com.ar",
                     "pablo.pittaluga@hungrymachine.com": "pablo.puig@oldcompany.com.ar",
                     "lucas.ferrario@bigdeal.com.ar": "lucas.fabregas@oldcompany.com.ar",
                     "sofidelio17@gmail.com": "sofia.delgado@gmail.com",
                     "romina.camacho@hungrymachine.com": "romina.casas@oldcompany.com.ar",
                     "malena@bigdeal.com.ar": "malena@oldcompany.com.ar",
                     "sebastian.gatti@hungrymachine.com": "sebastian.gibert@oldcompany.com.ar",
                     "nicolas.foti@bigdeal.com.ar": "nicolas.fuentes@oldcompany.com.ar",
                     "karina.pace@hungrymachine.com": "karina.perez@oldcompany.com.ar",
                     "maximo.videla@bigdeal.com.ar": "maximo.valdes@oldcompany.com.ar",
                     "jose.liendro@bigdeal.com.ar": "jose.lagos@oldcompany.com.ar",
                     "carolina.rea@bigdeal.com.ar": "carolina.rodriguez@oldcompany.com.ar",
                     "sofia.isnardi@hungrymachine.com": "sofia.ibanez@oldcompany.com.ar",
                     "sergio.dolfo@bigdeal.com.ar": "sergio.dario@oldcompany.com.ar",
                     "carolina.sevilla@hungrymachine.com": "carolina.sola@oldcompany.com.ar",
                     "maria.rivera@letsbonus.com": "maria.reig@oldcompany.com.ar",
                     "marcos.ribot@letsbonus.com": "marcos.ribot@oldcompany.com.ar",
                     "pablo.fernandez@bigdeal.com.ar": "pablo.fernandez@oldcompany.com.ar",
                     "florencia.torres@bigcorp.info": "florencia.tapia@oldcompany.com.ar",
                     "gonzalo.roget@hungrymachine.com": "gonzalo.ribas@oldcompany.com.ar",
                     "gabriel.cartuccia@bigdeal.com.ar": "gabriel.cabral@oldcompany.com.ar",
                     "leandro.marino@bigdeal.com.ar": "leandro.mayo@oldcompany.com.ar",
                     "ivana.casas@hungrymachine.com": "ivana.cerro@oldcompany.com.ar",
                     "yamila.shade@hungrymachine.com": "yamila.solana@oldcompany.com.ar",
                     "mariana.garau@hungrymachine.com": "mariana.gama@oldcompany.com.ar",
                     "nicolas.casanova@hungrymachine.com": "nicolas.cuevas@oldcompany.com.ar",
                     "flavia.medina@hungrymachine.com": "flavia.medrano@oldcompany.com.ar",
                     "cintia.matteo@bigdeal.com.ar": "cintia.mesa@oldcompany.com.ar",
                     "pilar.casasbellas@hungrymachine.com": "pilar.carballo@oldcompany.com.ar",
                     "francisco.suarez@hungrymachine.com": "francisco.serra@oldcompany.com.ar",
                     "natalia.papasidero@hungrymachine.com": "natalia.paez@oldcompany.com.ar",
                     "marcos.ball@bigcorp.info":"marcos.bianco@oldcompany.com.ar",
                     "julieta.danieli@letsbonus.com": "julieta.daza@oldcompany.com.ar",
                     "christian.janse": "christian.coronado",
                     "bigdeal": "oldcompany",
                     "big-deal": "oldcompany",
                     "bigbox": "newcompany",
                     "bigcorp.info": "oldcompany.com.ar",
                     "bigcorp": "oldcompany",
                     }
    with open(source_file) as infile, open(destination_file, 'w') as outfile:
        for line in infile:
            for src, target in replacements.iteritems():
                line = line.replace(src, target)
            outfile.write(line)