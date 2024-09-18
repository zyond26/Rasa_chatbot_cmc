import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('pokemon_data.csv')

# Xem xét thông tin tổng quát về dữ liệu
print(df.info())
print(df.head())

# Kiểm tra các giá trị bị thiếu
print(df.isnull().sum())

# Xử lý dữ liệu thiếu
# Ví dụ: Điền giá trị thiếu bằng giá trị trung bình của cột (nếu có cột số)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Chuyển đổi cột phân loại thành kiểu dữ liệu phù hợp
df['Type 1'] = df['Type 1'].astype('category')
df['Type 2'] = df['Type 2'].astype('category')

# Tạo cột mới nếu cần
# Ví dụ: Tạo cột 'Attack_Speed_Ratio' là tỷ lệ giữa Attack và Speed
df['Attack_Speed_Ratio'] = df['Attack'] / df['Speed'].replace(0, pd.NA)

# Xóa cột không cần thiết hoặc cột chứa dữ liệu không hợp lệ
df.drop(columns=['#'], inplace=True)  # Xóa cột '#', nếu không cần thiết

# Xem lại dữ liệu sau khi tiền xử lý
print(df.info())
print(df.head())

# Lưu dữ liệu đã tiền xử lý vào file mới
df.to_csv('pokemon_data_processed.csv', index=False)