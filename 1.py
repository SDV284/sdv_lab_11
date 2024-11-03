import csv

def process_gdp_life_expectancy(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            us_data = {}
            ukraine_data = {}

            for row in reader:
                country = row['Country Name']
                if country == "United States":
                    for year in range(2010, 2020):
                        year_str = f"{year} [YR{year}]"
                        if year_str in row:
                            us_data[year] = float(row[year_str])

                elif country == "Ukraine":
                    for year in range(2010, 2020):
                        year_str = f"{year} [YR{year}]"
                        if year_str in row:
                            ukraine_data[year] = float(row[year_str])

            if not us_data or not ukraine_data:
                raise ValueError("Insufficient data for the US or Ukraine.")

            comparison_data = []
            for year in range(2010, 2020):
                comparison_data.append({
                    'Year': year,
                    'US Life Expectancy': us_data[year],
                    'Ukraine Life Expectancy': ukraine_data[year],
                    'Difference': us_data[year] - ukraine_data[year]
                })


        with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
            fieldnames = ['Year', 'US Life Expectancy', 'Ukraine Life Expectancy', 'Difference']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(comparison_data)

        print("Data processed successfully. Results saved to", output_filename)
        with open(input_filename, 'r', encoding='utf-8') as infile:
            print("\nContent of input file:")
            print(infile.read())
        
        with open(output_filename, 'r', encoding='utf-8') as outfile:
            print("\nContent of output file:")
            print(outfile.read())

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_csv_file = "gdp_life_expectancy.csv"
output_csv_file = "comparison_results.csv"
process_gdp_life_expectancy(input_csv_file, output_csv_file)