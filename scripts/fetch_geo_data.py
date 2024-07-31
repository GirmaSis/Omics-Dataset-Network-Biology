# Access GEO Data Using GEOparse API

import GEOparse

# Define the GEO accession number: Global gene expression profiling of human pleural mesotheliomas
geo_accession = 'GSE12345'

# Fetch the GEO dataset
gse = GEOparse.get_GEO(geo=geo_accession, destdir="./data")

# Extract sample data and save to CSV
samples = gse.pivot_samples('VALUE')
samples.to_csv('data/GSE12345_samples.csv')

# Print the first few rows of the data
print(samples.head())
