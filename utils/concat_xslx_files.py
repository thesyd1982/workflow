import pandas as pd
import glob

xslx_files = glob.glob('urrh*.xlsx')


def concat_xslx_files(xslxfiles, output_filename, sheet_name='Sheet1'):
	data_frame = [pd.read_excel(xslxfile, sheet_name) for xslxfile in xslxfiles]
	df_master = pd.concat(data_frame)
	df_master.to_excel(output_filename, index=False)


# for file in xslx_files:
# print(file)
# tag = file.split('_')[0]
# middle_name = file.split('_')[1].replace('.xlsx', '')

# if middle_name == 'companies':
# middle_name = '_company_'

# else:
# middle_name = '_'

# profile = 'linkedin' + middle_name + 'profile'
# df = pd.read_excel(file)
# df.columns.values[0] = profile
# df.columns = df.columns.str.upper()

# df.to_excel(file, index=False)

companies = [file for file in xslx_files if 'companies' in file]

profiles = [file for file in xslx_files if 'companies' not in file]
print(companies)
concat_xslx_files(companies, '../bots/output/master_companies_urrh.xlsx')
print(profiles)
concat_xslx_files(profiles, '../bots/output/master_users_urrh.xlsx')
