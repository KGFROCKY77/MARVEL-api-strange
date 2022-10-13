def gen_filter(df_63,column_name,filter):
    if filter[0]== '>':
        res_obt_df = df_63[df_63[column_name]>filter[1]]
    if filter[0]== '<':
        res_obt_df= df_63[df_63[column_name]<filter[1]]
    return res_obt_df