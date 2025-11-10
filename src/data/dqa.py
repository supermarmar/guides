import pandera.pandas as pa

from src.const import MISSING_RATE_THRESHOLD_RED, MISSING_RATE_THRESHOLD_YELLOW


# Function to perform comprehensive data quality assessment
def data_quality_assessment(
    table_name: str,
    schema_class: pa.DataFrameModel,
    connection,
    sample_size: int = 10000,
):
    """
    Perform comprehensive DQA following BCBS 239 principles

    Parameters:
    - table_name: Name of the table to validate
    - schema_class: Pandera schema class for validation
    - connection: DuckDB connection
    - sample_size: Size of sample for validation (for performance)
    """

    print(f"\n{'=' * 60}")
    print(f"DATA QUALITY ASSESSMENT: {table_name.upper()}")
    print(f"{'=' * 60}")

    # 1. COMPLETENESS CHECK
    print("\n🔍 1. COMPLETENESS ASSESSMENT")
    print("-" * 40)

    # Get basic table info
    table_info_query = f"SELECT COUNT(*) as total_rows FROM {table_name}"
    total_rows = connection.execute(table_info_query).fetchone()[0]
    print(f"Total records in {table_name}: {total_rows:,}")

    # Sample data for validation (for performance on large tables)
    sample_query = f"""
        SELECT * FROM {table_name}
        USING SAMPLE {min(sample_size, total_rows)} ROWS
    """

    try:
        df_sample = connection.execute(sample_query).df()
        print(f"Sample size for validation: {len(df_sample):,} rows")

        # Calculate completeness metrics
        missing_stats = df_sample.isnull().sum()
        completeness_stats = (1 - missing_stats / len(df_sample)) * 100

        print("\nCompleteness by column (% non-null):")
        for col in df_sample.columns:
            completeness = completeness_stats[col]
            status = (
                "✅"
                if completeness >= MISSING_RATE_THRESHOLD_YELLOW
                else "⚠️" if completeness >= MISSING_RATE_THRESHOLD_RED else "❌"
            )
            print(f"  {status} {col}: {completeness:.1f}%")

        # 2. SCHEMA VALIDATION
        print("\n🔍 2. SCHEMA VALIDATION (ACCURACY & UNIQUENESS ASSESSMENT)")
        print("-" * 40)

        try:
            validated_df = schema_class.validate(df_sample, lazy=True)
            print("✅ Schema validation & Uniqueness assessment PASSED")
            print(f"   - All {len(validated_df)} sample records conform to schema")

            # 3. TIMELINESS CHECK (if date columns exist)
            print("\n🔍 3. TIMELINESS ASSESSMENT")
            print("-" * 40)

            date_columns = df_sample.select_dtypes(include=["datetime64"]).columns
            if len(date_columns) > 0:
                for date_col in date_columns:
                    min_date = df_sample[date_col].min()
                    max_date = df_sample[date_col].max()
                    print(f"  📅 {date_col}: {min_date} to {max_date}")
            else:
                print("  ⚠️ No datetime columns detected for timeliness assessment")

            # 4. SUMMARY
            print("\n📊 DQA SUMMARY")
            print("-" * 40)
            print("  Schema Compliance: ✅ PASSED")
            print(f"  Sample Size: {len(df_sample):,} / {total_rows:,} records")
            print(f"  Avg Completeness: {completeness_stats.mean():.1f}%")

            return True, validated_df

        except pa.errors.SchemaErrors as e:
            print("❌ Schema validation FAILED")
            print(f"   Number of errors: {len(e.schema_errors)}")

            # Show first few errors
            for i, error in enumerate(e.schema_errors[:3]):
                print(f"   Error {i + 1}: {error}")

            if len(e.schema_errors) > 3:
                print(f"   ... and {len(e.schema_errors) - 3} more errors")

            return False, None

    except Exception as e:
        print(f"❌ Error during DQA: {str(e)}")
        return False, None
