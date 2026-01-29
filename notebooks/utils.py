#FUNCTION TO HAVE A GENERAL OVERVIEW OF A DATASET
def general_overview(df):
    print(f"{'Column Name':<40} | {'Type':<10} | {'Missing':<15} | {'Unique':<10} | {'Sample Values'}")
    print("-" * 110)

    for col in df.columns:
        dtype = str(df[col].dtype)
        
        missing_count = df[col].isnull().sum()
        missing_pct = (missing_count / len(df)) * 100
        missing_str = f"{missing_count} ({missing_pct:.1f}%)"
        
        n_unique = df[col].nunique()
        
        if len(df[col].dropna()) > 0:
            sample_vals = df[col].dropna().unique()
            if len(sample_vals) > 3:
                sample_vals = sample_vals[:3]
            examples = ", ".join(str(v) for v in sample_vals)
        else:
            examples = "All Empty"
            
        print(f"{col:<40} | {dtype:<10} | {missing_str:<15} | {n_unique:<10} | {examples}")