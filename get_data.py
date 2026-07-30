# Function to download the dataset
def get_data():
    import kagglehub

    path = kagglehub.dataset_download(
        'alexisbcook/geospatial-learn-course-data', # Location of the dataset on kaggle
        output_dir = 'data/', # Output directory
        force_download = True # Force download even if the file already exists
    )

    print("Download complete!")
    print("Path to data files:", path)


if __name__ == "__main__":
    get_data()
