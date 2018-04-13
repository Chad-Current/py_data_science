import pandas as pd
import numpy as np
import pickle
import h5py
import scipy.io


def type_diff():
    info = pd.read_csv('C:\\Users\ccurrent\\Desktop\\Check.csv',index_col=0)
    get_series = info['Age']
    get_dataframe = pd.DataFrame(info)
    get_np_arr = np.array(info)
    print('get_series')
    print(type(get_series))
    print(get_series)
    print('\n')
    print('get_dataframe')
    print(type(get_dataframe))
    print(get_dataframe)
    print('\n')
    print('get_np_arr')
    print(type(get_np_arr))
    print(get_np_arr)
    print('\n')
    check_old = info['Age'] > 40
    print('checking if age older than 40 with pd.series and np.array')
    print(type(get_series[check_old]))
    print(get_series[check_old])
    print('\n')
    print(type(get_np_arr[check_old]))
    print(get_np_arr[check_old])

def import_flat_files():
    """
    Basic text files containing records, table data
    Records:row of fields or attributes
    """
    file = 'C:\\Users\ccurrent\Desktop\Test.csv'
    # Numpy, Good for single type databases , but breaks down when you used mixed data types
    data = np.loadtxt(file,delimiter=',',skiprows=1,usecols=[0,1],dtype=str)
    # Numpy, Good for single type databases , but breaks down when you used mixed data types
    print('numpy array: \n',data)

    # Pandas importing and use
    pd_data = pd.read_csv(file)
    print('pandas head file \n',pd_data.head())
    print('convert from dataframe to numpy array \n',pd_data.values)

def other_file_types():
    file = 'C:\\Users\ccurrent\Desktop\PRO_TECT Radar Unit List.xls'
    # with open(file,'rb') as file:
    #     data = pickle.load(file)
    #     print(data)
    data = pd.ExcelFile(file)
    print(data.sheet_names)
    # df1 = data.parse(sheet_name='1')  # sheet name, as a string or
    # df2 = data.parse(0)  # sheet index, as a float

    # Parse the first sheet and rename the columns: df1
    # df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])
    #
    # # Print the head of the DataFrame df1
    # print(df1.head())
    #
    # # Parse the first column of the second sheet and rename the column: df2
    # df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country'])
    #
    # # Print the head of the DataFrame df2
    # print(df2.head())

    """ SAS Files"""
    # import sas7bdat import SAS7BDAT
    # with SAS7BDAT('urbanpop.sas7bdat') as file:
    #     df_sas = file.to_data_frame()
    """ STATA Files"""
    # data = pd.read_stata('urbanpop.dta')

def importing_hdf5_files():
    import h5py
    # filename = 'H-H1_LOSC_4_V1-1234123.hdf5'
    # data = h5py.File(filename,'r') # 'r' is to read
    # """Reading the structure of the h5fy file"""
    # for key in data.keys():
    #     print(key)
    #print structure of the h5fy file i.e. meta
    # for key in data['meta'].keys():
    #   print(key)

    #print(data['meta']['Description'].value, data['meta']['Detector'].value)

def importing_Matlab():
    import scipy.io
    # filename = 'workspace.mat'
    # mat = scipy.io.loadmat(filename)
    # print(type(mat))
    # <class 'dict'>

def relational_databases():
    pass




if __name__=='__main__':
    other_file_types()