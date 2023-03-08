import os
import configparser as cp

globals().update(os.environ)

frps_ini = cp.ConfigParser()
frps_ini.read('frps.ini', encoding='utf8')

for section in frps_ini.sections():
    for option in frps_ini.options(section):
        env_arg_str = f'{section}_{option}'.upper()
        if env_arg_str in globals():
            frps_ini[section][option] = eval(env_arg_str)
            
with open('frps.ini', 'w+', encoding='utf8') as ini_file:
    frps_ini.write(ini_file)
