import pandas as pd
import sqlite3

def get_customer_spending_rank(db_path):
    conn = None
    try:
        query = """
            SELECT
                c.FirstName || ' ' || c.LastName AS FullName,
                c.Country,
                COUNT(i.InvoiceId) AS InvoiceCount,
                SUM(i.Total) AS TotalSpending
            FROM
                Customer c
            JOIN
                Invoice i ON c.CustomerId = i.CustomerId
            GROUP BY
                c.CustomerId
            ORDER BY
                TotalSpending DESC;
        """
        conn = sqlite3.connect(db_path)
        customer_rank_df = pd.read_sql_query(query, conn)
        customer_rank_df['TotalSpending'] = customer_rank_df['TotalSpending'].round(2)
        return customer_rank_df

    except sqlite3.Error as e:
        print(f"Lỗi truy vấn cơ sở dữ liệu: {e}")
        return None
    finally:
        if conn:
            conn.close()

database_file = '../databases/Chinook_Sqlite.sqlite'
full_ranking = get_customer_spending_rank(database_file)
if full_ranking is not None:
    print("BẢNG XẾP HẠNG CHI TIÊU CỦA KHÁCH HÀNG")
    print("Top 10 khách hàng hàng đầu")
    print(full_ranking.head(10).to_string(index=False))
