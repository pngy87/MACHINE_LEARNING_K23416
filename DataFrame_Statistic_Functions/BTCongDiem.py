'''
Input: df
Output: Top 3 sản phẩm bán ra nhưng có giá trị bán hàng lớn nhất (sản phẩm nào bán chạy nhất)
'''
import pandas as pd
def get_top_products_by_revenue(df, top_n=3):
    df['TotalRevenue'] = df['Quantity'] * df['UnitPrice'] * (1 - df['Discount'])
    product_revenue = df.groupby('ProductID')['TotalRevenue'].sum()
    top_products = product_revenue.sort_values(ascending=False).head(top_n)
    result_df = top_products.reset_index()
    result_df.columns = ['ProductID', 'TotalRevenue']
    return result_df

df = pd.read_csv('../datasets/SalesTransactions/SalesTransactions.csv')
top_3_products = get_top_products_by_revenue(df, top_n=3)
print("Top 3 sản phẩm có DOANH THU cao nhất")
print(top_3_products.to_string(index=False))